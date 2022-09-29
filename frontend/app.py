import streamlit as st
import requests
import json

def run():
    st.title("SMS Text Spam Classifier")
    input = st.text_input("Enter your text here:")
    data = {"text":input}
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    if st.button("Predict"):
        response = requests.post("https://text-spam-classifier-09.herokuapp.com/predict", data = json.dumps(data), headers = headers)
        # response = requests.post("http://127.0.0.1:8000/predict", data = json.dumps(data), headers = headers) # for local testing
        if response.status_code == 200:
            st.success(f"The text you entered is: {response.text}")
        else:
            print(response.raise_for_status)
if __name__ == '__main__':
    run()