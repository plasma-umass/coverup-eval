# file mimesis/providers/food.py:52-60
# lines [52, 60]
# branches []

import pytest
from mimesis.providers.food import Food

@pytest.fixture
def food_provider():
    return Food()

def test_dish(food_provider):
    dish_name = food_provider.dish()
    assert isinstance(dish_name, str)
    assert dish_name in food_provider._data['dishes']
