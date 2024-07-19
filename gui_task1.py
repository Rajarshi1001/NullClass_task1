# import libraries
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from keras.layers import TextVectorization
import re
import requests
# import tensorflow.strings as tf_strings
import json
import string
from keras.models import load_model
from tensorflow import argmax
from keras.preprocessing.text import tokenizer_from_json
from keras.utils import pad_sequences
import numpy as np
import tensorflow as tf

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

## loading the tokenizers

model = load_model('english_to_french_lstm_model')

#load Tokenizer
with open('english_tokenizer.json') as f:
    data = json.load(f)
    english_tokenizer = tokenizer_from_json(data)
    
with open('french_tokenizer.json') as f:
    data = json.load(f)
    french_tokenizer = tokenizer_from_json(data)
    
    
with open('sequence_length.json') as f:
    max_length = json.load(f)
    
def pad(x, length=None):
    return pad_sequences(x, maxlen=length, padding='post')

def translate_to_french(english_sentence):
    english_sentence = english_sentence.lower()
    
    english_sentence = english_sentence.replace(".", '')
    english_sentence = english_sentence.replace("?", '')
    english_sentence = english_sentence.replace("!", '')
    english_sentence = english_sentence.replace(",", '')
    
    english_sentence = english_tokenizer.texts_to_sequences([english_sentence])
    english_sentence = pad(english_sentence, max_length)
    
    english_sentence = english_sentence.reshape((-1,max_length))
    
    french_sentence = model.predict(english_sentence)[0]
    
    french_sentence = [np.argmax(word) for word in french_sentence]

    french_sentence = french_tokenizer.sequences_to_texts([french_sentence])[0]
    
    print("French translation: ", french_sentence)
    
    return french_sentence

def solve():
    input_text = input_entry.get()
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        'client': 'gtx',
        'sl': 'en',  
        'tl': 'fr',  
        'dt': 't',
        'q': input_text  
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        translation = response.json()[0][0][0]
        translated_sent = f"French: {translation}"
    except Exception as e:
        translated_sent = f"Error: {e}"
    
    result_label.config(text=translated_sent)
    

root = tk.Tk()
root.title("Language Translator")
root.geometry("500x300")

font = ('Helvetica', 14)

input_entry = tk.Entry(root, width=80, font=font)
input_entry.pack(pady=10)

instruction_label = tk.Label(root, text="Enter sentence for English to French translation", wraplength=400, font=font)
instruction_label.pack(pady=10)

translate_button = tk.Button(root, text="Translate", command=solve, font=font)
translate_button.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=400, font=font)
result_label.pack(pady=20)

root.mainloop()

