# Gradio Capital Chatbot (LangChain + OpenAI)

## Project Path
`ui/ux kits/gradio-capital-chatbot`

## What It Does
- Takes a country name from the user
- Uses LangChain `ChatOpenAI` to return the capital city
- Shows interaction in a Gradio web interface

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your OpenAI key:
   ```bash
   export OPENAI_API_KEY="your_key_here"
   ```

## Run Tests
```bash
pytest -q
```

## Run App
```bash
python app.py
```
