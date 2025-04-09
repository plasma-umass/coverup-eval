# file mimesis/providers/person.py:87-95
# lines [87, 95]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis.enums import Gender

@pytest.fixture
def person():
    return Person()

def test_first_name_male(person):
    first_name = person.first_name(Gender.MALE)
    assert isinstance(first_name, str)
    assert first_name != ""

def test_first_name_female(person):
    first_name = person.first_name(Gender.FEMALE)
    assert isinstance(first_name, str)
    assert first_name != ""

def test_first_name_none(person):
    first_name = person.first_name()
    assert isinstance(first_name, str)
    assert first_name != ""
