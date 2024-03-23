# file cookiecutter/repository.py:31-46
# lines [31, 37, 38, 42, 43, 44, 46]
# branches ['37->38', '37->42', '43->44', '43->46']

import pytest
from cookiecutter.repository import expand_abbreviations

def test_expand_abbreviations_with_exact_match():
    abbreviations = {'gh': 'https://github.com/{0}'}
    template = 'gh'
    expected = 'https://github.com/{0}'
    assert expand_abbreviations(template, abbreviations) == expected

def test_expand_abbreviations_with_prefix_match():
    abbreviations = {'gh': 'https://github.com/{0}'}
    template = 'gh:username/repo'
    expected = 'https://github.com/username/repo'
    assert expand_abbreviations(template, abbreviations) == expected

def test_expand_abbreviations_without_match():
    abbreviations = {'gh': 'https://github.com/{0}'}
    template = 'bitbucket:username/repo'
    expected = 'bitbucket:username/repo'
    assert expand_abbreviations(template, abbreviations) == expected
