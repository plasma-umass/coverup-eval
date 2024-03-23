# file mimesis/providers/food.py:22-25
# lines [22, 23, 25]
# branches []

import pytest
from mimesis.providers.food import Food
from mimesis import Generic

@pytest.fixture
def food_provider():
    return Food()

def test_food_meta_name(food_provider):
    assert food_provider.Meta.name == 'food'
