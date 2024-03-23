# file mimesis/random.py:56-63
# lines [56, 63]
# branches []

import pytest
from mimesis.random import Random

def test_generate_string():
    random_instance = Random()
    str_seq = "abc123"
    length = 5

    result = random_instance.generate_string(str_seq, length)
    assert len(result) == length
    assert all(char in str_seq for char in result)

def test_generate_string_default_length():
    random_instance = Random()
    str_seq = "xyz789"

    result = random_instance.generate_string(str_seq)
    assert len(result) == 10
    assert all(char in str_seq for char in result)
