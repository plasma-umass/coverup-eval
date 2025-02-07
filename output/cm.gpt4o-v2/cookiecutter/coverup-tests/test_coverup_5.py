# file: cookiecutter/repository.py:31-46
# asked: {"lines": [31, 37, 38, 42, 43, 44, 46], "branches": [[37, 38], [37, 42], [43, 44], [43, 46]]}
# gained: {"lines": [31, 37, 38, 42, 43, 44, 46], "branches": [[37, 38], [37, 42], [43, 44], [43, 46]]}

import pytest

from cookiecutter.repository import expand_abbreviations

def test_expand_abbreviations_direct_match():
    abbreviations = {
        'py': 'python',
        'js': 'javascript'
    }
    template = 'py'
    result = expand_abbreviations(template, abbreviations)
    assert result == 'python'

def test_expand_abbreviations_with_colon():
    abbreviations = {
        'gh': 'github.com/{0}',
        'bb': 'bitbucket.org/{0}'
    }
    template = 'gh:myrepo'
    result = expand_abbreviations(template, abbreviations)
    assert result == 'github.com/myrepo'

def test_expand_abbreviations_no_match():
    abbreviations = {
        'gh': 'github.com/{0}',
        'bb': 'bitbucket.org/{0}'
    }
    template = 'gl:myrepo'
    result = expand_abbreviations(template, abbreviations)
    assert result == 'gl:myrepo'
