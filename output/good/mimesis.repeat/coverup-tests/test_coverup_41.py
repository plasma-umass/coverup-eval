# file mimesis/providers/person.py:48-60
# lines [48, 58, 59, 60]
# branches []

import pytest
from mimesis.providers import Person
from mimesis import Generic

@pytest.fixture
def person():
    return Person()

def test_age(person):
    min_age = 18
    max_age = 30
    age = person.age(minimum=min_age, maximum=max_age)
    assert min_age <= age <= max_age
    assert person._store['age'] == age

def test_age_with_invalid_range(person):
    with pytest.raises(ValueError):
        person.age(minimum=70, maximum=65)
