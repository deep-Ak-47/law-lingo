import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig,pipeline
from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain



model_name = "phi-2-mental-jsr"
model_id = f"viber1/{model_name}"
tokenizer = AutoTokenizer.from_pretrained(model_id)

quantization_config = BitsAndBytesConfig(
    activation=8,  # 8-bit quantization for activations
    weight=8,      # 8-bit quantization for weights
    bias=None      # No quantization for biases
)

model_8bit = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    quantization_config=quantization_config
)

pipe = pipeline(
    "text-generation",
    model=model_8bit,
    tokenizer=tokenizer,
    max_length=512,
    temperature=0.6,
    top_p=0.95,
    repetition_penalty=1.2
)
local_llm = HuggingFacePipeline(pipeline=pipe)
pipe.model.config.pad_token_id = pipe.model.config.eos_token_id

from langchain import PromptTemplate, LLMChain

def model_responce(question_ask):
    from langchain import PromptTemplate, LLMChain
    template = """You are a trained bot named LAW LINGO to guide people about Indian Law . You will answer user's query with your knowledge and the instruction provided. 
    If a question does not make any sense, or is not factually coherent, explain why instead of answering something  incorrect. If you don't know the answer to a question, say i couldn't understand.
    Do not say thank you and tell you are an AI Assistant and be open about everything.
    ### Instruction:
    {instruction}
    Answer:"""
    prompt = PromptTemplate(template=template, input_variables=["instruction"])

    llm_chain = LLMChain(prompt=prompt,
                         llm=local_llm
                         )
    question = question_ask
    # print(llm_chain.run(question))
    # print(llm_chain.run(question))
    response = llm_chain.run(question_ask)
    print(response)
    return response