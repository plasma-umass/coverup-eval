# file mimesis/providers/person.py:74-85
# lines [74, 83, 84, 85]
# branches []

import pytest
from mimesis.enums import Gender
from mimesis.providers.person import Person
from mimesis.exceptions import NonEnumerableError

@pytest.fixture
def person_provider():
    return Person()

def test_name_with_gender(person_provider):
    male_name = person_provider.name(gender=Gender.MALE)
    female_name = person_provider.name(gender=Gender.FEMALE)

    assert male_name in person_provider._data['names']['male']
    assert female_name in person_provider._data['names']['female']

def test_name_without_gender(person_provider):
    name = person_provider.name()
    all_names = person_provider._data['names']['male'] + person_provider._data['names']['female']

    assert name in all_names

def test_name_with_invalid_gender(person_provider):
    with pytest.raises(NonEnumerableError):
        person_provider.name(gender="invalid_gender")
