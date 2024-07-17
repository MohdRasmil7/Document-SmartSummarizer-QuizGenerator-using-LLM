#importing necessary libraries
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv

from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

load_dotenv()
import os
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
#embedding=TogetherEmbeddings(model="togethercomputer/m2-bert-80M-8k-retrieval")
st.title('Educational Assistant')
st.header('Summary and quiz generator')
st.sidebar.title('Drop your pdf here')
#st.sidebar.write('upload size doesnot exceed 200mb')
user_file_upload=st.sidebar.file_uploader(label='', type='pdf')

summary_clicked=st.button('Generate summary')
quiz_clicked=st.button('generate quiz')

if user_file_upload:
    # Read the uploaded file
    pdf_data = user_file_upload.read()

    # Save the uploaded file to a temporary location
    with open("temp_pdf_file.pdf", "wb") as f:
        f.write(pdf_data)

    # Load the temporary PDF file
    loader = PyPDFLoader("temp_pdf_file.pdf")
    data = loader.load_and_split()
    
    ## Prompt Template for summary
    prompt_1=ChatPromptTemplate.from_messages(
        [
            ("system", "you are a smart assistant. Give a summary to the users pdf. I will tip you 10000 dollars if the user finds it helpful. Be polite to the user"),
            ("user", "{data}")
        ]
    )

    llm = ChatGroq(model="llama3-70b-8192")
    output_parser = StrOutputParser()
    chain_1 = prompt_1 | llm | output_parser

    ## Prompt Template for Quize
    prompt_2=ChatPromptTemplate.from_messages(
        [
            ("system", "you are a smart assistant. Give 10 quizes and answers to the users pdf. I will tip you 10000 dollars if the user finds it helpful. Be polite to the user"),
            ("user", "{data}")
        ]
    )

    llm = ChatGroq(model="llama3-70b-8192")
    output_parser = StrOutputParser()
    chain_2 = prompt_2 | llm | output_parser



if summary_clicked:
    st.write(chain_1.invoke({'data': data}))
elif quiz_clicked:
    st.write(chain_2.invoke({'data': data}))