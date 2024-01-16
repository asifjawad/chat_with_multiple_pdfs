import streamlit as st
from dotenv import load_dotenv
from src.utils import get_pdf_text, get_text_chunks, get_vector_store, get_conversation_chain

from components.html_temp import css, user_template, bot_template

def handle_user_input(user_question):
    response = st.session_state.conversation({'question': user_question})
    # st.write(response)

    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2== 0:
            st.write(user_template.replace("{{MSG}}", message.content ), unsafe_allow_html=True)

        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)







def main():
    load_dotenv()
    st.set_page_config(page_title="Searching from PDF", page_icon=":books:")

    st.write(css, unsafe_allow_html=True)

 
    if "conversation" not in st.session_state:
        st.session_state.conversation = None


    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chatting with several PDFs :")
    user_question = st.text_input("What you want to know from your uploaded pdfs")

    if user_question:
        handle_user_input(user_question)

    st.write(user_template.replace("{{MSG}}", "Hi, This is Jawad, You can ask any Question"), unsafe_allow_html=True)
    st.write(bot_template.replace("{{MSG}}", "hello"), unsafe_allow_html=True)


    with st.sidebar:
        st.subheader("Your Documents") 
        pdf_docs = st.file_uploader("Upload your PDFs here", accept_multiple_files=True)
        if st.button("Upload"):
            with st.spinner("Uploading files"):
                # get pdf
                raw_text = get_pdf_text(pdf_docs)

                # get the chunks

                chunks_text = get_text_chunks(raw_text)
                # st.write(chunks_text)

                # create vector store
                vectors = get_vector_store(chunks_text)

                #starting conversation
                st.session_state.conversation = get_conversation_chain(vectors)

    # st.session_state.conversation

if __name__ == '__main__':
    main()