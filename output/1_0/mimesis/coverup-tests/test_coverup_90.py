# file mimesis/providers/food.py:72-80
# lines [72, 80]
# branches []

import pytest
from mimesis.providers.food import Food
from mimesis import Generic

@pytest.fixture
def food_provider():
    return Food()

def test_drink(food_provider, mocker):
    # Mock the _choice_from method to ensure it is called with 'drinks'
    mocker.patch.object(food_provider, '_choice_from', return_value='Mocked Drink')

    # Call the drink method
    result = food_provider.drink()

    # Assert that the result is the mocked value
    assert result == 'Mocked Drink'

    # Assert that _choice_from was called with 'drinks'
    food_provider._choice_from.assert_called_once_with('drinks')
