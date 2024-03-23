# file mimesis/providers/food.py:42-50
# lines [42, 50]
# branches []

import pytest
from mimesis.providers.food import Food
from unittest.mock import Mock

@pytest.fixture
def food_provider():
    return Food()

def test_fruit(food_provider):
    # Mock the _choice_from method to ensure it is called with 'fruits'
    food_provider._choice_from = Mock(return_value='Apple')
    
    fruit_name = food_provider.fruit()
    
    # Check that the returned fruit name is the one we mocked
    assert fruit_name == 'Apple'
    # Verify that _choice_from was called with the correct argument
    food_provider._choice_from.assert_called_once_with('fruits')
