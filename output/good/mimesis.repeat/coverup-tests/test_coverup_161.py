# file mimesis/providers/person.py:426-442
# lines [439, 440]
# branches ['438->439']

import pytest
from mimesis.enums import Gender
from mimesis.providers.person import Person
from mimesis import Generic

@pytest.fixture
def generic(mocker):
    gen = Generic()
    mocker.patch.object(gen.person, '_data', {'nationality': {'male': ['Russian'], 'female': ['American']}})
    return gen

def test_nationality_with_gender(generic):
    person = generic.person
    male_nationality = person.nationality(gender=Gender.MALE)
    female_nationality = person.nationality(gender=Gender.FEMALE)
    
    assert male_nationality == 'Russian'
    assert female_nationality == 'American'
