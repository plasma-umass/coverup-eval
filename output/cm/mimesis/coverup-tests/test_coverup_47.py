# file mimesis/random.py:107-131
# lines [107, 108, 121, 122, 124, 125, 127, 128, 129, 131]
# branches ['121->122', '121->124', '124->125', '124->127']

import pytest
from mimesis.random import Random
from unittest.mock import patch
import string
import secrets

def test_randstr_unique():
    random_instance = Random()
    result = random_instance.randstr(unique=True)
    assert len(result) == 32  # UUID4 hex length is 32
    assert all(c in string.hexdigits for c in result)

def test_randstr_with_length():
    random_instance = Random()
    length = 20
    result = random_instance.randstr(length=length)
    assert len(result) == length
    assert all(c in string.ascii_letters + string.digits for c in result)

def test_randstr_without_length():
    random_instance = Random()
    with patch.object(random_instance, 'randint', return_value=50) as mock_randint:
        result = random_instance.randstr()
        mock_randint.assert_called_once_with(16, 128)
        assert len(result) == 50
        assert all(c in string.ascii_letters + string.digits for c in result)

def test_randstr_length_none_unique_false():
    random_instance = Random()
    with patch.object(random_instance, 'randint', return_value=16):
        with patch('secrets.choice', side_effect=lambda x: 'a'):
            result = random_instance.randstr(unique=False, length=None)
            assert result == 'a' * 16  # Default minimum length

@pytest.fixture
def mock_secrets_choice():
    with patch('secrets.choice', side_effect=lambda x: 'a') as mock:
        yield mock

def test_randstr_random_length(mock_secrets_choice):
    random_instance = Random()
    with patch.object(random_instance, 'randint', return_value=16):
        result = random_instance.randstr()
        assert len(result) == 16
        assert all(c == 'a' for c in result)
        assert mock_secrets_choice.call_count == len(result)
