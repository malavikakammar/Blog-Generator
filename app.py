import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import os

os.environ['GOOGLE_API_KEY'] = os.getenv('google_api')

def blog_generator(input_text,no_of_words,blog_type):
    
    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest")

    template ="""
    You are Blog Generative Expert Assistant.
    Create a blog on topic {input_text} for {blog_type} with words limit {no_of_words}. 
    Give as much creative blogs as possible.
    """

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({
        "input_text":input_text,
        "no_of_words":no_of_words,
        "blog_type":blog_type
    })




st.set_page_config(page_title="Blog Generator", page_icon='robot',layout='centered')

st.header("Blog Generator 🤖")

input_text = st.text_input('Enter the topic for Blog...')

col1,col2 = st.columns([5,5])

with col1:
    no_of_words = st.text_input("Enter the number of words...")
with col2:
    blog_type = st.selectbox('Write the blog for',('Researchers','Data Scientist','General People'),index=0)

submit = st.button('Submit')

if submit:
    st.info(blog_generator(input_text,no_of_words,blog_type))


