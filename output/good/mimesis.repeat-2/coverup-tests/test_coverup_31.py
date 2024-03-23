# file mimesis/providers/person.py:291-315
# lines [291, 292, 309, 310, 312, 313, 315]
# branches ['309->310', '309->312', '312->313', '312->315']

import pytest
from mimesis.providers.person import Person

@pytest.fixture
def person_provider():
    return Person()

def test_gender_iso5218(person_provider):
    gender = person_provider.gender(iso5218=True)
    assert gender in [0, 1, 2, 9]

def test_gender_symbol(person_provider, mocker):
    mocker.patch('mimesis.providers.person.GENDER_SYMBOLS', ['♂', '♀'])
    gender = person_provider.gender(symbol=True)
    assert gender in ['♂', '♀']

def test_gender_default(person_provider):
    gender = person_provider.gender()
    assert gender in person_provider._data['gender']
