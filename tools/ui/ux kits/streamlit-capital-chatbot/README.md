# Streamlit Capital Chatbot (LangChain + OpenAI)

## Project Path
`ui/ux kits/streamlit-capital-chatbot`

## What It Does
- Takes a country name from the user
- Uses LangChain `ChatOpenAI` to return the capital city
- Shows chat interaction in Streamlit

## Setup
1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your OpenAI key:
   ```bash
   export OPENAI_API_KEY="your_key_here"
   ```

## Run Tests
```bash
pytest -q
```

## Run App
```bash
streamlit run app.py
```

## Notes
- If input is not a valid country, the assistant is instructed to return `Unknown country.`
- Keep `OPENAI_API_KEY` in your environment or in a local `.env` file.
