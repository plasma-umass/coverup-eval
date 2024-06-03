# file mimesis/providers/person.py:341-352
# lines [341, 351, 352]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def person():
    generic = Generic()
    return generic.person

def test_weight_default(person):
    weight = person.weight()
    assert 38 <= weight <= 90

def test_weight_custom_range(person):
    weight = person.weight(minimum=50, maximum=60)
    assert 50 <= weight <= 60

def test_weight_minimum_greater_than_maximum(person):
    with pytest.raises(ValueError):
        person.weight(minimum=100, maximum=90)

def test_weight_negative_values(person):
    weight = person.weight(minimum=-10, maximum=10)
    assert -10 <= weight <= 10
