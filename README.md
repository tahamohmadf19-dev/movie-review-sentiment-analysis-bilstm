# IMDB Sentiment Analysis with a Bidirectional LSTM

A Keras notebook that classifies IMDB movie reviews as positive or negative, using text preprocessing
that keeps negation words and a Bidirectional LSTM.

**Status:** learning project. The notebook code has been corrected but **has not been re-run**, so it has
no saved results. An earlier version of this README reported about 88% accuracy. That figure had no saved
evidence and came from code that fitted the tokenizer on all data, so treat it as unverified.

## What the notebook does

1. Loads the [IMDB 50K reviews dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) through `kagglehub`.
2. Cleans text, tokenizes it, and removes stopwords while keeping negation words such as "not".
3. Splits data 70/15/15, stratified, with a fixed seed.
4. Fits the tokenizer on training text only, then pads sequences to 200 tokens.
5. Trains Embedding, Bidirectional LSTM (64 units), Dropout and a sigmoid output, with early stopping.
6. Reports a classification report, a confusion matrix and training curves.

## Corrected

The tokenizer used to be fitted on the full dataset before splitting, which let test vocabulary leak into
training. The README also claimed "no train-test contamination". The split now comes first, and
`tests/test_notebook.py` guards this order.

## Setup

```bash
git clone https://github.com/tahamohmadf19-dev/movie-review-sentiment-analysis-bilstm.git
cd movie-review-sentiment-analysis-bilstm
pip install -r requirements.txt
pip install pytest
python -m pytest
jupyter notebook imdb_sentiment_analysis_bilstm.ipynb
```

The tests are static and do not train the model. Training on a CPU can take a long time.

## Next steps

- Run the notebook from a clean state and commit the outputs.
- Compare against a TF-IDF and logistic regression baseline.

## License

MIT. See [LICENSE](LICENSE).
