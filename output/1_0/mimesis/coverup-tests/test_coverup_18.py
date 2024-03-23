# file mimesis/random.py:134-143
# lines [134, 141, 142, 143]
# branches ['141->142', '141->143']

import pytest
from mimesis.random import get_random_item
from enum import Enum
from random import Random

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

@pytest.fixture
def custom_random():
    return Random(0)

def test_get_random_item_with_custom_random(custom_random):
    # Test with custom random object
    random_item = get_random_item(Color, custom_random)
    assert random_item in Color

def test_get_random_item_with_default_random():
    # Test with default random object
    random_item = get_random_item(Color)
    assert random_item in Color
