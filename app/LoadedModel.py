from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import re
import os

"""
DOCS:

class LoadedModel
constructor parameters: model_path,tokenizer_path,max_seq_len:

    model_path: Keras model's path saved as model.save()
    tokenizer_path: serialized Tokenizer object's path 
    max_seq_len: padding value model has trained.

function predict_answer(answer):

    parameters:
        answer: answer text given which will be evaluated.
    
    this function cleans, tokenizes and applies padding to the answer string given.
    then it uses sequence formed and predicts the probability of the answer being true.

"""

class LoadedModel():

    def __init__(self,model_path,tokenizer_path,max_seq_len):
        if os.path.exists(model_path):
            self.model = keras.models.load_model(model_path)
        else:
            raise FileNotFoundError("Model path not found")
            
        if os.path.exists(tokenizer_path):
            self.tokenizer = pickle.load(open(tokenizer_path,mode="rb"))
        else:
            raise FileNotFoundError("Tokenizer object pickle not found")

        # This is the general regular expressions pattern that clean the text from
        # the redundant characters.
        self.PATTERN = "[^a-zA-Z0-9ıüğşçöİĞÜŞÇÖ]"

        # This is the maximum length for padding, which is 53 for the first prototype.
        self.MAXLEN = max_seq_len

    def predict_answer(self,answer):

        cleaned_answer = re.sub(self.PATTERN," ",str(answer))
        tokenized_answer = self.tokenizer.texts_to_sequences([answer.lower()])
        padded_answer = pad_sequences(tokenized_answer,self.MAXLEN)

        result = self.model.predict(padded_answer)[0]
        rounded_result = round(float(result) * 100,1)
        return {
            "answer":answer,
            "result":rounded_result
        }
    


