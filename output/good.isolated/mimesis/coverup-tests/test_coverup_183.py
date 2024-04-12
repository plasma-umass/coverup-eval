# file mimesis/providers/person.py:97-113
# lines [110, 111]
# branches ['109->110']

import pytest
from mimesis.enums import Gender
from mimesis.providers.person import Person
from unittest.mock import patch

@pytest.fixture
def person_provider():
    return Person()

def test_surname_with_gender_dict(person_provider):
    # Mock the _data to contain a dict for surnames
    with patch.object(person_provider, '_data', {'surnames': {'male': ['Smith'], 'female': ['Doe']}}):
        # Test with Gender.MALE
        male_surname = person_provider.surname(gender=Gender.MALE)
        assert male_surname == 'Smith'

        # Test with Gender.FEMALE
        female_surname = person_provider.surname(gender=Gender.FEMALE)
        assert female_surname == 'Doe'
