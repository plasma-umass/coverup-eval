# file: string_utils/generation.py:41-60
# asked: {"lines": [41, 53, 54, 56, 57, 58, 60], "branches": [[53, 54], [53, 56]]}
# gained: {"lines": [41, 53, 54, 56, 57, 58, 60], "branches": [[53, 54], [53, 56]]}

import pytest
import string
import random
from string_utils.generation import random_string

def test_random_string_valid_size(monkeypatch):
    # Mock random.choice to return a predictable sequence
    mock_choices = iter('abc123')
    monkeypatch.setattr(random, 'choice', lambda x: next(mock_choices))
    
    result = random_string(6)
    assert result == 'abc123'
    assert len(result) == 6

def test_random_string_invalid_size_type():
    with pytest.raises(ValueError, match='size must be >= 1'):
        random_string('a')

def test_random_string_size_less_than_one():
    with pytest.raises(ValueError, match='size must be >= 1'):
        random_string(0)

def test_random_string_size_one(monkeypatch):
    # Mock random.choice to return a predictable character
    monkeypatch.setattr(random, 'choice', lambda x: 'a')
    
    result = random_string(1)
    assert result == 'a'
    assert len(result) == 1

def test_random_string_large_size(monkeypatch):
    # Mock random.choice to return a predictable sequence
    mock_choices = iter('abc123' * 100)
    monkeypatch.setattr(random, 'choice', lambda x: next(mock_choices))
    
    result = random_string(600)
    assert result == 'abc123' * 100
    assert len(result) == 600
