import numpy as np
import tensorflow_datasets as tfds
import tensorflow as tf
tfds.disable_progress_bar()
import matplotlib.pyplot as plt
import os
import sys
import math
from tensorflow.keras.layers import TextVectorization
import subprocess
from tqdm import tqdm
import transformers
import torch
import data
import logging
import ipfshttpclient
from transformers import pipeline, BertConfig, BertLMHeadModel, AutoModelForCausalLM, BertForSequenceClassification, BertTokenizer, BertModel, T5Tokenizer, T5ForConditionalGeneration, GPT2LMHeadModel, AutoTokenizer, AutoModelForCausalLM, GPT2Tokenizer, LineByLineTextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments


def start_conversation():
    print("Athena Version 0.0.1")
    print("Copyright 2023 Banbury Enterprises")
    print("All Rights Reserved")
    print(" ")
    prompt = input("How may I help you?: ")
    return prompt


def continue_conversation():
    prompt = input("How may I help you?: ")
    return prompt


def load_model():
    

    # load the default text classification pipeline
    text_classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

    # add BART-large-mnli model to the pipeline
    text_classifier.model.config.model_name_or_path = "facebook/bart-large-mnli"
    text_classifier.model = text_classifier.model.from_pretrained(
    text_classifier.model.config.model_name_or_path
    )
    


    return text_classifier


def render_response(prompt, text_classifier):
    sequence_to_classify = prompt
    candidate_labels = ['summarization', 'coding', 'conversational', 'translation', 'question-answering']
    results = text_classifier(sequence_to_classify, candidate_labels)
    max_score = 0
    max_label = None
    response = results['labels'][0]
            
   
    return response



def main():
    logging.disable(logging.CRITICAL)
    # Start a conversation with the user
    prompt = start_conversation()

    # Load the pre-trained model and tokenizer
    text_classifier = load_model()

    # Continue the conversation until the user ends it
    while True:
        if prompt == "go to exploration mode":
            subprocess.run(['python', 'Artificial_Intelligence\exploration_mode.py'])
        else:
            response = render_response(prompt, text_classifier)
            print("This prompt is most likely about " + response)
            if response == "summarization":
                print("Initiating summarization")
            elif response == "coding":
                print("Initiating coding")
            elif response == "conversational":
                print("Initiating conversational")
            elif response == "translation":
                print("Initiating translation")
            elif response == "question-answering":
                print("Initiating question-answering")
        prompt = continue_conversation()


if __name__ == "__main__":
    main()