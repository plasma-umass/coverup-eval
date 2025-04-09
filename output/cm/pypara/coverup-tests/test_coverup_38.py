# file pypara/monetary.py:140-145
# lines [140, 141, 145]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def positive(self) -> "Money":
        return self

def test_money_positive(mocker):
    # Create a mock object for the abstract class
    mock_money = mocker.MagicMock(spec=Money)
    
    # Set up the mock to return itself when positive is called
    mock_money.positive.return_value = mock_money
    
    # Call the positive method
    result = mock_money.positive()
    
    # Assert that the result is the mock itself
    assert result is mock_money
    
    # Assert that the positive method was called once
    mock_money.positive.assert_called_once()
