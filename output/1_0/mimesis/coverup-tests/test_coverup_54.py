# file mimesis/providers/food.py:27-30
# lines [27, 29, 30]
# branches []

import pytest
from mimesis.providers.food import Food
from mimesis import Generic

@pytest.fixture
def food_provider():
    return Food()

def test_choice_from(food_provider):
    # Mock the internal data to control the output
    food_provider._data = {
        'test_key': ['apple', 'banana', 'cherry']
    }

    # Mock the random.choice method to return a predictable value
    food_provider.random.choice = lambda x: x[0]

    # Call the method under test
    result = food_provider._choice_from('test_key')

    # Assert that the result is as expected
    assert result == 'apple', "The result should be the first element of the list"

    # Clean up by deleting the mock
    del food_provider._data['test_key']
    del food_provider.random.choice
