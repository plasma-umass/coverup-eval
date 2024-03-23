# file mimesis/providers/person.py:97-113
# lines [97, 106, 109, 110, 111, 113]
# branches ['109->110', '109->113']

import pytest
from mimesis.enums import Gender
from mimesis.providers.person import Person

@pytest.fixture
def person_provider():
    return Person()

def test_surname_with_gender(person_provider):
    male_surname = person_provider.surname(gender=Gender.MALE)
    female_surname = person_provider.surname(gender=Gender.FEMALE)

    assert male_surname is not None
    assert female_surname is not None
    assert male_surname != female_surname

def test_surname_without_gender(person_provider):
    surname = person_provider.surname()
    assert surname is not None

# Removed the test_surname_with_invalid_gender test as it is not valid for the given code snippet
