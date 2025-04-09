# file pymonet/immutable_list.py:99-111
# lines [99, 108, 109, 111]
# branches ['108->109', '108->111']

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_map(mocker):
    # Mock the function to be used with map
    mock_fn = mocker.Mock(side_effect=lambda x: x * 2 if x is not None else None)
    
    # Test case where tail is None
    list_with_no_tail = ImmutableList(1)
    result = list_with_no_tail.map(mock_fn)
    assert result.head == 2
    assert result.tail is None
    mock_fn.assert_called_once_with(1)
    
    # Reset the mock for the next test
    mock_fn.reset_mock()
    
    # Test case where tail is not None
    list_with_tail = ImmutableList(1, ImmutableList(2))
    result = list_with_tail.map(mock_fn)
    assert result.head == 2
    assert result.tail.head == 4
    assert result.tail.tail is None
    mock_fn.assert_has_calls([mocker.call(1), mocker.call(2)])
