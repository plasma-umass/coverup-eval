# file mimesis/providers/person.py:328-339
# lines [328, 338, 339]
# branches []

import pytest
from mimesis.providers import Person

@pytest.fixture
def person():
    return Person()

def test_height(person):
    min_height = 1.5
    max_height = 2.0
    height = person.height(minimum=min_height, maximum=max_height)
    height_value = float(height)
    assert min_height <= height_value <= max_height
    assert len(height.split('.')[1]) == 2  # Check if height has two decimal places

def test_height_with_custom_range(person):
    min_height = 1.6
    max_height = 1.9
    height = person.height(minimum=min_height, maximum=max_height)
    height_value = float(height)
    assert min_height <= height_value <= max_height
    assert len(height.split('.')[1]) == 2  # Check if height has two decimal places
