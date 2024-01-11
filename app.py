import streamlit as st
from dotenv import load_dotenv
from src.utils import get_pdf_text

# from PyPDF2 import PdfReader




def main():
    load_dotenv()
    st.set_page_config(page_title="Searching from PDF", page_icon=":books:")

    st.header("Chatting with several PDFs :")
    st.text_input("What you want to know from your uploaded pdfs")


    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your PDFs here", accept_multiple_files=True)
        if st.button("Upload"):
            with st.spinner("Uploading files"):
                # get pdf
                raw_text = get_pdf_text(pdf_docs)
                st.write(raw_text)

                # get the chunks

                # create vector store


if __name__ == '__main__':
    main()