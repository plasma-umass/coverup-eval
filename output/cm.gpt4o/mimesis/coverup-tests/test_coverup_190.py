# file mimesis/random.py:134-143
# lines [143]
# branches ['141->143']

import pytest
import random as random_module
from mimesis.random import get_random_item

class MockEnum:
    ITEM1 = 1
    ITEM2 = 2
    ITEM3 = 3

    def __iter__(self):
        return iter([self.ITEM1, self.ITEM2, self.ITEM3])

def test_get_random_item_without_custom_random(mocker):
    mock_enum = MockEnum()
    mock_choice = mocker.patch('random.choice', return_value=mock_enum.ITEM1)
    
    result = get_random_item(mock_enum)
    
    mock_choice.assert_called_once_with([mock_enum.ITEM1, mock_enum.ITEM2, mock_enum.ITEM3])
    assert result == mock_enum.ITEM1
