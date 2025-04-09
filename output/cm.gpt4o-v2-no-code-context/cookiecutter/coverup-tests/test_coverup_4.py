# file: cookiecutter/repository.py:31-46
# asked: {"lines": [31, 37, 38, 42, 43, 44, 46], "branches": [[37, 38], [37, 42], [43, 44], [43, 46]]}
# gained: {"lines": [31, 37, 38, 42, 43, 44, 46], "branches": [[37, 38], [37, 42], [43, 44], [43, 46]]}

import pytest

from cookiecutter.repository import expand_abbreviations

def test_expand_abbreviations_direct_match():
    template = "example"
    abbreviations = {"example": "expanded_example"}
    result = expand_abbreviations(template, abbreviations)
    assert result == "expanded_example"

def test_expand_abbreviations_with_colon_match():
    template = "prefix:rest"
    abbreviations = {"prefix": "expanded_{0}"}
    result = expand_abbreviations(template, abbreviations)
    assert result == "expanded_rest"

def test_expand_abbreviations_no_match():
    template = "no_match"
    abbreviations = {"example": "expanded_example"}
    result = expand_abbreviations(template, abbreviations)
    assert result == "no_match"

def test_expand_abbreviations_with_colon_no_match():
    template = "prefix:rest"
    abbreviations = {"example": "expanded_example"}
    result = expand_abbreviations(template, abbreviations)
    assert result == "prefix:rest"
