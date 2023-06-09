import validators
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import UnstructuredURLLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate

# Streamlit app
st.subheader('Summarize URL')

# Get OpenAI API key and URL to be summarized
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API key", value="", type="password")
    st.caption("*If you don't have an OpenAI API key, get it [here](https://platform.openai.com/account/api-keys).*")
url = st.text_input("URL", label_visibility="collapsed")

# If 'Summarize' button is clicked
if st.button("Summarize"):
    # Validate inputs
    if not openai_api_key.strip() or not url.strip():
        st.error("Please provide the missing fields.")
    elif not validators.url(url):
        st.error("Please enter a valid URL.")
    else:
        try:
            with st.spinner("Please wait..."):
                # Load URL data
                url_loader = UnstructuredURLLoader(urls=[url])
                data = url_loader.load()
                
                # Initialize the ChatOpenAI module, load and run the summarize chain
                chat_model = ChatOpenAI(temperature=0, model='gpt-3.5-turbo', openai_api_key=openai_api_key)
                prompt_template = """Write a summary of the following in 200-250 words:
                    
                    {text}

                """
                prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
                summarize_chain = load_summarize_chain(chat_model, chain_type="stuff", prompt=prompt)
                summary = summarize_chain.run(data)

                st.success(summary)
        except Exception as e:
            st.exception(f"Exception: {e}")

