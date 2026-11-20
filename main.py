 #!/usr/bin/env python3
"""
MSE 641 Assignment 3: Word2Vec Training with Gensim
-----------------------------------------
Author: Fatima Sajjad
Student ID: Your ID
"""

import os
import json
import numpy as np
import pandas as pd
from gensim.models import Word2Vec
from gensim.models.phrases import Phrases, Phraser

def load_data(file_path):
    """Load tokenized data from a CSV file
    
    Args:
        file_path: Path to the CSV file containing tokenized sentences
        
    Returns:
        List of lists, where each inner list is a tokenized sentence
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        # Each line contains comma-separated tokens
        data = [line.strip().split(',') for line in f if line.strip()]
    return data

def train_word2vec_model(sentences, vector_size=100, window=5, min_count=5, 
                        workers=4, epochs=10, sg=1):
    """Train a Word2Vec model using Gensim
    
    Args:
        sentences: List of tokenized sentences
        vector_size: Dimensionality of word vectors
        window: Maximum distance between current and predicted word
        min_count: Ignores words with total frequency lower than this
        workers: Number of worker threads
        epochs: Number of training epochs
        sg: Training algorithm (1 for skip-gram, 0 for CBOW)
        
    Returns:
        Trained Word2Vec model
        
    Implementation steps:
    1. Initialize a Word2Vec model with the specified parameters
    2. Build the vocabulary from the sentences
    3. Train the model on the sentences for the specified number of epochs
    4. Return the trained model
    """
    model = Word2Vec(
        vector_size=vector_size,
        window=window,
        min_count=min_count,
        workers=workers,
        sg=sg
    )
    model.build_vocab(sentences)

    model.train(sentences, total_examples=len(sentences), epochs=epochs)
    
    return model
   
def find_similar_words(model, word, topn=20):
    """Find the most similar words to a given word
    
    Args:
        model: Trained Word2Vec model
        word: Target word to find similarities for
        topn: Number of most similar words to return
        
    Returns:
        List of tuples (word, similarity_score) sorted by similarity
        
    Implementation steps:
    1. Check if the word exists in the model's vocabulary
    2. If it exists, use the model to find the most similar words
    3. Return the results as a list of (word, score) tuples
    4. If the word doesn't exist, return an empty list or handle appropriately
    """
    try:
        return model.wv.most_similar(word, topn=topn)
    except KeyError:
       
        return []

def save_model(model, filepath):
    """Save the trained Word2Vec model to disk
    
    Args:
        model: Trained Word2Vec model
        filepath: Path where to save the model
        
    Implementation steps:
    1. Use Gensim's save method to save the model to the specified filepath
    """
def save_model(model, filepath):
    model.save(filepath)

def load_model(filepath):
    """Load a Word2Vec model from disk
    
    Args:
        filepath: Path to the saved model
        
    Returns:
        Loaded Word2Vec model
        
    Implementation steps:
    1. Use Gensim's Word2Vec.load method to load the model from the filepath
    2. Return the loaded model
    """
from gensim.models import Word2Vec

def load_model(filepath):
    return Word2Vec.load(filepath)

def analyze_word_similarities(model):
    """Analyze similarities for 'good' and 'bad' words
    
    Args:
        model: Trained Word2Vec model
        
    Returns:
        Dictionary containing analysis results
        
    Implementation steps:
    1. Find 20 most similar words to "good"
    2. Find 20 most similar words to "bad"
    3. Store results in a structured format
    4. Return the results dictionary
    """
    results = {
        'good_similar': [],
        'bad_similar': [],
        'analysis': {
            'good_words': [],
            'bad_words': []
        }
    }

    try:
        results['good_similar'] = model.wv.most_similar('good', topn=20)
        results['analysis']['good_words'] = [word for word, _ in results['good_similar']]
    except KeyError:
        results['good_similar'] = []
        results['analysis']['good_words'] = []

    try:
        results['bad_similar'] = model.wv.most_similar('bad', topn=20)
        results['analysis']['bad_words'] = [word for word, _ in results['bad_similar']]
    except KeyError:
        results['bad_similar'] = []
        results['analysis']['bad_words'] = []

    return results

def save_results(results, filepath='word_similarities.json'):
    """Save analysis results to a JSON file
    
    Args:
        results: Dictionary containing analysis results
        filepath: Path to save the results
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

def main():
    """Main function to train Word2Vec model and analyze word similarities
    
    Implementation steps:
    1. Load the training data from the data directory
    2. Train a Word2Vec model on the loaded data
    3. Save the trained model
    4. Analyze similarities for 'good' and 'bad'
    5. Save the analysis results
    6. Print summary statistics about the model and findings
    """
    # TODO: Implement the main function
    # See README.md for detailed instructions
    
    # Expected data files (from Assignment 1):
    # - data/train.csv or data/train_ns.csv (tokenized training data)
    # - You can choose which preprocessed version to use
    
    print("Starting Word2Vec training...")
    
def main():
    data_path = "data/train_subset.csv"
    model_path = "word2vec_model.model"
    json_path = "word_similarities.json"

    print("Starting Word2Vec training...")

    sentences = load_data(data_path)
    model = train_word2vec_model(sentences)
    save_model(model, model_path)

    analysis_results = analyze_word_similarities(model)

    with open(json_path, "w", encoding="utf-8") as f:
        formatted_results = {
            "good_similar": [list(pair) for pair in analysis_results["good_similar"]],
            "bad_similar": [list(pair) for pair in analysis_results["bad_similar"]],
            "analysis": analysis_results["analysis"]
        }
        json.dump(formatted_results, f, indent=4)

    print("\nTop 5 similar words to 'good':")
    for word, score in analysis_results["good_similar"][:5]:
        print(f"{word}: {score:.4f}")

    print("\nTop 5 similar words to 'bad':")
    for word, score in analysis_results["bad_similar"][:5]:
        print(f"{word}: {score:.4f}")
if __name__ == "__main__":
    main()
