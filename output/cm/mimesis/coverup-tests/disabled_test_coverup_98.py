# file mimesis/providers/person.py:87-95
# lines [87, 95]
# branches []

import pytest
from mimesis.enums import Gender
from mimesis.providers.person import Person

@pytest.fixture
def person_provider():
    return Person()

def test_first_name_with_gender(person_provider):
    male_first_name = person_provider.first_name(gender=Gender.MALE)
    female_first_name = person_provider.first_name(gender=Gender.FEMALE)

    assert male_first_name != female_first_name  # Assuming male and female names are different

def test_first_name_without_gender(person_provider):
    first_name = person_provider.first_name()
    assert isinstance(first_name, str) and len(first_name) > 0
