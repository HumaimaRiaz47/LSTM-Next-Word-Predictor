import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


# load the lstm model
load_model('hamlet_text_generator.h5')

# load the tokenizer
with open('token')