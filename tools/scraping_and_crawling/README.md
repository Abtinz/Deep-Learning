# Tavily Scraping and Crawling Demo

This project is a practical, lightweight demo of **Tavily Crawl** for collecting web data you can use in RAG pipelines, search workflows, and documentation ingestion.

Source inspiration:
`https://github.com/emarco177/documentation-helper/blob/main/Tavily%20Crawl%20Demo%20Tutorial.ipynb`

## What is Tavily and why it is useful

TavilyCrawl is an intelligent web crawler that uses AI to determine which paths to explore during crawling. It combines AI-powered decision making with parallel processing capabilities.
Key Features:

    - AI-Powered Path Selection: Uses AI to determine which paths to explore
    - Parallel Processing: Explores hundreds of paths simultaneously
    - Advanced Extraction: Extracts content from dynamically rendered pages
    - Instruction-Driven: Follows natural language instructions to guide exploration
    - Targeted Content: Returns content tailored for LLM integration and RAG systems


In this demo, we compare:
- Baseline crawl (no instructions)
- Guided crawl (`Find all pages about ai agents`)

## Project files

- `crawl_demo.py`: main runnable script
- `Tavily_Crawl_Demo_Tutorial.ipynb`: notebook version
- `setup_env.sh`: creates `.venv`, installs dependencies, and registers Jupyter kernel
- `run.sh`: one-command setup + run flow
- `requirements.txt`: dependencies
- `.env.example`: API key template
- `crawled/`: generated JSON/TXT outputs (git-ignored)

## Quick start (recommended)

1. Add your Tavily key:
```bash
cp .env.example .env
# edit .env and set TAVILY_API_KEY=...
```

2. Run everything:
```bash
./run.sh
```

This will:
- ensure virtual environment is ready
- install requirements
- register notebook kernel: `Python (scraping-and-crawling)`
- run the crawl demo
- save outputs in `crawled/`

## Manual commands

```bash
sh setup_env.sh
source .venv/bin/activate
python crawl_demo.py
```

## Output files

After a run, you will see:
- `crawled/baseline_results.json`
- `crawled/baseline_results.txt`
- `crawled/guided_results.json`
- `crawled/guided_results.txt`

JSON stores raw retrieved records.
TXT stores cleaned, readable text extracted from those records.
