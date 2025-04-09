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
    # Test that full_name method covers both genders
    male_full_name = person.full_name(gender=Gender.MALE)
    female_full_name = person.full_name(gender=Gender.FEMALE)

    assert male_full_name != female_full_name  # Assuming male and female names are different

    # Clean up is not necessary as the Person object is created in the fixture
    # and will be garbage collected after the test runs
