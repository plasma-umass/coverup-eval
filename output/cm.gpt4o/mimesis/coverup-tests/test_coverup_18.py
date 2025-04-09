# file mimesis/providers/person.py:97-113
# lines [97, 106, 109, 110, 111, 113]
# branches ['109->110', '109->113']

import pytest
from mimesis.providers.person import Person
from mimesis.enums import Gender
from unittest.mock import patch

@pytest.fixture
def person():
    return Person()

def test_surname_with_gender(person):
    with patch.object(person, '_data', {'surnames': {'male': ['Smith', 'Johnson'], 'female': ['Doe', 'Brown']}}):
        surname_male = person.surname(Gender.MALE)
        surname_female = person.surname(Gender.FEMALE)
        
        assert surname_male in ['Smith', 'Johnson']
        assert surname_female in ['Doe', 'Brown']

def test_surname_without_gender(person):
    with patch.object(person, '_data', {'surnames': ['Smith', 'Johnson', 'Doe', 'Brown']}):
        surname = person.surname()
        
        assert surname in ['Smith', 'Johnson', 'Doe', 'Brown']
