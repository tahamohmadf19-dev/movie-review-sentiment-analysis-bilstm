# 🎬 IMDB Sentiment Analysis using Bidirectional LSTM

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-2.x-red.svg)](https://keras.io/)
[![Kaggle](https://img.shields.io/badge/Kaggle-Dataset-20BEFF.svg)](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A deep learning project implementing a **Bidirectional LSTM (BiLSTM)** model for sentiment analysis on the IMDB movie reviews dataset, achieving **88% accuracy** on the test set.

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Dataset](#-dataset)
- [Model Architecture](#-model-architecture)
- [Results](#-results)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Methodology](#-methodology)
- [Limitations & Future Work](#-limitations--future-work)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 🎯 Project Overview

This project demonstrates the application of **Natural Language Processing (NLP)** and **Deep Learning** techniques to classify movie reviews as either positive or negative. The implementation showcases:

- Advanced text preprocessing with negation preservation
- Bidirectional LSTM architecture for contextual understanding
- Early stopping mechanism to prevent overfitting
- Comprehensive evaluation using multiple metrics

### Why Bidirectional LSTM?

Bidirectional LSTMs process sequences in both forward and backward directions, allowing the model to capture context from both past and future tokens. This is particularly valuable for sentiment analysis where:
- **Context matters**: "not good" vs "good"
- **Long-term dependencies**: Understanding sentiment across longer reviews
- **Negation handling**: Correctly interpreting negative phrases

---

## ✨ Key Features

- **🧹 Advanced Text Preprocessing**
  - HTML tag removal
  - Lowercasing and punctuation removal
  - Smart stopword removal (preserves negation words like "not", "never", "no")
  
- **🧠 Sophisticated Model Architecture**
  - Embedding layer (128 dimensions)
  - Bidirectional LSTM (64 units)
  - Dropout regularization (50%)
  - Binary classification output

- **📊 Robust Evaluation**
  - Classification report with precision, recall, F1-score
  - Confusion matrix visualization
  - Training/validation curves

- **🔮 Prediction Pipeline**
  - Complete preprocessing pipeline
  - Ready-to-use prediction function
  - Support for custom review inputs

---

## 📊 Dataset

**Source**: [IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

| Property | Value |
|----------|-------|
| Total Reviews | 50,000 |
| Positive Reviews | 25,000 (50%) |
| Negative Reviews | 25,000 (50%) |
| Average Review Length | ~230 words |
| Training Set | 35,000 (70%) |
| Validation Set | 7,500 (15%) |
| Test Set | 7,500 (15%) |

**Dataset Characteristics**:
- Balanced classes (no class imbalance)
- Real user-generated content
- Wide variety of writing styles and vocabulary
- Includes HTML tags and special characters (cleaned during preprocessing)

---

## 🧠 Model Architecture

```
Model: "BiLSTM_Sentiment_Classifier"
_________________________________________________________________
Layer (type)                Output Shape              Param #   
=================================================================
embedding                   (None, 200, 128)          1,280,000 
bidirectional (LSTM)        (None, 128)               98,816    
dropout                     (None, 128)               0         
dense (sigmoid)             (None, 1)                 129       
=================================================================
Total params: 1,378,945
Trainable params: 1,378,945
Non-trainable params: 0
_________________________________________________________________
```

### Layer Details

| Layer | Configuration | Purpose |
|-------|--------------|---------|
| **Embedding** | vocab=10,000, dim=128 | Converts word indices to dense vectors |
| **Bidirectional LSTM** | units=64 (×2 directions) | Captures context from both directions |
| **Dropout** | rate=0.5 | Prevents overfitting |
| **Dense** | units=1, activation='sigmoid' | Binary classification output |

### Hyperparameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Vocabulary Size | 10,000 | Covers 95%+ of word occurrences |
| Max Sequence Length | 200 | Balances context vs computation |
| Embedding Dimension | 128 | Rich representation without overfitting |
| LSTM Units | 64 | Sufficient capacity for task |
| Dropout Rate | 0.5 | Prevents overfitting |
| Batch Size | 64 | Optimal for GPU utilization |
| Optimizer | Adam | Adaptive learning rate |
| Loss Function | Binary Crossentropy | Standard for binary classification |

---

## 📈 Results

### Performance Metrics

| Metric | Negative Class | Positive Class | Overall |
|--------|---------------|----------------|---------|
| **Precision** | 0.87 | 0.89 | 0.88 |
| **Recall** | 0.89 | 0.87 | 0.88 |
| **F1-Score** | 0.88 | 0.88 | 0.88 |
| **Accuracy** | - | - | **88%** |

### Confusion Matrix

```
                Predicted
              Negative  Positive
Actual Negative  3307      415
       Positive   491     3287
```

**Interpretation**:
- **True Negatives (3307)**: Correctly identified negative reviews
- **False Positives (415)**: Negative reviews incorrectly classified as positive
- **False Negatives (491)**: Positive reviews incorrectly classified as negative
- **True Positives (3287)**: Correctly identified positive reviews

### Key Achievements

✅ **Balanced Performance**: Similar precision/recall for both classes  
✅ **High Accuracy**: 88% on unseen test data  
✅ **Low False Positive Rate**: Only 11% of negative reviews misclassified  
✅ **Low False Negative Rate**: Only 13% of positive reviews misclassified  
✅ **No Overfitting**: Validation accuracy closely tracks training accuracy  

---

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) CUDA-enabled GPU for faster training

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/imdb-sentiment-analysis-bilstm.git
cd imdb-sentiment-analysis-bilstm
```

2. **Create virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download NLTK data**
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

## 🚀 Usage

### Running the Notebook

1. **Launch Jupyter Notebook**
```bash
jupyter notebook imdb_sentiment_analysis_bilstm.ipynb
```

2. **Run all cells** or execute step-by-step

### Using Google Colab

1. Upload the notebook to Google Drive
2. Open with Google Colab
3. Enable GPU: `Runtime` → `Change runtime type` → `GPU`
4. Run all cells

### Making Predictions

```python
# Load the trained model and preprocessing pipeline
from tensorflow.keras.models import load_model

# Example prediction
sample_review = "This movie was absolutely amazing! Best film I've seen this year."
prediction = predict_sentiment(sample_review)
print(prediction)
# Output: Positive (94.32% confidence)
```

---

## 📁 Project Structure

```
imdb-sentiment-analysis-bilstm/
│
├── imdb_sentiment_analysis_bilstm.ipynb  # Main Jupyter notebook
├── requirements.txt                       # Python dependencies
├── README.md                              # Project documentation
├── LICENSE                                # MIT License
├── .gitignore                            # Git ignore rules
│
├── docs/                                  # Additional documentation
│   ├── METHODOLOGY.md                    # Detailed methodology
│   └── RESULTS_ANALYSIS.md               # In-depth results analysis
│
└── models/                                # (Optional) Saved models
    └── bilstm_sentiment_model.h5         # Trained model weights
```

---

## 🔬 Methodology

### 1. Data Preprocessing Pipeline

```
Raw Text → Cleaning → Tokenization → Stopword Removal → Numerical Encoding → Padding
```

**Step-by-Step**:

1. **Text Cleaning**
   - Convert to lowercase
   - Remove HTML tags (`<br />`, etc.)
   - Remove punctuation and special characters
   - Remove extra whitespace

2. **Word Tokenization**
   - Split text into individual words using NLTK

3. **Stopword Removal**
   - Remove common words (the, is, at, etc.)
   - **Preserve negation words** (not, never, no, etc.)
   - Why? "not good" vs "good" have opposite sentiments

4. **Numerical Tokenization**
   - Convert words to integer indices
   - Build vocabulary of 10,000 most frequent words
   - Use `<OOV>` token for unknown words

5. **Sequence Padding**
   - Pad/truncate all sequences to 200 tokens
   - Post-padding (add zeros at the end)
   - Post-truncation (cut from the end if too long)

### 2. Model Training Strategy

- **Optimizer**: Adam (adaptive learning rate)
- **Loss Function**: Binary Crossentropy
- **Early Stopping**: Monitors validation loss with patience=2
- **Epochs**: Maximum 10 (typically stops at 4-5)
- **Batch Size**: 64 samples

### 3. Evaluation Methodology

- **No Train-Test Contamination**: Strict separation of splits
- **Stratified Splitting**: Maintains class distribution
- **Multiple Metrics**: Precision, recall, F1-score, accuracy
- **Confusion Matrix**: Detailed error analysis

---

## 🔍 Limitations & Future Work

### Current Limitations

1. **Binary Classification Only**: Does not handle neutral sentiment
2. **Fixed Vocabulary**: Unknown words are treated as `<OOV>`
3. **No Attention Mechanism**: Cannot highlight important words
4. **Requires GPU**: Training can be slow on CPU
5. **Limited Context Window**: 200 tokens may truncate very long reviews

### Future Improvements

- [ ] **Multi-class Sentiment**: Add neutral, very positive, very negative classes
- [ ] **Attention Mechanism**: Implement attention layers to identify key phrases
- [ ] **Pre-trained Embeddings**: Use GloVe or Word2Vec instead of random initialization
- [ ] **Transfer Learning**: Fine-tune BERT, RoBERTa, or DistilBERT
- [ ] **Ensemble Methods**: Combine BiLSTM with CNN or other architectures
- [ ] **Explainability**: Add LIME or SHAP for model interpretability
- [ ] **Hyperparameter Tuning**: Use Optuna or Keras Tuner
- [ ] **Real-time API**: Deploy as REST API using Flask/FastAPI
- [ ] **Web Interface**: Build Streamlit or Gradio demo

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Areas for Contribution

- Implementing attention mechanisms
- Adding model explainability features
- Creating deployment scripts
- Writing additional documentation
- Optimizing hyperparameters

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Dataset**: Maas et al. (2011) - Learning Word Vectors for Sentiment Analysis
- **Kaggle**: [lakshmi25npathi](https://www.kaggle.com/lakshmi25npathi) for hosting the dataset
- **TensorFlow/Keras**: For the deep learning framework
- **NLTK**: For natural language processing tools
- **Inspiration**: Various NLP and sentiment analysis research papers

---

## 📞 Contact

**Mohmad Taha Jasem Alhmad**  
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

---

## 📊 Project Stats

![GitHub repo size](https://img.shields.io/github/repo-size/yourusername/imdb-sentiment-analysis-bilstm)
![GitHub stars](https://img.shields.io/github/stars/yourusername/imdb-sentiment-analysis-bilstm)
![GitHub forks](https://img.shields.io/github/forks/yourusername/imdb-sentiment-analysis-bilstm)

---

**⭐ If you found this project helpful, please consider giving it a star!**

---

*Last Updated: February 2026*
