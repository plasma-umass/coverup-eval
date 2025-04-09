# file mimesis/providers/person.py:364-380
# lines [364, 376, 377, 379, 380]
# branches ['376->377', '376->379']

import pytest
from mimesis.providers import Person
from mimesis.data import SEXUALITY_SYMBOLS

@pytest.fixture
def person():
    return Person()

def test_sexual_orientation_with_symbol(person, mocker):
    mocker.patch.object(person.random, 'choice', return_value='🏳️‍🌈')
    result = person.sexual_orientation(symbol=True)
    assert result == '🏳️‍🌈'
    person.random.choice.assert_called_once_with(SEXUALITY_SYMBOLS)

def test_sexual_orientation_without_symbol(person, mocker):
    mocker.patch.object(person.random, 'choice', return_value='Heterosexuality')
    mocker.patch.object(person, '_data', {'sexuality': ['Heterosexuality', 'Homosexuality', 'Bisexuality']})
    result = person.sexual_orientation(symbol=False)
    assert result == 'Heterosexuality'
    person.random.choice.assert_called_once_with(['Heterosexuality', 'Homosexuality', 'Bisexuality'])
