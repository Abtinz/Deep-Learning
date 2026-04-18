import streamlit as st

from main import run_reflexion

st.set_page_config(page_title="Reflexion Assistant", page_icon="R", layout="centered")

st.markdown(
    """
<style>
:root {
  --cream: #EDE9E6;
  --gold: #C9996B;
  --brown: #5C4F4A;
  --sage: #5C766D;
}

html, body, [class*="css"], .stApp, .stMarkdown, .stTextInput, .stTextArea, .stButton {
  font-family: "Times New Roman", Times, serif !important;
}

.stApp {
  background: linear-gradient(160deg, var(--cream) 0%, #f5f1ed 100%);
}

h1, h2, h3 {
  color: var(--brown);
  letter-spacing: 0.2px;
}

.subtitle {
  color: var(--sage);
  margin-bottom: 0.75rem;
}

label, .stMarkdown p, .stSpinner, .stSpinner > div {
  color: var(--sage) !important;
}

div[data-baseweb="textarea"] textarea {
  background-color: #fffaf6 !important;
  border: 1px solid var(--brown) !important;
  color: var(--brown) !important;
}

.stButton > button {
  background-color: var(--gold) !important;
  color: #ffffff !important;
  border: 1px solid var(--brown) !important;
  border-radius: 8px !important;
  padding: 0.5rem 1rem !important;
  font-weight: 600 !important;
}

.stButton > button:hover {
  background-color: var(--sage) !important;
  border-color: var(--sage) !important;
}

.result-box {
  background: #ffffffd9;
  border: 1px solid var(--gold);
  border-left: 6px solid var(--sage);
  border-radius: 10px;
  padding: 1rem;
  color: var(--brown);
}
</style>
""",
    unsafe_allow_html=True,
)

st.title("Reflexion Assistant")
st.markdown(
    '<p class="subtitle">Ask a question and get a researched, revised answer.</p>',
    unsafe_allow_html=True,
)

question = st.text_area(
    "Your question",
    placeholder="Example: What are the latest trends in AI-powered SOC startups?",
    height=140,
)

if st.button("Generate Answer"):
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Researching and revising..."):
            try:
                answer = run_reflexion(question.strip())
                st.markdown(
                    f'<div class="result-box">{answer}</div>',
                    unsafe_allow_html=True,
                )
            except Exception as exc:
                st.error(f"Failed to generate answer: {exc}")
