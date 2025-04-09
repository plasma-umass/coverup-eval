# file mimesis/providers/person.py:426-442
# lines [426, 435, 438, 439, 440, 442]
# branches ['438->439', '438->442']

import pytest
from mimesis.providers.person import Person
from mimesis.enums import Gender

@pytest.fixture
def person(mocker):
    instance = Person()
    mocker.patch.object(instance, '_data', {
        'nationality': {
            'male': ['Russian', 'American'],
            'female': ['Russian', 'American'],
        }
    })
    return instance

def test_nationality_with_gender(person):
    nationality_male = person.nationality(Gender.MALE)
    assert nationality_male in ['Russian', 'American']
    
    nationality_female = person.nationality(Gender.FEMALE)
    assert nationality_female in ['Russian', 'American']

def test_nationality_without_gender(mocker):
    instance = Person()
    mocker.patch.object(instance, '_data', {
        'nationality': ['Russian', 'American']
    })
    nationality = instance.nationality()
    assert nationality in ['Russian', 'American']
