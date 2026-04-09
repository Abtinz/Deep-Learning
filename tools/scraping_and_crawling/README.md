# Scraping and Crawling

Simple Tavily crawl demo adapted from:
`Tavily Crawl Demo Tutorial.ipynb`

Source:
`https://github.com/emarco177/documentation-helper/blob/main/Tavily%20Crawl%20Demo%20Tutorial.ipynb`

## What this folder includes

- `Tavily_Crawl_Demo_Tutorial.ipynb`: simplified notebook version
- `crawl_demo.py`: script version of the same flow
- `requirements.txt`: minimal dependencies
- `.env.example`: environment variable template

## Quick start

1. Run setup script:
   `sh setup_env.sh`
2. Create `.env` from `.env.example` and set your key:
   `TAVILY_API_KEY=...`
3. Activate env:
   `source .venv/bin/activate`
4. Run:
   `python crawl_demo.py`

## Notes

- This demo compares:
  - baseline crawl (no instructions)
  - instruction-guided crawl (`"Find all pages about ai agents"`)
- Target URL defaults to:
  `https://python.langchain.com/`
