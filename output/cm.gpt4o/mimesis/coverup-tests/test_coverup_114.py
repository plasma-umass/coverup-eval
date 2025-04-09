# file mimesis/providers/person.py:354-362
# lines [354, 362]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis.data import BLOOD_GROUPS

@pytest.fixture
def person():
    return Person()

def test_blood_type(person, mocker):
    mocker.patch.object(person.random, 'choice', return_value='A+')
    blood_type = person.blood_type()
    assert blood_type == 'A+'
    assert blood_type in BLOOD_GROUPS
