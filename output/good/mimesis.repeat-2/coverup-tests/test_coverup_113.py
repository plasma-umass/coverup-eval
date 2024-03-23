# file mimesis/providers/person.py:115-123
# lines [115, 123]
# branches []

import pytest
from mimesis.enums import Gender
from mimesis.providers.person import Person

@pytest.fixture
def person_provider():
    return Person()

def test_last_name_with_gender(person_provider):
    last_name_male = person_provider.last_name(gender=Gender.MALE)
    last_name_female = person_provider.last_name(gender=Gender.FEMALE)
    assert isinstance(last_name_male, str)
    assert isinstance(last_name_female, str)

def test_last_name_without_gender(person_provider):
    last_name = person_provider.last_name()
    assert isinstance(last_name, str)
