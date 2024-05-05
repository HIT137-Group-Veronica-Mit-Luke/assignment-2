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
            text_columns = [col for col in df.columns if 'TEXT' in col]
            
            # Check if any text columns are found
            if text_columns:
                text_column = text_columns[0]  # Take the first text column found
                raw_text = ' '.join(df[text_column].tolist())

                # Removing words under 4 characters as they are irrelevant
                clean_text = ' '.join(re.findall(r'\b[a-zA-Z]{4,}\b', raw_text))
        
                text_list.append(clean_text)
            else:
                print(f"No text column found in {filename}")

    with open('cvs_text_file.txt', 'w') as f:
        f.write('\n'.join(text_list))

# Call the function 
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

#Task 4 
#defining functions
import spacy

# Load the spacy model for biomedical NER
nlp_bio = spacy.load("en_ner_bc5cdr_md")

# Define the function to perform named entity recognition (NER)
def perform_ner(text_file):
    try:
        # Process text in chunks to avoid exceeding the maximum limit
        chunk_size = 1000000  # Adjust chunk size as needed
        num_chunks = (len(text_file) + chunk_size - 1) // chunk_size  # Calculate number of chunks

        for i in range(num_chunks):
            start_idx = i * chunk_size
            end_idx = (i + 1) * chunk_size
            chunk_text = text_file[start_idx:end_idx]

            # Process the chunk using the biomedical NER model
            doc_bio = nlp_bio(chunk_text)

            # Perform further processing with the chunk if needed
            # For example, extract entities or perform analysis

    except Exception as e:
        print("An error occurred during named entity recognition:", e)  # Handle exceptions

# Call the function
with open('cvs_text_file.txt', 'r') as file:
    text = file.read()
    perform_ner(text)


# Function to perform named entity recognition (NER)
def perform_ner(text_file):
    try:
       # Load the spacy model for scientific NER
        nlp_sci = spacy.load("en_core_sci_sm")

        # Load the spacy model for biomedical NER
        nlp_bio = spacy.load("en_ner_bc5cdr_md")

        # Process the text using the scientific NER model
        doc_sci = nlp_sci(text_file)

        # Process the text using the biomedical NER model
        doc_bio = nlp_bio(text_file)

        # Extract diseases entities using the scientific NER model
        diseases_sci = [ent.text for ent in doc_sci.ents if ent.label_ == 'DISEASE']

        # Extract drugs entities using the scientific NER model
        drugs_sci = [ent.text for ent in doc_sci.ents if ent.label_ == 'CHEMICAL']

        # Extract diseases entities using the biomedical NER model
        diseases_bio = [ent.text for ent in doc_bio.ents if ent.label_ == 'DISEASE']

        # Extract drugs entities using the biomedical NER model
        drugs_bio = [ent.text for ent in doc_bio.ents if ent.label_ == 'DRUG']

        # Print the statistics for each model
        print("Scientific NER Model:")
        print("Total diseases entities:", len(diseases_sci))
        print("Total drugs entities:", len(drugs_sci))
        print("\nBiomedical NER Model:")
        print("Total diseases entities:", len(diseases_bio))
        print("Total drugs entities:", len(drugs_bio))

        # Compare the differences between the two models
        print("\nDifferences between the two models:")
        print("Total diseases detected by both models:", len(set(diseases_sci) & set(diseases_bio)))
        print("Total drugs detected by both models:", len(set(drugs_sci) & set(drugs_bio)))

        # Check for most common words
        print("\nMost common diseases (scientific NER model):", Counter(diseases_sci).most_common(5))
        print("Most common diseases (biomedical NER model):", Counter(diseases_bio).most_common(5))
        print("Most common drugs (scientific NER model):", Counter(drugs_sci).most_common(5))
        print("Most common drugs (biomedical NER model):", Counter(drugs_bio).most_common(5))
    except Exception as e:
        print("An error occurred during named entity recognition:", e)  # Handle exceptions

if __name__ == "__main__":
    # Define folder path relative to the script's location
    folder_path = os.path.join(os.getcwd(), 'data')


    # Extract text from CSVs
    extract_text_from_csvs(folder_path)

    # Count words
    count_words('cvs_text_file.txt')

    # Count unique tokens
    count_unique_tokens('cvs_text_file.txt')

    # Perform Named Entity Recognition (NER)
    with open('cvs_text_file.txt', 'r') as file:
        text = file.read()
        perform_ner(text)
