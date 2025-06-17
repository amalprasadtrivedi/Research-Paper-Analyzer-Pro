# about.py

import streamlit as st

def show_about_page():
    st.set_page_config(page_title="About", page_icon="ℹ️")
    st.title("📖 About Research Paper Analyzer Pro")

    st.markdown("""
    ## 🔍 Overview
    **Research Paper Analyzer Pro** is an AI-powered, interactive application that assists researchers, students, and academics in analyzing research papers with ease, efficiency, and intelligence.

    ---

    ## 🌟 Key Features

    - 📄 **PDF Parser** – Extracts structured text from uploaded research papers using `PyMuPDF`.
    - 🧠 **AI-Based Summarizer** – Generates concise and coherent summaries using `BERT`, `T5`, and `TextRank`.
    - 🔑 **Keyword & Topic Extraction** – Automatically extracts key topics and terms using TF-IDF and RAKE.
    - 🧪 **Domain Classifier** – Classifies papers into fields like CS, Biology, Medicine, and more using a trained ML model.
    - 🔍 **Citation Extractor** – Parses both inline citations and bibliography references from academic papers.
    - ⚠️ **Plagiarism Detector** – Uses semantic similarity (SBERT) to flag content similar to known sources.
    - 📌 **Research Insights Panel** – Get a quick overview of the structure and core ideas of the paper.
    - 🧾 **Reference Analyzer** – Detect citation styles (APA, MLA, IEEE) and provide structured citation outputs.
    - 🎯 **Searchable Corpus Support** – Compare new papers with a custom or global corpus using cosine similarity.
    - 🧹 **Text Cleaner** – Applies advanced NLP techniques to sanitize, normalize, and tokenize academic text.

    ---

    ## 🧰 Tech Stack

    - 🖥 **Frontend**: Streamlit, HTML/CSS (custom theming)
    - 🧠 **NLP Models**: Sentence-BERT, T5, BERT, TextRank
    - 🧮 **ML & Data Science**: Scikit-learn, NumPy, Pandas
    - 📚 **NLP Preprocessing**: NLTK, spaCy
    - 📎 **PDF Parsing**: PyMuPDF (fitz)
    - 📦 **Storage**: Pickle, Local file system
    - 🔄 **Embedding Similarity**: Sentence Transformers + Cosine Similarity

    ---

    ### 🚀 Vision

    Our mission is to **automate the tedious aspects of research reading** and help students, researchers, and educators **digest complex papers faster** using AI.

    Future updates will include:
    - 💬 Chatbot interface for interactive paper querying
    - 📈 Graph-based citation analysis
    - 🌐 Research trend prediction using time-series NLP

    ---

    ## 🗂️ Project Structure

    ```
    research-paper-analyzer-pro/
    ├── app/                        # Streamlit UI and config
    ├── modules/                    # NLP/ML processing logic
    ├── backend_services/           # PDF parsing, embeddings
    ├── data/                       # Dataset and embeddings
    ├── assets/                     # Models, CSS, sample papers
    └── notebooks/                  # Jupyter R&D scripts
    ```

    ---

    ## 👨‍💻 Developer

    **Amal Prasad Trivedi**  
    B.Tech CSE (AI & ML), Ambalika Institute of Management and Technology  
    📫 `amaltrivedi3904stella@gmail.com`  
    🔗 [LinkedIn](https://www.linkedin.com/in/amalprasadtrivedi-aiml-engineer/)  
    💼 [Portfolio](https://amalprasadtrivediportfolio.vercel.app/)  
    🐙 [GitHub](https://github.com/amalprasadtrivedi)

    ---

    ## 🤝 Contribute

    Want to help improve this project?

    - 🧠 Suggest new AI modules
    - 📝 Report bugs or feature requests
    - ⭐ Star the GitHub repo and fork for contributions

    Pull requests are welcome!

    ---

    ## 📌 Disclaimer

    This tool is meant for **educational and research assistance** only. The plagiarism checker provides **semantic similarity**, not legally verified plagiarism scoring.

    """)

    # Footer
    st.sidebar.markdown("""
    Made with ❤️ by [Amal Prasad Trivedi](https://www.linkedin.com/in/amalprasadtrivedi-aiml-engineer/)
    ---
    """)


# Run when this file is executed directly
if __name__ == "__main__":
    show_about_page()
