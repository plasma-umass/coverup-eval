# file mimesis/random.py:56-63
# lines [56, 63]
# branches []

import pytest
from mimesis.random import Random

def test_generate_string():
    rnd = Random()
    str_seq = 'abcdef'
    length = 5

    result = rnd.generate_string(str_seq, length)
    assert len(result) == length
    assert all(char in str_seq for char in result)
