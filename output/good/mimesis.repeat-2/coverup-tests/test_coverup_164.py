# file mimesis/providers/person.py:426-442
# lines [435, 438, 439, 440, 442]
# branches ['438->439', '438->442']

import pytest
from mimesis.enums import Gender
from mimesis.providers.person import Person
from unittest.mock import MagicMock

@pytest.fixture
def person_with_mocked_data():
    person = Person()
    person._data = {'nationality': {'male': ['Russian'], 'female': ['American']}}
    return person

def test_nationality_with_gender(person_with_mocked_data):
    male_nationality = person_with_mocked_data.nationality(gender=Gender.MALE)
    female_nationality = person_with_mocked_data.nationality(gender=Gender.FEMALE)
    
    assert male_nationality == 'Russian'
    assert female_nationality == 'American'
