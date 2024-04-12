# file flutes/iterator.py:92-111
# lines [92, 105, 106, 107, 108, 109, 110, 111]
# branches ['106->107', '106->111', '107->108', '107->109']

import pytest
from flutes.iterator import drop_until

def test_drop_until():
    # Test dropping elements until a condition is met
    def is_greater_than_five(x):
        return x > 5

    # Create a list to test the function
    test_list = list(range(10))

    # Use the drop_until function
    result = list(drop_until(is_greater_than_five, test_list))

    # Check the result is as expected
    assert result == [6, 7, 8, 9]

    # Test with an iterable that does not satisfy the condition at all
    result = list(drop_until(is_greater_than_five, range(5)))
    assert result == []

    # Test with an empty iterable
    result = list(drop_until(is_greater_than_five, []))
    assert result == []

    # Test with a condition that is immediately satisfied
    result = list(drop_until(lambda x: x == 0, range(10)))
    assert result == list(range(10))

    # Test with a non-list iterable
    result = list(drop_until(is_greater_than_five, (x for x in range(10))))
    assert result == [6, 7, 8, 9]

def test_drop_until_with_mock(mocker):
    # Mock an iterable to ensure the function cleans up properly
    mock_iterable = mocker.MagicMock()
    mock_iterable.__iter__.return_value = iter(range(10))

    # Use the drop_until function with the mocked iterable
    result = list(drop_until(lambda x: x > 5, mock_iterable))

    # Check the result is as expected
    assert result == [6, 7, 8, 9]

    # Verify that the iterable was only accessed once
    mock_iterable.__iter__.assert_called_once()
