# In VSCode on Coder
# Make sure you are in the right directory. Paths are with respect to the directory where you are. 
# Check your directory with `pwd` in the terminal

# Run streamlit server with `uv run streamlit run streamlit.py`; usually automatically opens the website in the browser
# CTRL + C to stop the server

# If this is not working, use the "PORTS" tab in VScode  (CTRL+shit+P, then type "Ports" and select "Focus on ports view") 
# to forward the port to localhost and view it your local browser 

# OR use preview browser in VScode


# (1) Tutorial use `st.markdown`` to add the following markdown text
markdown = """


### Material Musings

Material musings begin, where properties convene, from sturdy steel to plastics keen, a world of substances, a vibrant scene. From rigid structures, strong and boldly built, to flexible forms with elastic guilt, each material plays a role, with properties that make it whole. 

| Material | Expected Properties | Actual Properties (according to a sleep-deprived student) |
|---|---|---|
| Steel | Strong, durable, high tensile strength |  Made of tiny robots holding hands, occasionally they let go (hence fatigue) |
| Rubber | Elastic, flexible, insulating |  A solidified version of that goo they use to prank people, but less sticky |
| Glass | Transparent, brittle, amorphous |  Frozen air that sometimes forgets it's solid and shatters dramatically |
| Polymers | Long chains of molecules, versatile |  Those things that tangle up in your drawer and somehow multiply overnight |

""" 

# (2) See the API documentation at https://docs.streamlit.io/develop/api-reference
# Add a code block `st.code` with the following code:
code = """
with st.sidebar:
    st.title("Settings")
    st.write("Choose your options here")
    option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
    st.write(f"You selected {option}")
"""

# (3) Add a sidebar; use the code from above

# (4) Add a button that says "Say hello" and prints "Why hello there" when clicked

# (5) Add a slide bar with a range from 0 to 100 that value is printed when the button is clicked

# (6) Add a line_chart of the `data = np.random.randn(100, 1)`

# (7) Add two tab using `intro, me = st.tabs(["🥦 Intro", "🍔 About me"])`
# Move the current code in the intro tab by adding `with intro:` before the code
# Add the some information about yourself in the "About me" tab using `with me:`

import streamlit as st
from transformers import pipeline
import numpy as np
import pandas as pd
from autogluon.tabular import TabularPredictor
import os

# Dont use GPUS 
os.environ['CUDA_VISIBLE_DEVICES'] = ''

# model_path = f"your path to the model"
# predictor = TabularPredictor.load(model_path)

def main():
    st.title("Hello 🍩👀")
       

if __name__ == '__main__':
    main()
