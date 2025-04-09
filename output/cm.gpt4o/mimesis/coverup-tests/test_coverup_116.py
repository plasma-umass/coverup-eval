# file mimesis/providers/person.py:27-29
# lines [27, 28]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def person_provider():
    return Person()

def test_person_provider_initialization(person_provider):
    assert isinstance(person_provider, Person)

def test_person_provider_methods(person_provider):
    # Assuming Person class has methods like full_name, age, etc.
    full_name = person_provider.full_name()
    assert isinstance(full_name, str)
    assert len(full_name) > 0

    age = person_provider.age()
    assert isinstance(age, int)
    assert 0 <= age <= 120

def test_person_provider_with_generic():
    generic = Generic()
    person = generic.person
    assert isinstance(person, Person)

    full_name = person.full_name()
    assert isinstance(full_name, str)
    assert len(full_name) > 0

    age = person.age()
    assert isinstance(age, int)
    assert 0 <= age <= 120
