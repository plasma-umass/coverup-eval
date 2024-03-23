# file mimesis/providers/person.py:48-60
# lines [48, 58, 59, 60]
# branches []

import pytest
from mimesis.providers import Person

@pytest.fixture
def person():
    return Person()

def test_age(person):
    min_age = 16
    max_age = 66
    age = person.age(minimum=min_age, maximum=max_age)
    assert min_age <= age <= max_age
    assert person._store['age'] == age

def test_age_with_custom_range(person):
    min_age = 20
    max_age = 30
    age = person.age(minimum=min_age, maximum=max_age)
    assert min_age <= age <= max_age
    assert person._store['age'] == age

def test_age_with_same_min_max(person):
    fixed_age = 40
    age = person.age(minimum=fixed_age, maximum=fixed_age)
    assert age == fixed_age
    assert person._store['age'] == age
