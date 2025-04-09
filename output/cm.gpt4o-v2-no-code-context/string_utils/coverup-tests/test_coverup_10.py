# file: string_utils/generation.py:41-60
# asked: {"lines": [41, 53, 54, 56, 57, 58, 60], "branches": [[53, 54], [53, 56]]}
# gained: {"lines": [41, 53, 54, 56, 57, 58, 60], "branches": [[53, 54], [53, 56]]}

import pytest
import string
import random
from string_utils.generation import random_string

def test_random_string_valid_size(monkeypatch):
    size = 10
    chars = string.ascii_letters + string.digits

    def mock_choice(seq):
        return 'a'  # predictable output for testing

    monkeypatch.setattr(random, 'choice', mock_choice)
    result = random_string(size)
    assert result == 'a' * size
    assert len(result) == size

def test_random_string_invalid_size_type():
    with pytest.raises(ValueError, match='size must be >= 1'):
        random_string('10')

def test_random_string_invalid_size_value():
    with pytest.raises(ValueError, match='size must be >= 1'):
        random_string(0)

def test_random_string_negative_size():
    with pytest.raises(ValueError, match='size must be >= 1'):
        random_string(-5)
