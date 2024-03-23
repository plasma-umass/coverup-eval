# file mimesis/providers/person.py:341-352
# lines [341, 351, 352]
# branches []

import pytest
from mimesis.providers import Person

@pytest.fixture
def person():
    return Person()

def test_weight_default_range(person):
    weight = person.weight()
    assert 38 <= weight <= 90

def test_weight_custom_range(person):
    min_weight = 50
    max_weight = 100
    weight = person.weight(minimum=min_weight, maximum=max_weight)
    assert min_weight <= weight <= max_weight

def test_weight_invalid_range(person):
    with pytest.raises(ValueError):
        person.weight(minimum=100, maximum=50)
