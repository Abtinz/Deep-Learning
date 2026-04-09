import json
import os
import re
import ssl
from typing import Any

import certifi
from dotenv import load_dotenv
from langchain_tavily import TavilyCrawl
import crawl_configs

def setup_env() -> None:
    """Load environment variables and SSL settings for Tavily requests.

    Raises:
        RuntimeError: If `TAVILY_API_KEY` is missing.
    """
    load_dotenv()
    os.environ["SSL_CERT_FILE"] = certifi.where()
    os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
    ssl.create_default_context(cafile=certifi.where())

    if not os.getenv("TAVILY_API_KEY"):
        raise RuntimeError(
            "Missing TAVILY_API_KEY. Create .env from .env.example and set your API key."
        )


def run_crawl(crawler: TavilyCrawl, payload: dict[str, Any]) -> list[dict[str, Any]]:
    """Run a Tavily crawl and return the `results` list.

    Args:
        crawler: Initialized Tavily crawler instance.
        payload: Tavily crawl request payload.

    Returns:
        List of crawl result dictionaries.
    """
    result = crawler.invoke(payload)
    return result.get("results", [])


def print_sample(title: str, rows: list[dict[str, Any]], limit: int = 3) -> None:
    """Print a small preview of crawl results.

    Args:
        title: Section title to print.
        rows: Crawl result rows to preview.
        limit: Maximum number of rows to print.
    """
    print(f"\n{title}: {len(rows)} pages")
    for i, item in enumerate(rows[:limit], start=1):
        url = item.get("url", "N/A")
        raw = item.get("raw_content", "") or ""
        preview = raw[:400].replace("\n", " ")
        print(f"{i}. {url}")
        print(f"   {preview}...")


def clean_text(text: str) -> str:
    """Normalize whitespace in extracted content.

    Args:
        text: Raw text to clean.

    Returns:
        Cleaned single-line text.
    """
    collapsed = re.sub(r"\s+", " ", text).strip()
    return collapsed


def save_results(name: str, rows: list[dict[str, Any]]) -> None:
    """Save raw crawl data to JSON and cleaned text output.

    Args:
        name: File prefix for output files.
        rows: Crawl result rows to save.

    """
    os.makedirs("crawled", exist_ok=True)

    json_path = os.path.join("crawled", f"{name}.json")
    txt_path = os.path.join("crawled", f"{name}.txt")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

    cleaned_blocks: list[str] = []
    for idx, item in enumerate(rows, start=1):
        url = item.get("url", "N/A")
        raw = item.get("raw_content", "") or ""
        cleaned = clean_text(raw)
        cleaned_blocks.append(f"[{idx}] {url}\n{cleaned}")

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(cleaned_blocks))

    print(f"Saved: {json_path}")
    print(f"Saved: {txt_path}")


def main() -> None:

    setup_env()
    crawler = TavilyCrawl()

    basic_results = run_crawl(
        crawler,
        {
            "url": crawl_configs.URL,
            "max_depth": crawl_configs.MAX_DEPTH,
            "extract_depth": crawl_configs.EXTRACT_DEPTH,
        },
    )

    print_sample("Baseline crawl (no instructions)", basic_results)
    save_results("baseline_results", basic_results)

    guided_results = run_crawl(
        crawler,
        {
            "url": crawl_configs.URL,
            "instructions": crawl_configs.INSTRUCTIONS,
            "max_depth": crawl_configs.MAX_DEPTH,
            "extract_depth": crawl_configs.EXTRACT_DEPTH,
        },
    )

    print_sample("Instruction-guided crawl", guided_results)
    save_results("guided_results", guided_results)

    if basic_results:
        noise_reduction = ((len(basic_results) - len(guided_results)) / len(basic_results)) * 100
        print(f"\nEstimated noise reduction: {noise_reduction:.1f}%")
    else:
        print("\nBaseline crawl returned no results; cannot compute reduction.")


if __name__ == "__main__":
    main()
