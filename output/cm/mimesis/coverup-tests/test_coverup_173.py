# file mimesis/providers/person.py:426-442
# lines [435, 438, 439, 440, 442]
# branches ['438->439', '438->442']

import pytest
from mimesis.enums import Gender
from mimesis.providers.person import Person

@pytest.fixture
def person_with_gender_data(mocker):
    # Mock the _data attribute to include gender-specific nationalities
    data = {
        'nationality': {
            'male': ['Russian', 'American'],
            'female': ['British', 'Italian']
        }
    }
    person_instance = Person()
    mocker.patch.object(person_instance, '_data', data)
    return person_instance

def test_nationality_with_gender(person_with_gender_data):
    male_nationality = person_with_gender_data.nationality(gender=Gender.MALE)
    female_nationality = person_with_gender_data.nationality(gender=Gender.FEMALE)
    
    assert male_nationality in ['Russian', 'American']
    assert female_nationality in ['British', 'Italian']
