# file mimesis/providers/food.py:32-40
# lines [32, 40]
# branches []

import pytest
from mimesis.providers.food import Food

@pytest.fixture
def food_provider():
    return Food()

def test_vegetable(food_provider):
    vegetable = food_provider.vegetable()
    assert isinstance(vegetable, str)
    assert len(vegetable) > 0
