# file mimesis/providers/person.py:48-60
# lines [48, 58, 59, 60]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def person():
    generic = Generic()
    return generic.person

def test_age_within_bounds(person):
    min_age = 16
    max_age = 66
    age = person.age(minimum=min_age, maximum=max_age)
    assert min_age <= age <= max_age

def test_age_custom_bounds(person):
    min_age = 20
    max_age = 30
    age = person.age(minimum=min_age, maximum=max_age)
    assert min_age <= age <= max_age

def test_age_stored(person):
    age = person.age()
    assert person._store['age'] == age
