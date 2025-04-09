# file: cookiecutter/repository.py:31-46
# asked: {"lines": [31, 37, 38, 42, 43, 44, 46], "branches": [[37, 38], [37, 42], [43, 44], [43, 46]]}
# gained: {"lines": [31, 37, 38, 42, 43, 44, 46], "branches": [[37, 38], [37, 42], [43, 44], [43, 46]]}

import pytest

from cookiecutter.repository import expand_abbreviations

def test_expand_abbreviations_direct_match():
    abbreviations = {'py': 'python'}
    template = 'py'
    result = expand_abbreviations(template, abbreviations)
    assert result == 'python'

def test_expand_abbreviations_with_colon():
    abbreviations = {'gh': 'github.com/{}'}
    template = 'gh:cookiecutter/cookiecutter'
    result = expand_abbreviations(template, abbreviations)
    assert result == 'github.com/cookiecutter/cookiecutter'

def test_expand_abbreviations_no_match():
    abbreviations = {'py': 'python'}
    template = 'java'
    result = expand_abbreviations(template, abbreviations)
    assert result == 'java'

def test_expand_abbreviations_prefix_match():
    abbreviations = {'gh': 'github.com/{}'}
    template = 'gh:cookiecutter'
    result = expand_abbreviations(template, abbreviations)
    assert result == 'github.com/cookiecutter'
