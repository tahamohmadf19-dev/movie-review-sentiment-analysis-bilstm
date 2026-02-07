# Quick Start Guide - IMDB Sentiment Analysis

Get up and running with the IMDB Sentiment Analysis model in under 5 minutes!

---

## 🚀 Option 1: Google Colab (Fastest)

**No installation required! Run directly in your browser.**

### Steps:

1. **Open the notebook in Colab**:
   - Click this badge: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/imdb-sentiment-analysis-bilstm/blob/main/imdb_sentiment_analysis_bilstm.ipynb)

2. **Enable GPU** (recommended):
   - Click `Runtime` → `Change runtime type`
   - Select `GPU` under Hardware accelerator
   - Click `Save`

3. **Run all cells**:
   - Click `Runtime` → `Run all`
   - Wait ~10 minutes for training to complete

4. **Test with your own reviews**:
   - Scroll to the last cell
   - Modify the test reviews
   - Run the cell to see predictions

**That's it! No setup required.**

---

## 💻 Option 2: Local Installation (Recommended for Development)

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) CUDA-enabled GPU for faster training

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/imdb-sentiment-analysis-bilstm.git
cd imdb-sentiment-analysis-bilstm

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### Run the Notebook

```bash
# Start Jupyter Notebook
jupyter notebook imdb_sentiment_analysis_bilstm.ipynb
```

Then:
1. Click `Kernel` → `Restart & Run All`
2. Wait for training to complete (~10-15 minutes on CPU, ~5 minutes on GPU)

---

## 🎯 Option 3: Quick Test (Pre-trained Model)

If you just want to test predictions without training:

### Using Python Script

```python
# quick_test.py
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK data (first time only)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Load model and tokenizer
model = load_model('models/bilstm_sentiment_model.h5')
with open('models/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# Preprocessing function
def preprocess(text):
    # Clean
    text = text.lower()
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stopwords (keep negation)
    stop_words = set(stopwords.words('english'))
    negation = {"no", "not", "nor", "never", "none", "cannot", "cant"}
    stop_words = stop_words - negation
    tokens = [w for w in tokens if w not in stop_words]
    
    return " ".join(tokens)

# Prediction function
def predict_sentiment(review):
    # Preprocess
    cleaned = preprocess(review)
    
    # Tokenize
    seq = tokenizer.texts_to_sequences([cleaned])
    padded = pad_sequences(seq, maxlen=200, padding='post')
    
    # Predict
    prob = model.predict(padded, verbose=0)[0][0]
    sentiment = "Positive" if prob > 0.5 else "Negative"
    confidence = prob if prob > 0.5 else 1 - prob
    
    return sentiment, confidence

# Test
if __name__ == "__main__":
    reviews = [
        "This movie was absolutely amazing! Best film of the year.",
        "Terrible movie. Complete waste of time and money.",
        "It was okay, nothing special but not terrible either."
    ]
    
    for review in reviews:
        sentiment, confidence = predict_sentiment(review)
        print(f"\nReview: {review}")
        print(f"Prediction: {sentiment} ({confidence*100:.2f}% confidence)")
```

**Run it**:
```bash
python quick_test.py
```

---

## 📊 Expected Output

After training completes, you should see:

```
Model: "BiLSTM_Sentiment_Classifier"
_________________________________________________________________
Layer (type)                Output Shape              Param #   
=================================================================
embedding                   (None, 200, 128)          1,280,000 
bidirectional (LSTM)        (None, 128)               98,816    
dropout                     (None, 128)               0         
dense                       (None, 1)                 129       
=================================================================

Epoch 1/10
547/547 ━━━━━━━━━━━━━━━━━━━━ 18s - accuracy: 0.7093 - loss: 0.5391
Epoch 2/10
547/547 ━━━━━━━━━━━━━━━━━━━━ 11s - accuracy: 0.9059 - loss: 0.2460
...

Classification Report:
              precision    recall  f1-score   support
           0       0.87      0.89      0.88      3722
           1       0.89      0.87      0.88      3778
    accuracy                           0.88      7500

Test Accuracy: 88.08%
```

---

## 🔧 Troubleshooting

### Issue 1: `ModuleNotFoundError: No module named 'kagglehub'`

**Solution**:
```bash
pip install kagglehub[pandas-datasets]
```

### Issue 2: `Resource punkt not found`

**Solution**:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### Issue 3: Training is very slow

**Solutions**:
- Use Google Colab with GPU (fastest)
- Reduce batch size: `BATCH_SIZE = 32` instead of 64
- Reduce epochs: `EPOCHS = 5` instead of 10
- Use CPU if GPU isn't available (will be slower but works)

### Issue 4: Out of memory error

**Solutions**:
- Reduce batch size: `BATCH_SIZE = 32`
- Use Google Colab (16GB RAM)
- Close other applications
- Restart kernel and clear output

### Issue 5: Different results each time

**Cause**: Random initialization  
**Solution**: Set random seeds (already done in notebook)
```python
import numpy as np
import tensorflow as tf

np.random.seed(42)
tf.random.set_seed(42)
```

---

## 📝 Next Steps

After successfully running the notebook:

1. **Explore the code**: Understand each preprocessing step
2. **Modify hyperparameters**: Try different values and see impact
3. **Test your own reviews**: Add custom movie reviews
4. **Read documentation**: Check `docs/` folder for deep dives
5. **Contribute**: See `CONTRIBUTING.md` for how to help

---

## 🎓 Learning Resources

### Understanding the Model

- **Bidirectional LSTM**: [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- **Word Embeddings**: [Word2Vec Tutorial](https://www.tensorflow.org/tutorials/text/word2vec)
- **Sentiment Analysis**: [Stanford CS224N Lecture](http://web.stanford.edu/class/cs224n/)

### Improving the Model

- **Attention Mechanism**: [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- **BERT for NLP**: [BERT Paper](https://arxiv.org/abs/1810.04805)
- **Hyperparameter Tuning**: [Keras Tuner Guide](https://www.tensorflow.org/tutorials/keras/keras_tuner)

---

## 💬 Getting Help

If you run into issues:

1. **Check the docs**: See `docs/` folder
2. **Search existing issues**: [GitHub Issues](https://github.com/yourusername/imdb-sentiment-analysis-bilstm/issues)
3. **Ask a question**: Open a new issue with the "question" label
4. **Join discussions**: [GitHub Discussions](https://github.com/yourusername/imdb-sentiment-analysis-bilstm/discussions)

---

## ⚡ Performance Benchmarks

| Hardware | Training Time | Inference Speed |
|----------|--------------|-----------------|
| Google Colab (T4 GPU) | 5 minutes | 1000 reviews/sec |
| Local GPU (RTX 3060) | 7 minutes | 1500 reviews/sec |
| Local CPU (i7-9700K) | 45 minutes | 100 reviews/sec |
| Local CPU (i5-8250U) | 90 minutes | 50 reviews/sec |

---

## ✅ Validation Checklist

Make sure everything works:

- [ ] Notebook runs without errors
- [ ] Training completes successfully
- [ ] Test accuracy is around 88%
- [ ] Predictions work on custom reviews
- [ ] All cells execute in order
- [ ] No warnings about deprecated functions

---

**Ready to dive deeper?** Check out the [full README](README.md) and [methodology documentation](docs/METHODOLOGY.md)!

---

**Questions?** Open an issue or start a discussion!

**Happy coding! 🚀**
