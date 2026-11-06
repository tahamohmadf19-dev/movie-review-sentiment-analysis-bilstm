"""Static checks on the notebook. These do not train the model."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NB = json.loads((ROOT / "imdb_sentiment_analysis_bilstm.ipynb").read_text(encoding="utf-8"))
CODE = ["".join(c["source"]) for c in NB["cells"] if c["cell_type"] == "code"]


def _first(needle):
    return next(i for i, source in enumerate(CODE) if needle in source)


def test_split_happens_before_tokenizer_fit():
    assert _first("train_test_split(") <= _first("fit_on_texts")


def test_tokenizer_is_fitted_on_training_text_only():
    fit_lines = [line for source in CODE for line in source.splitlines() if "fit_on_texts" in line]
    assert fit_lines == ["tokenizer.fit_on_texts(texts_train)"]


def test_all_code_cells_compile():
    for source in CODE:
        lines = [line for line in source.splitlines() if not line.lstrip().startswith(("!", "%"))]
        compile("\n".join(lines), "cell", "exec")


def test_no_template_placeholders():
    for path in (ROOT / "README.md", ROOT / "imdb_sentiment_analysis_bilstm.ipynb"):
        text = path.read_text(encoding="utf-8")
        assert "yourusername" not in text and "your.email" not in text
