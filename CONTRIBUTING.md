# Contributing to IMDB Sentiment Analysis

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)

---

## Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code:

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on what is best for the community
- Show empathy towards other community members

---

## How Can I Contribute?

### 1. Reporting Bugs

If you find a bug, please create an issue with:

- **Clear title**: Describe the bug in one sentence
- **Description**: Detailed explanation of the problem
- **Steps to reproduce**: How to trigger the bug
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**: OS, Python version, library versions
- **Screenshots**: If applicable

**Example**:
```
Title: Model fails to load with TensorFlow 2.15

Description: When loading the saved model with TensorFlow 2.15, 
I get a compatibility error.

Steps to Reproduce:
1. Install TensorFlow 2.15
2. Run: model = load_model('bilstm_model.h5')
3. Error appears

Expected: Model loads successfully
Actual: ValueError about incompatible layer types

Environment:
- OS: Ubuntu 22.04
- Python: 3.10
- TensorFlow: 2.15.0
```

### 2. Suggesting Enhancements

Have an idea for improvement? Open an issue with:

- **Feature description**: What you want to add
- **Use case**: Why it's useful
- **Proposed implementation**: How it could work (optional)
- **Alternatives considered**: Other approaches

**Example**:
```
Title: Add attention mechanism to model

Description: Implement attention layers to improve model 
interpretability and potentially boost accuracy.

Use Case: Users want to see which words influenced the prediction.

Proposed Implementation:
- Add Attention layer after BiLSTM
- Visualize attention weights
- Compare performance with baseline

Alternatives:
- Integrated Gradients for post-hoc explainability
- LIME for model-agnostic interpretation
```

### 3. Contributing Code

Areas where contributions are welcome:

#### High Priority
- [ ] Implement attention mechanism
- [ ] Add LIME/SHAP explainability
- [ ] Create REST API with Flask/FastAPI
- [ ] Build Streamlit demo app

#### Medium Priority
- [ ] Experiment with pre-trained embeddings (GloVe)
- [ ] Add hyperparameter tuning with Optuna
- [ ] Implement data augmentation
- [ ] Create Docker container

#### Low Priority
- [ ] Add more visualization functions
- [ ] Write additional unit tests
- [ ] Improve documentation
- [ ] Translate README to other languages

### 4. Improving Documentation

Documentation improvements are always welcome:

- Fix typos and grammar
- Add examples and tutorials
- Clarify confusing sections
- Translate to other languages
- Add diagrams and visualizations

---

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/imdb-sentiment-analysis-bilstm.git
cd imdb-sentiment-analysis-bilstm
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install project dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8 mypy jupyter
```

### 4. Create a Branch

```bash
# Create a new branch for your feature
git checkout -b feature/your-feature-name

# Or for bug fixes:
git checkout -b fix/bug-description
```

---

## Pull Request Process

### 1. Before Submitting

- [ ] Code follows the project's style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] No unnecessary files are included

### 2. Commit Message Format

Use clear and descriptive commit messages:

```
type(scope): Brief description

Detailed explanation of what changed and why.

Fixes #123
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples**:
```
feat(model): Add attention mechanism to BiLSTM

Implemented attention layer after BiLSTM to improve interpretability.
Achieved 89.5% accuracy (up from 88%).

Fixes #42
```

```
docs(readme): Add installation instructions for Windows

Added specific steps for Windows users including path setup
and common troubleshooting tips.
```

### 3. Pull Request Template

```markdown
## Description
Brief description of your changes

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## How Has This Been Tested?
Describe the tests you ran to verify your changes

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
```

### 4. Review Process

1. Maintainer will review your PR within 3-5 days
2. Address any feedback or requested changes
3. Once approved, maintainer will merge your PR
4. Your contribution will be acknowledged in the next release

---

## Coding Standards

### Python Style Guide

Follow [PEP 8](https://pep8.org/) style guide:

```python
# Good
def predict_sentiment(review_text):
    """
    Predict sentiment of a movie review.
    
    Args:
        review_text (str): Raw review text
        
    Returns:
        str: Predicted sentiment (Positive/Negative)
    """
    cleaned = preprocess(review_text)
    prediction = model.predict(cleaned)
    return "Positive" if prediction > 0.5 else "Negative"


# Bad
def predictSentiment(reviewText):
    cleaned=preprocess(reviewText)
    pred=model.predict(cleaned)
    return "Positive" if pred>0.5 else "Negative"
```

### Code Formatting

Use `black` for automatic formatting:

```bash
# Format all Python files
black .

# Check without modifying
black --check .
```

### Linting

Use `flake8` to check code quality:

```bash
# Run linter
flake8 .

# With specific configuration
flake8 --max-line-length=100 --ignore=E203,W503 .
```

### Type Hints

Add type hints for better code clarity:

```python
from typing import List, Tuple, Optional

def preprocess_text(text: str) -> List[int]:
    """Convert text to sequence of integers."""
    pass

def train_model(
    X_train: np.ndarray,
    y_train: np.ndarray,
    epochs: int = 10
) -> Tuple[tf.keras.Model, dict]:
    """Train BiLSTM model and return model + history."""
    pass
```

---

## Testing Guidelines

### Unit Tests

Write tests for new functions:

```python
# tests/test_preprocessing.py
import pytest
from src.preprocessing import clean_text, tokenize

def test_clean_text():
    """Test text cleaning function."""
    input_text = "This is a <br> TEST!"
    expected = "this is a test"
    assert clean_text(input_text) == expected

def test_tokenize_empty_string():
    """Test tokenization with empty string."""
    assert tokenize("") == []

def test_tokenize_negation_preserved():
    """Test that negation words are preserved."""
    tokens = tokenize("not good")
    assert "not" in tokens
    assert "good" in tokens
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_preprocessing.py

# Run with verbose output
pytest -v
```

### Integration Tests

Test the complete pipeline:

```python
def test_end_to_end_prediction():
    """Test complete prediction pipeline."""
    review = "This movie was amazing!"
    prediction = predict_sentiment(review)
    assert prediction in ["Positive", "Negative"]
    assert isinstance(prediction, str)
```

---

## Code Review Checklist

Before submitting your PR, ensure:

- [ ] **Functionality**: Code works as intended
- [ ] **Tests**: All tests pass
- [ ] **Documentation**: Updated if necessary
- [ ] **Code Quality**: Follows style guide
- [ ] **Performance**: No unnecessary performance degradation
- [ ] **Security**: No security vulnerabilities
- [ ] **Compatibility**: Works with specified Python versions
- [ ] **Dependencies**: No unnecessary dependencies added

---

## Communication

### Where to Ask Questions?

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For general questions and ideas
- **Pull Request Comments**: For code-specific questions

### Response Time

- Bug reports: 1-3 days
- Feature requests: 3-7 days
- Pull requests: 3-5 days

---

## Recognition

Contributors will be acknowledged in:

- README.md (Contributors section)
- Release notes
- Project changelog

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## Questions?

If you have questions not covered here, feel free to:

- Open an issue with the "question" label
- Start a discussion on GitHub Discussions

Thank you for contributing! 🎉

---

**Maintainer**: Mohmad Taha Jasem Alhmad  
**Last Updated**: February 2026
