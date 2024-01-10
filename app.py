import streamlit as st
from dotenv import load_dotenv

def main():
    st.set_page_config(page_title="Searching from PDF", page_icon=":books:")

    st.header("Chatting with several PDFs :")
    st.text_input("What you want to know from your uploaded pdfs")


    with st.sidebar:
        st.subheader("Your Documents")
        st.file_uploader("Upload your PDFs here")
        st.button("Upload")


if __name__ == '__main__':
    main()