# main.py

import sys
import os

# Ensure the project root is in sys.path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)


import streamlit as st
from app import config, utils
from backend_services import pdf_parser, text_cleaner, embedder
from modules import summarizer, keyword_extractor, domain_classifier, citation_extractor, plagiarism_checker
from modules.plagiarism_checker import check_plagiarism

import os
import tempfile

# App Config
st.set_page_config(page_title=config.APP_TITLE, page_icon=config.APP_ICON)
st.title(f"{config.APP_ICON} {config.APP_TITLE}")
st.write(config.APP_DESCRIPTION)

# Inject custom CSS
# with open("assets/css/style.css") as f:
#   st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📂 Module Selector")
module = st.sidebar.radio("Choose a function:", [
    "Upload & Preview",
    "Summarization",
    "Keyword Extraction",
    "Domain Classification",
    "Citation Extraction",
    "Plagiarism Checker",
])

# File uploader
uploaded_file = st.sidebar.file_uploader("📤 Upload a PDF File", type="pdf")

# Check file validity
if uploaded_file and utils.allowed_file(uploaded_file.name):

    # Save temporarily
    temp_dir = tempfile.TemporaryDirectory()
    file_path = os.path.join(temp_dir.name, utils.format_filename(uploaded_file))
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # Extract & clean text
    raw_text = pdf_parser.extract_text_from_pdf(file_path)
    cleaned_text = text_cleaner.clean_text(raw_text)

    st.success("✅ File processed successfully!")

    # Show selected module output
    if module == "Upload & Preview":
        st.subheader("📄 Extracted Paper Preview")
        st.text_area("Raw Extracted Text", value=utils.truncate_text(raw_text, 500), height=400)

    elif module == "Summarization":
        st.subheader("🧠 Summarized Content")
        summary = summarizer.summarize(cleaned_text, method="t5")
        st.success("📝 Summary Generated Below:")
        st.write(summary)

    elif module == "Keyword Extraction":
        st.subheader("🔑 Extracted Keywords with Scores")
        keywords = keyword_extractor.extract_keywords(cleaned_text, top_n=config.TOP_N_KEYWORDS)
        if keywords and isinstance(keywords, list):
            try:
                for idx, (word, score) in enumerate(keywords, start=1):
                    st.markdown(f"**{idx}. {word}** — `{round(float(score), 2)}`")
            except Exception as e:
                st.error(f"Error displaying keywords: {e}")
        else:
            st.warning("No keywords extracted or format is invalid.")


    elif module == "Domain Classification":
        st.subheader("🧪 Predicted Domain")
        domain = domain_classifier.classify_paper(cleaned_text)
        st.info(f"📘 The paper belongs to the domain: **{domain}**")

    elif module == "Citation Extraction":
        st.subheader("📌 Extracted Citations")
        citations = citation_extractor.extract_citations(raw_text)
        if citations:
            for i, c in enumerate(citations, 1):
                st.markdown(f"**[{i}]** {c}")
        else:
            st.warning("⚠️ No citations found or recognized.")

    elif module == "Plagiarism Checker":
        st.subheader("⚠️ Plagiarism Report")

        try:
            matches = check_plagiarism(cleaned_text, threshold=0.8)

            if matches:
                for i, (text, score) in enumerate(matches):
                    st.write(f"**Match {i + 1}:** Similarity: `{score:.2f}`")
                    st.info(text)
            else:
                st.success("✅ No significant plagiarism detected.")
        except ValueError as e:
            st.error(f"Error: {str(e)}")

else:
    st.warning("📎 Please upload a valid `.pdf` file to begin.")

# Footer
st.sidebar.markdown("""
---
Made with ❤️ by [Amal Prasad Trivedi](https://www.linkedin.com/in/amalprasadtrivedi-aiml-engineer/)
---
""")
