"""
Setup script for IMDB Sentiment Analysis BiLSTM package.
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="imdb-sentiment-bilstm",
    version="1.0.0",
    author="Mohmad Taha Jasem Alhmad",
    author_email="your.email@example.com",
    description="Bidirectional LSTM model for IMDB sentiment analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/imdb-sentiment-analysis-bilstm",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
        "visualization": [
            "matplotlib>=3.7.0",
            "seaborn>=0.12.0",
        ],
    },
    keywords="sentiment-analysis nlp deep-learning lstm tensorflow imdb",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/imdb-sentiment-analysis-bilstm/issues",
        "Source": "https://github.com/yourusername/imdb-sentiment-analysis-bilstm",
        "Documentation": "https://github.com/yourusername/imdb-sentiment-analysis-bilstm/blob/main/README.md",
    },
)
