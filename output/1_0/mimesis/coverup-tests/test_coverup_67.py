# file mimesis/providers/food.py:13-20
# lines [13, 18, 19, 20]
# branches []

import pytest
from mimesis.providers.food import Food


@pytest.fixture
def food_provider(mocker):
    mocker.patch('mimesis.providers.BaseDataProvider._pull')
    return Food()


def test_food_init(mocker):
    mock_pull = mocker.patch('mimesis.providers.BaseDataProvider._pull')
    food = Food()
    mock_pull.assert_called_once_with('food.json')
    assert food._datafile == 'food.json'
