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
    # Test with male gender
    male_last_name = person_provider.last_name(gender=Gender.MALE)
    assert male_last_name is not None
    assert isinstance(male_last_name, str)

    # Test with female gender
    female_last_name = person_provider.last_name(gender=Gender.FEMALE)
    assert female_last_name is not None
    assert isinstance(female_last_name, str)

    # Test with unspecified gender
    any_last_name = person_provider.last_name()
    assert any_last_name is not None
    assert isinstance(any_last_name, str)

    # Test with non-Gender enum value should fall back to default behavior
    other_last_name = person_provider.last_name(gender="non_enum_value")
    assert other_last_name is not None
    assert isinstance(other_last_name, str)
