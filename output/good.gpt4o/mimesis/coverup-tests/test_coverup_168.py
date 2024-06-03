# file mimesis/random.py:107-131
# lines [121, 122, 124, 125, 127, 128, 129, 131]
# branches ['121->122', '121->124', '124->125', '124->127']

import pytest
from mimesis.random import Random
import string
import secrets
import uuid

@pytest.fixture
def random_instance():
    return Random()

def test_randstr_unique(random_instance, mocker):
    mocker.patch('uuid.uuid4', return_value=uuid.UUID('12345678123456781234567812345678'))
    result = random_instance.randstr(unique=True)
    assert result == '12345678123456781234567812345678'

def test_randstr_length(random_instance, mocker):
    mocker.patch('mimesis.random.Random.randint', return_value=20)
    result = random_instance.randstr(length=20)
    assert len(result) == 20
    assert all(c in string.ascii_letters + string.digits for c in result)

def test_randstr_default_length(random_instance, mocker):
    mocker.patch('mimesis.random.Random.randint', return_value=16)
    result = random_instance.randstr()
    assert len(result) == 16
    assert all(c in string.ascii_letters + string.digits for c in result)
