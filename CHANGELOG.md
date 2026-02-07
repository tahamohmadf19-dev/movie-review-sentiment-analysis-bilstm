# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-06

### 🎉 Initial Release

#### Added
- **Model Implementation**
  - Bidirectional LSTM architecture for sentiment analysis
  - Embedding layer with 128 dimensions
  - Dropout regularization (50%)
  - Binary classification output with sigmoid activation

- **Data Preprocessing**
  - Text cleaning (HTML tags, punctuation, lowercasing)
  - Word tokenization using NLTK
  - Smart stopword removal with negation preservation
  - Numerical tokenization with 10K vocabulary
  - Sequence padding to 200 tokens

- **Training Pipeline**
  - Adam optimizer with binary crossentropy loss
  - Early stopping callback (patience=2)
  - 70-15-15 train-validation-test split
  - Stratified sampling to maintain class balance

- **Evaluation**
  - Classification report with precision, recall, F1-score
  - Confusion matrix visualization
  - Training/validation curves
  - Custom prediction function for new reviews

- **Documentation**
  - Comprehensive README.md with badges
  - Detailed METHODOLOGY.md explaining technical approach
  - In-depth RESULTS_ANALYSIS.md with error analysis
  - Quick start guide (QUICK_START.md)
  - Contribution guidelines (CONTRIBUTING.md)
  - Project summary (PROJECT_SUMMARY.md)
  - MIT License

- **Project Structure**
  - Clean Jupyter notebook with markdown explanations
  - requirements.txt with all dependencies
  - .gitignore for Python/Data Science projects
  - setup.py for package installation
  - docs/ folder with supplementary documentation

#### Performance
- **Test Accuracy**: 88.08%
- **Precision**: 0.87-0.89 for both classes
- **Recall**: 0.87-0.89 for both classes
- **F1-Score**: 0.88 (balanced)
- **Training Time**: ~5 minutes on GPU
- **Inference Speed**: 1000 reviews/second

#### Highlights
- ✨ Negation-aware preprocessing (critical innovation)
- ✨ Bidirectional context processing
- ✨ Production-ready performance (88% accuracy)
- ✨ Comprehensive documentation
- ✨ Reproducible results with random seeds

---

## [Unreleased]

### Planned Features

#### Version 1.1.0 (Q2 2026)
- [ ] Attention mechanism for interpretability
- [ ] REST API with Flask/FastAPI
- [ ] Streamlit web demo
- [ ] Model versioning with MLflow
- [ ] Docker containerization

#### Version 1.2.0 (Q3 2026)
- [ ] Pre-trained embeddings (GloVe, Word2Vec)
- [ ] Multi-class sentiment (5 classes)
- [ ] Hyperparameter tuning with Optuna
- [ ] Data augmentation techniques
- [ ] Domain adaptation for product reviews

#### Version 2.0.0 (Q4 2026)
- [ ] Transfer learning with BERT/RoBERTa
- [ ] Ensemble methods (BiLSTM + CNN + Transformer)
- [ ] Explainable AI with LIME/SHAP
- [ ] Multilingual support
- [ ] Continuous learning pipeline

---

## Version History

### [1.0.0] - 2026-02-06
- Initial public release
- Core BiLSTM implementation
- 88% accuracy on IMDB dataset
- Comprehensive documentation

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

---

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

**Maintained by**: Mohmad Taha Jasem Alhmad  
**Last Updated**: February 6, 2026
