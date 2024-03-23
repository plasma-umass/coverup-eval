# file mimesis/providers/food.py:62-70
# lines [62, 70]
# branches []

import pytest
from mimesis.providers.food import Food

@pytest.fixture
def food_provider():
    return Food()

def test_spices(food_provider):
    spice = food_provider.spices()
    assert spice is not None
    assert isinstance(spice, str)

    # Ensure that the spice is in the predefined list of spices
    # Since we cannot import Locale, we will not use it to create a generic object
    # Instead, we will directly access the food provider's data
    expected_spices = food_provider._data['spices']
    assert spice in expected_spices
