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
    # Test last name with male gender
    male_last_name = person_provider.last_name(gender=Gender.MALE)
    assert male_last_name is not None
    assert isinstance(male_last_name, str)

    # Test last name with female gender
    female_last_name = person_provider.last_name(gender=Gender.FEMALE)
    assert female_last_name is not None
    assert isinstance(female_last_name, str)

    # Test last name with no gender specified
    neutral_last_name = person_provider.last_name()
    assert neutral_last_name is not None
    assert isinstance(neutral_last_name, str)
