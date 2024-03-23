# file mimesis/providers/person.py:27-29
# lines [27, 28]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis.enums import Gender

@pytest.fixture
def person():
    return Person()

def test_person_full_name(person):
    # Test that the full_name method covers both genders
    male_full_name = person.full_name(gender=Gender.MALE)
    female_full_name = person.full_name(gender=Gender.FEMALE)

    assert male_full_name != female_full_name  # Ensure names are different
    assert isinstance(male_full_name, str)  # Ensure the name is a string
    assert isinstance(female_full_name, str)  # Ensure the name is a string

    # Clean up is not necessary as the Person object is stateless and fixture scoped functionally
