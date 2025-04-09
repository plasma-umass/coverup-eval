# file mimesis/providers/person.py:415-424
# lines [423, 424]
# branches []

import pytest
from mimesis.providers.person import Person
from mimesis.enums import Gender
from mimesis import Generic

@pytest.fixture
def person():
    return Person()

def test_views_on(person, mocker):
    # Mock the data to ensure the test is deterministic
    test_data = {
        'views_on': ['Positive', 'Neutral', 'Negative']
    }
    mocker.patch.object(person, '_data', test_data)

    # Call the method to test
    result = person.views_on()

    # Check that the result is in the mocked data
    assert result in test_data['views_on']

    # Clean up is not necessary as the mocker fixture automatically undoes patches after the test
