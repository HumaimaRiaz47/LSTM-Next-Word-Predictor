# 🧠 LSTM Next Word Predictor (CampusX Series)

## 🚀 Overview

This project implements a **Next Word Prediction system** using an LSTM (Long Short-Term Memory) neural network.
It follows a complete NLP pipeline — from problem formulation to deployment — based on the CampusX deep learning series.

The model learns patterns from text data and predicts the most probable next word given an input sequence.

---

## 🎯 Problem Statement

Given a sequence of words, the goal is to **predict the next word** in a meaningful and context-aware way.

Example:
Input:
"I love artificial"

Output:
"intelligence"

This task is fundamental in:

* Language modeling
* Text generation
* Chatbots and conversational AI

---

## 📚 Project Workflow

### 🔹 1. Data Collection & Processing

* Used text dataset (e.g., Hamlet)
* Cleaned and normalized text
* Tokenized words using Keras Tokenizer
* Generated input sequences for training
* Applied padding for equal-length sequences

---

### 🔹 2. LSTM Model Training

* Built a Sequential model with:

  * Embedding layer
  * LSTM layer
  * Dense output layer (Softmax)
* Used categorical crossentropy loss
* Trained on generated sequences

---

### 🔹 3. Prediction System

* Converted input text into token sequences
* Applied padding
* Predicted next word using trained model
* Decoded prediction into readable text

---

### 🔹 4. Streamlit Web App Integration

* Built an interactive UI using Streamlit
* User enters input text
* Model predicts next word in real-time
* Simple and user-friendly interface

---

### 🔹 5. GRU Variant Implementation

* Implemented GRU (Gated Recurrent Unit) as an alternative
* Compared performance with LSTM
* Demonstrated flexibility of RNN architectures

---

## 🛠️ Tech Stack

* Python
* TensorFlow / Keras
* NumPy
* Streamlit

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧠 Model Architecture

* Embedding Layer (word representation)
* LSTM Layer (sequence learning)
* Dense Layer with Softmax (prediction)

---

## 🔁 GRU vs LSTM

* GRU is a simpler and faster variant of LSTM
* Fewer parameters → faster training
* LSTM may capture more complex dependencies

---

## 📊 Future Improvements

* Train on larger datasets (Wikipedia, books)
* Use Transformer-based models (e.g., GPT)
* Add multi-word prediction
* Deploy on cloud (Streamlit Cloud / Hugging Face)

---

## 👩‍💻 Author

Humaima Riaz
