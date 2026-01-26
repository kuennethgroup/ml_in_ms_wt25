
# --- INSTRUCTIONS FOR DEPLOYING AND EDITING THIS APP ---
#
# 1. Open a terminal and make sure you are in the correct directory that contains the deploy_values.py file. Use `pwd` to check your path and `cd <dir>` to navigate.
#
# 2. To start the Streamlit app, run in terminal:
#      uv run streamlit run deploy_values.py
#    Stop the server with CTRL+C, if you like.
#
# 3. Check the "PORTS" tab in VSCode (CTRL+Shift+P → "Focus on ports view")
#    to see if the port Streamlit is running on (default is 8501) is correctly forwarded. Open in your browser by clicking the link.
#
# 4. To build your app:
#    - See the Streamlit API docs: https://docs.streamlit.io/develop/api-reference
#    - Load your AutoGluon model from the first hackathon for inference.
#    - Use `st.text_input`, `st.slider`, etc. to collect user input.
#    - Add a button to trigger prediction: `if st.button("Predict"):`
#    - Display the prediction result on the page.
#    - Make the UI visually appealing and user-friendly.
#
# 5. Edit below this section to implement your app logic.

import streamlit as st
from transformers import pipeline

import pandas as pd
from autogluon.tabular import TabularPredictor
import os

# Dont use GPUS for now
os.environ['CUDA_VISIBLE_DEVICES'] = ''

# model_path = f"your path to the model"
# predictor = TabularPredictor.load(model_path)


def main():
    st.title("My cool ML model predictor 🍩👀")



if __name__ == '__main__':
    main()
