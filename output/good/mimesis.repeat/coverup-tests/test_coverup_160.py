# file mimesis/providers/person.py:291-315
# lines [310, 313]
# branches ['309->310', '312->313']

import pytest
from mimesis.providers.person import Person
from mimesis.enums import Gender

@pytest.fixture
def person(mocker):
    return Person()

def test_gender_iso5218(person):
    result = person.gender(iso5218=True)
    assert result in [0, 1, 2, 9]

def test_gender_symbol(person, mocker):
    mocker.patch('mimesis.providers.person.GENDER_SYMBOLS', ['♂', '♀'])
    result = person.gender(symbol=True)
    assert result in ['♂', '♀']
