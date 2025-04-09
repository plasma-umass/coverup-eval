# file mimesis/random.py:24-31
# lines [24, 25]
# branches []

import pytest
from mimesis.random import Random as MimesisRandom
import random as random_module

def test_random_class_extension():
    class CustomRandom(MimesisRandom):
        def custom_method(self):
            return "custom"

    custom_random = CustomRandom()
    assert isinstance(custom_random, random_module.Random)
    assert custom_random.custom_method() == "custom"
