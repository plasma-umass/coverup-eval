# file mimesis/providers/food.py:10-12
# lines [10, 11]
# branches []

import pytest
from mimesis.providers.food import Food
from mimesis.providers.base import BaseDataProvider

@pytest.fixture
def food_provider():
    return Food()

def test_food_provider(food_provider):
    assert isinstance(food_provider, Food)
    assert issubclass(Food, BaseDataProvider)
