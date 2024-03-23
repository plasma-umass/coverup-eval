# file mimesis/providers/person.py:74-85
# lines [74, 83, 84, 85]
# branches []

import pytest
from mimesis.enums import Gender
from mimesis.providers.person import Person
from mimesis.exceptions import NonEnumerableError

@pytest.fixture
def person():
    return Person()

def test_name_with_gender(person):
    male_name = person.name(gender=Gender.MALE)
    assert male_name in person._data['names']['male']

    female_name = person.name(gender=Gender.FEMALE)
    assert female_name in person._data['names']['female']

def test_name_without_gender(person):
    name = person.name()
    assert name in person._data['names']['male'] or name in person._data['names']['female']

def test_name_with_invalid_gender(person):
    with pytest.raises(NonEnumerableError):
        person.name(gender="not_a_gender")
