# file pymonet/immutable_list.py:113-130
# lines [122, 123, 124, 125, 127, 128, 130]
# branches ['122->123', '122->127', '123->124', '123->125', '127->128', '127->130']

import pytest
from pymonet.immutable_list import ImmutableList

def test_filter_empty_tail(mocker):
    # Mocking the ImmutableList to control the head and tail
    mock_head = mocker.Mock()
    mock_tail = None
    mock_fn = mocker.Mock(return_value=True)
    
    # Creating an ImmutableList instance with a mocked head and no tail
    immutable_list = ImmutableList(mock_head, mock_tail)
    
    # Test when fn(self.head) returns True
    result = immutable_list.filter(mock_fn)
    assert result.head == mock_head
    assert result.tail is None
    
    # Test when fn(self.head) returns False
    mock_fn.return_value = False
    result = immutable_list.filter(mock_fn)
    assert result.head is None
    assert result.tail is None

def test_filter_non_empty_tail(mocker):
    # Mocking the ImmutableList to control the head and tail
    mock_head = mocker.Mock()
    mock_tail = mocker.Mock()
    mock_fn = mocker.Mock(return_value=True)
    
    # Creating an ImmutableList instance with a mocked head and tail
    immutable_list = ImmutableList(mock_head, mock_tail)
    
    # Test when fn(self.head) returns True
    result = immutable_list.filter(mock_fn)
    assert result.head == mock_head
    assert result.tail == mock_tail.filter(mock_fn)
    
    # Test when fn(self.head) returns False
    mock_fn.return_value = False
    result = immutable_list.filter(mock_fn)
    assert result == mock_tail.filter(mock_fn)
