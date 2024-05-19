import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline
from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain
from  temp_test import model_responce
import re
from yt_web_link import  serch_link
from pyngrok import ngrok

# ngrok.set_auth_token("2eqrijBHXecwDXZ9RpqJzK81If6_6euaBjSakyRy3jUS6yLs4")
# public_url = ngrok.connect(8502).public_url
# print(public_url)


# Load model and tokenizer


question = st.text_input("You:", "")

if st.button("Ask"):
    # Generate response
    answer_r = model_responce(question)
    answer_match = re.search(r'Answer:(.*)', answer_r, re.DOTALL)
    if answer_match:
        answer = answer_match.group(1).strip()

    end_index = answer.index('"""')

    # Extract the substring before the end_index
    answer_strip = answer[:end_index].strip()
    st.text_area("Bot:", value= answer_strip)

    ytlink,web_link = serch_link(question)
    st.text_area("youtube link",value= ytlink)
    st.text_area("web link", value=web_link)


