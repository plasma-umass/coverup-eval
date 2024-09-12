# file: cookiecutter/repository.py:31-46
# asked: {"lines": [37, 38, 42, 43, 44, 46], "branches": [[37, 38], [37, 42], [43, 44], [43, 46]]}
# gained: {"lines": [37, 38, 42, 43, 44, 46], "branches": [[37, 38], [37, 42], [43, 44], [43, 46]]}

import pytest

from cookiecutter.repository import expand_abbreviations

def test_expand_abbreviations_direct_match():
    template = "py"
    abbreviations = {"py": "python-template"}
    result = expand_abbreviations(template, abbreviations)
    assert result == "python-template"

def test_expand_abbreviations_with_colon():
    template = "py:flask"
    abbreviations = {"py": "python-template-{0}"}
    result = expand_abbreviations(template, abbreviations)
    assert result == "python-template-flask"

def test_expand_abbreviations_no_match():
    template = "java"
    abbreviations = {"py": "python-template"}
    result = expand_abbreviations(template, abbreviations)
    assert result == "java"

def test_expand_abbreviations_prefix_no_rest():
    template = "py:"
    abbreviations = {"py": "python-template-{0}"}
    result = expand_abbreviations(template, abbreviations)
    assert result == "python-template-"

def test_expand_abbreviations_no_colon():
    template = "python"
    abbreviations = {"py": "python-template"}
    result = expand_abbreviations(template, abbreviations)
    assert result == "python"
