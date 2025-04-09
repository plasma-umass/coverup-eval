# file mimesis/providers/person.py:291-315
# lines [291, 292, 309, 310, 312, 313, 315]
# branches ['309->310', '309->312', '312->313', '312->315']

import pytest
from mimesis.providers.person import Person
from mimesis.data import GENDER_SYMBOLS

@pytest.fixture
def person():
    return Person()

def test_gender_iso5218(person, mocker):
    mocker.patch.object(person.random, 'choice', return_value=1)
    result = person.gender(iso5218=True)
    assert result == 1

def test_gender_symbol(person, mocker):
    mocker.patch.object(person.random, 'choice', return_value=GENDER_SYMBOLS[0])
    result = person.gender(symbol=True)
    assert result == GENDER_SYMBOLS[0]

def test_gender_default(person, mocker):
    mocker.patch.object(person.random, 'choice', return_value='Male')
    person._data = {'gender': ['Male', 'Female']}
    result = person.gender()
    assert result == 'Male'
