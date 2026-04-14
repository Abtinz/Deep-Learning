import json

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from typing import Any, Literal
import ssl
import certifi
import os
import re
from langchain_tavily import TavilySearch, TavilyCrawl

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

def clean_text(text: str) -> str:
    """Normalize whitespace in extracted content.

    Args:
        text: Raw text to clean.

    Returns:
        Cleaned single-line text.
    """
    collapsed = re.sub(r"\s+", " ", text).strip()
    return collapsed

@tool()
def save_results(name: str, rows: list[dict[str, Any]]) -> None:
    """Save raw crawl data to JSON and cleaned text output.

    param name: File prefix for output files.
    param rows: Crawl result rows to save.
    returns: None
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


def normalize_extract_depth(
    extract_depth: Literal["basic", "advanced"] | int,
) -> Literal["basic", "advanced"]:
    """Map legacy integer depth values to Tavily's current literal API."""
    if isinstance(extract_depth, int):
        return "advanced" if extract_depth > 0 else "basic"
    return extract_depth

@tool()
def triple(number:float) -> float:
    """ This function will get a float number and multiple it by 3

    param number: a number to triple
    returns: the triple of the input number
    """
    return number * 3

@tool()
def tavily_crawl(
    url: str,
    max_depth: int = 1,
    extract_depth: Literal["basic", "advanced"] | int = "advanced",
) -> list[dict[str, Any]]:
    ''' This function will perform a crawl using TavilyCrawl tool and return the results
    param url: the url to crawl
    param max_depth: the maximum depth to crawl
    param extract_depth: the depth to extract content from
    returns: the results of the crawl
    '''
    crawler = TavilyCrawl()
    normalized_depth = normalize_extract_depth(extract_depth)

    basic_results = run_crawl(
        crawler,
        {
            "url": url,
            "max_depth": max_depth,
            "extract_depth": normalized_depth,
        },
    )

    return basic_results

setup_env()

tools =[TavilySearch(max_results=1), triple, save_results, tavily_crawl]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools(tools)
