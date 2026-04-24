import streamlit as st
import numpy as np
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model
model = tf.keras.models.load_model("hamlet_text_generator.h5")

# Load tokenizer
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Max sequence length (same as training)
max_len = 56  # or use your len_max

# Title
st.title("🎭 Shakespeare Text Generator")

# Input
input_text = st.text_input("Enter a starting sentence:")

num_words = st.slider("Number of words to generate", 1, 20, 5)

# Generate function
def generate_text(seed_text, num_words):
    text = seed_text

    for _ in range(num_words):
        token_text = tokenizer.texts_to_sequences([text])[0]

        padded = pad_sequences([token_text], maxlen=max_len, padding='pre')

        preds = model.predict(padded, verbose=0)
        predicted_index = np.argmax(preds)

        # find word
        for word, index in tokenizer.word_index.items():
            if index == predicted_index:
                text += " " + word
                break

    return text

# Button
if st.button("Generate"):
    result = generate_text(input_text, num_words)
    st.success(result)