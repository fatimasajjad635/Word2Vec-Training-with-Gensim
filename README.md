This assignment focuses on training Word2Vec models using the Gensim library and analyzing word similarities in the Amazon reviews dataset.

## Overview

In this assignment, you will:

1. Train a Word2Vec model on the Amazon reviews dataset using Gensim
2. Analyze word similarities by finding the 20 most similar words to "good" and "bad"
3. Upload your trained model to the university server
4. Provide analysis and interpretation of the results

## Prerequisites

- Completed Assignment 1 (data preparation)
- Python 3.10+ with gensim, numpy, and pandas installed
- An API key for the model server (same as Assignment 2)

## Step 1: Set Up Your Environment

### Opening in Codespaces

1. Navigate to your assignment repository on GitHub
2. Click the green "Code" button
3. Select the "Codespaces" tab
4. Click "Create codespace on main"

### Install Dependencies

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Get Your Data into Codespaces

Bring your preprocessed data from Assignment 1 into your Codespace:

1. Create a directory named `data` in your Codespace:
   ```bash
   mkdir -p data
   ```
2. Upload your preprocessed CSV files from Assignment 1:
   - `train.csv` or `train_ns.csv` (choose one for training)
   - You can use either the version with or without stopwords

### ⚠️ Important: Data Size Considerations

**The full training set (`train.csv` or `train_ns.csv`) is too large for Codespaces.** You should use a subset for development and testing:

#### Option 1: Create a Subset

Copy and paste one of these commands in the terminal.

```bash
# Create a 100K line subset for faster training and testing
head -100000 data/train.csv > data/train_subset.csv

# Or create different sizes based on your needs:
head -50000 data/train.csv > data/train_small.csv    # 50K lines (~10-15 min training)
head -200000 data/train.csv > data/train_medium.csv  # 200K lines (~30-45 min training)
```

#### Option 2: Use Your Local Machine
If you have a more powerful local machine, you can:
- Download your repository locally
- Train on the full dataset (may take 1-2 hours)
- Upload only the final model to the server

#### Memory and Time Expectations:
- **50K lines**: ~10-15 minutes training, ~100MB model
- **100K lines**: ~20-30 minutes training, ~200MB model  
- **200K lines**: ~30-45 minutes training, ~400MB model
- **640K lines**: ~60-120 minutes training, ~800MB+ model


## Step 3: Set Up the Model Upload Client

```bash
# Download the model upload client
wget https://mse-msci-641.uwaterloo.ca/static/model_upload_client_A3.py

# Initialize with your API key (if not already done)
python model_upload_client_A3.py --init
```

## Step 4: Implement Word2Vec Training

Complete the implementation in `main.py` following these guidelines:

### 1. Data Loading Function (Already Provided)
```python
def load_data(file_path):
    """Load tokenized data from a CSV file"""
    # Implementation already provided
```

### 2. Word2Vec Training Function (Needs Implementation)
```python
def train_word2vec_model(sentences, vector_size=100, window=5, min_count=5, 
                        workers=4, epochs=10, sg=1):
    """Train a Word2Vec model using Gensim"""
    # Your implementation needed
```

**Implementation guidelines:**
- Use `gensim.models.Word2Vec` to create and train the model
- Use skip-gram algorithm (sg=1) as default
- Set reasonable parameters for vector_size (100-300), window (3-5), min_count (5-10)
- Train for sufficient epochs (10-20)

### 3. Similarity Analysis Function (Needs Implementation)
```python
def find_similar_words(model, word, topn=20):
    """Find the most similar words to a given word"""
    # Your implementation needed
```

**Implementation guidelines:**
- Use `model.wv.most_similar()` to find similar words
- Handle cases where the word might not be in vocabulary
- Return results as list of (word, similarity_score) tuples

### 4. Analysis Function (Needs Implementation)
```python
def analyze_word_similarities(model):
    """Analyze similarities for 'good' and 'bad' words"""
    # Your implementation needed
```

**Requirements:**
- Find 20 most similar words to "good"
- Find 20 most similar words to "bad"
- Store results in the specified format

### 5. Main Function (Needs Implementation)
```python
def main():
    """Main execution flow"""
    # Your implementation needed
```

**Implementation steps:**
1. Load training data from the data directory
2. Train Word2Vec model with appropriate parameters
3. Save the trained model as `word2vec_model.model`
4. Analyze similarities for "good" and "bad"
5. Save results to `word_similarities.json`
6. Upload model to server
7. Print summary of findings

## Expected Output Files

Your implementation should generate:

1. **`word2vec_model.model`** - The trained Word2Vec model
2. **`word_similarities.json`** - Analysis results in the following format:
   ```json
   {
     "good_similar": [
       ["excellent", 0.734],
       ["great", 0.712],
       ...
     ],
     "bad_similar": [
       ["terrible", 0.689],
       ["awful", 0.654],
       ...
     ],
     "analysis": {
       "good_words": ["list", "of", "similar", "words"],
       "bad_words": ["list", "of", "similar", "words"]
     }
   }
   ```

3. **`analysis.txt`** - Your written analysis (see Step 5)

## Step 5: Written Analysis

Create a file called `analysis.txt` with your interpretation of the results. **Use the provided `analysis_template.txt` as your starting point** - simply copy it and fill in your results and analysis.

The analysis should address the following questions in 5-6 sentences:

1. Are the words most similar to "good" generally positive in sentiment?
2. Are the words most similar to "bad" generally negative in sentiment?
3. Why do you think this is or isn't the case?
4. What does this tell you about how Word2Vec learns word representations?

**Steps:**
1. Copy `analysis_template.txt` to `analysis.txt`
2. Fill in your name and student ID
3. List the top 10 most similar words for both "good" and "bad" with their similarity scores
4. Write your 5-6 sentence analysis explaining the results

Your analysis should demonstrate understanding of:
- How Word2Vec uses context to learn word meanings
- The difference between semantic similarity and sentiment
- Why Word2Vec might capture sentiment patterns in the data


## Step 6: Upload Your Model

Upload your trained model to the server:

```bash
# Upload the Word2Vec model
python model_upload_client_A3.py --model word2vec_model.model --config word2vec_amazon_reviews
```

## Step 7: Create model_ids.json file

Run the following command to generate the complete `model_ids.json` file:

```bash
# Generate model_ids.json file containing the names of all your uploaded models
python model_upload_client_A3.py --generate-json
```

## Step 8: Submit Your Assignment

Ensure your repository contains:
- `main.py` - Your implementation
- `word_similarities.json` - Similarity analysis results  
- `analysis.txt` - Your written analysis
- `model_ids.json` - Reference to uploaded model

Commit and push:
```bash
git add main.py word_similarities.json analysis.txt model_ids.json
git commit -m "Complete Assignment 3 - Word2Vec"
git push
```

## Model Parameters and Considerations

### Recommended Parameters:
- **vector_size**: 100-300 (dimensionality of word vectors)
- **window**: 3-5 (short sentence window size)
- **min_count**: 5-10 (minimum word frequency threshold)
- **workers**: 4 (number of CPU cores to use)
- **epochs**: 10-20 (number of training iterations)
- **sg**: 1 (use skip-gram algorithm)


## Grading Criteria

- **Model Training (30%)**: Correct implementation of Word2Vec training
- **Similarity Analysis (25%)**: Proper extraction of similar words for "good" and "bad"
- **Code Quality (20%)**: Clean, well-documented implementation
- **Written Analysis (15%)**: Thoughtful interpretation of results
- **Model Upload (10%)**: Successful upload and proper file formats

## Troubleshooting

### Gensim Installation Issues
```bash
# If you encounter issues installing gensim
pip install --upgrade pip
pip install gensim --no-cache-dir
```

### Memory Issues
- Reduce the dataset size for testing
- Increase min_count parameter to filter rare words
- Consider using Google Colab for more memory

### Model Loading Issues
- Ensure you're using `model.save()` and `Word2Vec.load()` correctly
- Check file paths and permissions

### Vocabulary Issues
- If "good" or "bad" aren't in vocabulary, check your min_count parameter
- Verify your preprocessing hasn't removed these words

## Resources

- [Gensim Word2Vec Tutorial](https://radimrehurek.com/gensim/models/word2vec.html)
- [Word2Vec Paper (Mikolov et al.)](https://arxiv.org/abs/1301.3781)
- [Understanding Word2Vec](https://towardsdatascience.com/introduction-to-word-embedding-and-word2vec-652d0c2060fa)
