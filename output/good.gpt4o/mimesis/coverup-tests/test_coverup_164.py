# file mimesis/random.py:56-63
# lines [63]
# branches []

import pytest
from mimesis.random import Random

@pytest.fixture
def random_instance():
    return Random()

def test_generate_string(random_instance):
    str_seq = 'abc'
    length = 5
    result = random_instance.generate_string(str_seq, length)
    
    assert len(result) == length
    assert all(char in str_seq for char in result)

def test_generate_string_empty_sequence(random_instance):
    str_seq = ''
    length = 5
    with pytest.raises(IndexError):
        random_instance.generate_string(str_seq, length)
