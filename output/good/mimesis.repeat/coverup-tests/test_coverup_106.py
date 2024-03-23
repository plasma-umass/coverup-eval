# file mimesis/random.py:24-31
# lines [24, 25]
# branches []

import pytest
from mimesis.random import Random

def test_custom_random_class_methods():
    custom_random = Random()

    # Test if the custom_random instance is indeed an instance of Random
    assert isinstance(custom_random, Random)

    # Test if the custom_random can call the method from the superclass
    random_int = custom_random.randint(0, 10)
    assert 0 <= random_int <= 10

    # Test if the custom_random can call another method from the superclass
    random_float = custom_random.random()
    assert 0.0 <= random_float < 1.0
