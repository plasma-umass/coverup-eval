# file mimesis/random.py:107-131
# lines [107, 108, 121, 122, 124, 125, 127, 128, 129, 131]
# branches ['121->122', '121->124', '124->125', '124->127']

import pytest
from mimesis.random import Random
from unittest.mock import patch
import string
import secrets

@pytest.fixture
def random_instance():
    return Random()

def test_randstr_unique(random_instance):
    unique_str = random_instance.randstr(unique=True)
    assert len(unique_str) == 32
    assert all(c in string.hexdigits for c in unique_str)

def test_randstr_length(random_instance):
    length = 50
    random_str = random_instance.randstr(length=length)
    assert len(random_str) == length
    assert all(c in string.ascii_letters + string.digits for c in random_str)

def test_randstr_no_length(random_instance):
    with patch.object(Random, 'randint', return_value=20) as mock_randint:
        random_str = random_instance.randstr()
        assert len(random_str) == 20
        assert all(c in string.ascii_letters + string.digits for c in random_str)
        mock_randint.assert_called_once_with(16, 128)

def test_randstr_default(random_instance):
    random_str = random_instance.randstr()
    assert 16 <= len(random_str) <= 128
    assert all(c in string.ascii_letters + string.digits for c in random_str)
