# file mimesis/providers/person.py:364-380
# lines [364, 376, 377, 379, 380]
# branches ['376->377', '376->379']

import pytest
from mimesis.providers.person import Person

# Constants representing sexual orientation symbols
SEXUALITY_SYMBOLS = ['⚤', '⚢', '⚣', '⚪']

@pytest.fixture
def person():
    return Person(seed=0)

def test_sexual_orientation_with_symbol(person, mocker):
    # Mock the random.choice method of the person instance to return a specific symbol
    mocker.patch.object(person.random, 'choice', return_value=SEXUALITY_SYMBOLS[0])
    
    # Call the method with symbol=True
    result = person.sexual_orientation(symbol=True)
    
    # Assert that the result is the first symbol in SEXUALITY_SYMBOLS
    assert result == SEXUALITY_SYMBOLS[0]

def test_sexual_orientation_without_symbol(person, mocker):
    # Mock the random.choice method of the person instance to return a specific sexuality
    test_sexualities = ['Heterosexuality', 'Homosexuality', 'Bisexuality']
    mocker.patch.object(person.random, 'choice', return_value=test_sexualities[0])
    
    # Call the method with symbol=False
    result = person.sexual_orientation(symbol=False)
    
    # Assert that the result is the first sexuality in test_sexualities
    assert result == test_sexualities[0]
