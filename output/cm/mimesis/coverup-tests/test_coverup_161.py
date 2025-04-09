# file mimesis/providers/person.py:364-380
# lines [376, 377, 379, 380]
# branches ['376->377', '376->379']

import pytest
from mimesis.providers.person import Person
from mimesis.enums import Gender
from mimesis import Generic

@pytest.fixture
def person():
    return Person()

def test_sexual_orientation_symbol(person):
    # Mock the random.choice method to return a specific symbol
    person.random.choice = lambda x: x[0]
    # Call the method with symbol=True to cover lines 376-377
    result = person.sexual_orientation(symbol=True)
    # Assert that the result is the first element of SEXUALITY_SYMBOLS
    assert result == '⚤', "The result should be the first symbol of SEXUALITY_SYMBOLS"
