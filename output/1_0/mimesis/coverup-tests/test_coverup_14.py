# file mimesis/random.py:107-131
# lines [107, 108, 121, 122, 124, 125, 127, 128, 129, 131]
# branches ['121->122', '121->124', '124->125', '124->127']

import pytest
from mimesis.random import Random
import random as random_module
import uuid
from unittest.mock import patch

@pytest.fixture
def random_instance():
    return Random()

def test_randstr_unique(random_instance):
    result = random_instance.randstr(unique=True)
    assert isinstance(result, str)
    assert len(result) == 32  # UUID4 hex length is 32

def test_randstr_with_length(random_instance):
    length = 20
    result = random_instance.randstr(length=length)
    assert isinstance(result, str)
    assert len(result) == length

def test_randstr_without_length(random_instance):
    with patch.object(random_module.Random, 'randint', return_value=50):
        result = random_instance.randstr()
        assert isinstance(result, str)
        assert len(result) == 50
