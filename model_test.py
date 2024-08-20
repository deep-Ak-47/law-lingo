# from flask import Flask, request, jsonify
import streamlit as st
from langchain import PromptTemplate, HuggingFacePipeline

from langchain.schema import HumanMessage,SystemMessage,AIMessage
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import streamlit as st

model_name = "phi-2-mental-jsr"
model_id = f"viber1/{model_name}"
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Configure quantization
quantization_config = BitsAndBytesConfig(
    activation=8,  # 8-bit quantization for activations
    weight=8,      # 8-bit quantization for weights
    bias=None      # No quantization for biases
)

model_8bit = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", quantization_config=quantization_config)


# def user_input(user_question,tokenizer,model_8bit):
#
#
#     # Tokenize the input text
#     input_ids = tokenizer(user_question, return_tensors="pt").input_ids
#
#         # Generate translations
#     max_new_tokens = 100
#
#     outputs = model_8bit.generate(input_ids, max_new_tokens=max_new_tokens)
#
#         # Decode the generated output and return as response
#     translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     response_data = {'translated_text': translated_text}
#
#     st.write("Repluy",response_data["output"])
    




# def main():
#     # st.set_page_config("phi 2 model")
#     # st.header("chat with ph2-jsr-model")
#
#     model_name = "phi-2-mental-jsr"
#     model_id = f"viber1/{model_name}"
#     tokenizer = AutoTokenizer.from_pretrained(model_id)
#
#     # Configure quantization
#     quantization_config = BitsAndBytesConfig(
#         activation=8,  # 8-bit quantization for activations
#         weight=8,  # 8-bit quantization for weights
#         bias=None  # No quantization for biases
#     )
#
#     model_8bit = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto",
#                                                       quantization_config=quantization_config)
#
#     st.set_page_config("phi 2 model")
#     st.header("chat with ph2-jsr-model")
#
#     user_question = st.text_input("ask a question from the phi2 ")
#     if user_question:
#         user_input(user_question,tokenizer,model_8bit)

# app = Flask(__name__)
#
# # Load the model and tokenizer
#
#
#
# @app.route('/translate', methods=['POST'])
# def translate_text():
#     # Get the text to be translated from the request
#     data = request.get_json()
#     text = data['text']
#
#     # Tokenize the input text
#     input_ids = tokenizer(text, return_tensors="pt").input_ids
#
#     # Generate translations
#     max_new_tokens = 50
#     outputs = model_8bit.generate(input_ids, max_new_tokens=max_new_tokens)
#
#     # Decode the generated output and return as response
#     translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     response_data = {'translated_text': translated_text}
#     print(response_data)
#
#     return jsonify({'translated_text': translated_text})
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

text ="hi"

    # Tokenize the input text
input_ids = tokenizer(text, return_tensors="pt").input_ids

    # Generate translations
max_new_tokens = 100

outputs = model_8bit.generate(input_ids, max_new_tokens=max_new_tokens)

    # Decode the generated output and return as response
translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
response_data = {'translated_text': translated_text}

print(response_data)
# if __name__ == "__main__":
#     main()