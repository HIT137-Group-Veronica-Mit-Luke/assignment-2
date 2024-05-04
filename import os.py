import os
import csv
import torch
from collections import Counter
import pandas as pd
from transformers import AutoModel, AutoTokenizer
import spacy
import scispacy
import re


#Question 1 - Task1:  

#extrating text from CSV file! 
def extract_text_from_csvs(folder_path):
    text_list = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            filepath = os.path.join(folder_path, filename)
            df = pd.read_csv(filepath)
            text_column = [col for col in df.columns if 'TEXT' in col][0]
            raw_text = ' '.join(df[text_column].tolist())

            #removing words under 4 characters as they are irrelavant 
            clean_text = ' '.join(re.findall(r'\b[a-zA-Z]{4,}\b', raw_text))
        
            text_list.append(clean_text)

    with open('cvs_text_file.txt', 'w') as f:
        f.write('\n'.join(text_list))


folder_path = r'C:\Users\veron\OneDrive\Desktop\HIT137-Assignment 2-CVS'
extract_text_from_csvs(folder_path)

#Task 3.1 

#Reading in Chunks
def read_text_in_chunks(file_path, window_size=512, overlap=100):
    with open(file_path, 'r') as f:
        long_text = f.read()
        for i in range(0, len(long_text), window_size - overlap):
            chunk = long_text[i:i + window_size]
            yield chunk

file_path = 'cvs_text_file.txt'
text_chunks = read_text_in_chunks('cvs_text_file.txt', window_size=100000, overlap=20000)

#counting top 30 words
def count_words(text_file):
    word_counts = Counter()
    for chunk in read_text_in_chunks(text_file):
        words = chunk.split()
        word_counts.update(words)

    Top_30_Words = word_counts.most_common(30)

    with open('Top_30_Words.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Count'])
        writer.writerows(Top_30_Words)

count_words('cvs_text_file.txt')

#Task 3.2

#Counting unique tokens
def count_unique_tokens(text_file, model_name="dmis-lab/biobert-v1.1"):
    #  BioBERT Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Counter to track unique tokens
    unique_tokens = Counter()

    # Iterate over text chunks using the read_text_in_chunks function
    for chunk in read_text_in_chunks(text_file):
        # Tokenize the chunk using the Auto Tokenizer
        tokens = tokenizer.tokenize(chunk)

        # Update the Counter with the token occurrences
        unique_tokens.update(tokens)

    # Get the top 30 most common tokens
    top_30_tokens = unique_tokens.most_common(30)

    # Write the results to a CSV file
    with open('top_30_tokens.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['Token', 'Count'])
        # Write the top 30 tokens and their counts
        writer.writerows(top_30_tokens)

count_unique_tokens('cvs_text_file.txt')
