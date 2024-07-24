# Unleash Your Knowledge Wizard: Summaries and Quizzes Made Easy! 📚✨

## Overview

This project is an Educational Assistant powered by Large Language Models (LLM). It allows users to generate summaries and quizzes related to PDFs that users have uploaded. The chatbot leverages the LLM model to enhance its performance. 🤖📝

![](assets/Demo1.png) ![](assets/Demo2.png)

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [Code Explanation](#code-explanation)
7. [Future Enhancements](#future-enhancements)
8. [Contact](#contact)

## Introduction

This Educational Assistant is designed to simplify the process of summarizing and generating quizzes from PDF documents. Users can upload their documents, and the assistant will provide concise summaries and quizzes based on the content.

## Features

- Utilizes LLM for natural language understanding and generation.
- Allows users to generate quizzes and summaries from uploaded PDFs.
- Provides accurate and concise responses.
- User-friendly interface for seamless interaction. 🖥️

## Technologies Used

- **Python** 
- **Streamlit**: For building the web interface
- **LangChain**: For implementing the RAG model
- **PyPDF2**: For processing PDF documents
- **FAISS**: For efficient similarity search
- **Google Generative AI**: For generating embeddings
- **Groq API**: For advanced LLM functionalities
- **Llama3 Model**

## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-repo/EducationalAssistant.git
   cd EducationalAssistant

2. **Install the required packages:**

   bash
   pip install -r requirements.txt
   

3. **Set up environment variables:**

   Create a `.env` file in the root directory and add your API keys:

   
   GROQ_API_KEY=your_groq_api_key
   

4. **Run the Streamlit application:**

   bash
   streamlit run app.py

## Usage
1. Open the application in your web browser.
2. Upload your PDF document via the sidebar.
3. Select "Generate Summary" or "Generate Quiz" based on your needs. 📄🔍

## Code Explanation

### Importing Required Libraries

import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

load_dotenv()
import os
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")



### Streamlit UI Elements

st.title('Educational Assistant')
st.header('Summary and Quiz Generator')
st.sidebar.title('Drop your PDF here')
user_file_upload = st.sidebar.file_uploader(label='', type='pdf')
summary_clicked = st.button('Generate Summary')
quiz_clicked = st.button('Generate Quiz')



### Handling PDF Upload and Loading

if user_file_upload:
    pdf_data = user_file_upload.read()
    with open("temp_pdf_file.pdf", "wb") as f:
        f.write(pdf_data)
    loader = PyPDFLoader("temp_pdf_file.pdf")
    data = loader.load_and_split()



### Prompt Templates for Summary and Quiz Generation

prompt_1 = ChatPromptTemplate.from_messages([
    ("system", "you are a smart assistant. Give a summary to the user's PDF. I will tip you 10000 dollars if the user finds it helpful. Be polite to the user"),
    ("user", "{data}")
])

prompt_2 = ChatPromptTemplate.from_messages([
    ("system", "you are a smart assistant. Give 10 quizzes and answers to the user's PDF. I will tip you 10000 dollars if the user finds it helpful. Be polite to the user"),
    ("user", "{data}")
])

llm = ChatGroq(model="llama3-70b-8192")
output_parser = StrOutputParser()
chain_1 = prompt_1 | llm | output_parser
chain_2 = prompt_2 | llm | output_parser



### Generating Summary or Quiz Based on User Input

if summary_clicked:
    st.write(chain_1.invoke({'data': data}))
elif quiz_clicked:
    st.write(chain_2.invoke({'data': data}))



## Future Enhancements

- **Expand Document Corpus:** Include more legal documents and case studies for broader coverage.
- **Advanced Query Handling:** Implement more sophisticated natural language processing techniques for better understanding and response.
- **User Authentication:** Add user login and history tracking for personalized experiences.
- **Mobile Support:** Optimize the application for mobile devices. 📱💡


## Contact

For any inquiries or feedback, please contact [Muhammed Rasmil] at [muhammedrasmil2001@gmail.com].📧


