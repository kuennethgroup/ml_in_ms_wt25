# In VSCode on Coder
# Make sure you are in the right directory. Paths are with respect to the directory where you are. 
# Check your directory with `pwd` in the terminal

# Run streamlit server with `uv run streamlit run streamlit.py`; usually automatically opens the website in the browser
# CTRL + C to stop the server

# If this is not working, use the "PORTS" tab in VScode  (CTRL+shit+P, then type "Ports" and select "Focus on ports view") 
# to forward the port to localhost and view it your local browser 

# OR use preview browser in VScode


#### Follow this

# (1) See the API documentation at https://docs.streamlit.io/develop/api-reference
# Add `st.file_uploader` to gather the necessary inputs / files for your model

# (2) Create a button to trigger model inference: `if st.button("Predict"):`

# (3) Write the file the uploaded file as tmp file using
# ```
# with tempfile.NamedTemporaryFile(suffix='.jpg') as tmp:
#            tmp.write(input_file.getvalue())
#```

# (4) Print the results of the prediction on the website
# Load your AutoGluon model from the first hackathon 

# (5) Make the website look nice


import streamlit as st
from transformers import pipeline
import tempfile
import pandas as pd
from autogluon.multimodal import MultiModalPredictor
import os

# Dont use GPUS
os.environ['CUDA_VISIBLE_DEVICES'] = ''

# model_path = f"your file"
# predictor = MultiModalPredictor.load(model_path)

def main():
    st.title("My cool ML model predictor 🍩👀")


if __name__ == '__main__':
    main()



