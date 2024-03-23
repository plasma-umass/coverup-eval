# file mimesis/providers/person.py:364-380
# lines [376, 377, 379, 380]
# branches ['376->377', '376->379']

import pytest
from mimesis.providers.person import Person

@pytest.fixture
def person():
    return Person()

def test_sexual_orientation_with_symbol(person, mocker):
    # Mock the random.choice method to control its output
    mocker.patch('mimesis.random.Random.choice', return_value='♂')

    # Call the method with symbol=True to cover lines 376-377
    result = person.sexual_orientation(symbol=True)

    # Assert that the result is the mocked return value
    assert result == '♂'

def test_sexual_orientation_without_symbol(person, mocker):
    # Mock the random.choice method to control its output
    mocker.patch('mimesis.random.Random.choice', return_value='Heterosexuality')

    # Call the method with symbol=False to cover lines 379-380
    result = person.sexual_orientation(symbol=False)

    # Assert that the result is the mocked return value
    assert result == 'Heterosexuality'
