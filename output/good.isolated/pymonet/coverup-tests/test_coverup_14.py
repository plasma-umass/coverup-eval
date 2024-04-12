# file pymonet/immutable_list.py:18-22
# lines [18, 19, 20, 21, 22]
# branches []

import pytest
from pymonet.immutable_list import ImmutableList

@pytest.fixture
def mock_immutable_list(mocker):
    mock_list = mocker.MagicMock(spec=ImmutableList)
    mock_list.head = 'head'
    mock_list.tail = 'tail'
    mock_list.is_empty = False
    return mock_list

def test_immutable_list_eq(mock_immutable_list):
    other = ImmutableList()
    other.head = 'head'
    other.tail = 'tail'
    other.is_empty = False

    assert mock_immutable_list == other

def test_immutable_list_not_eq_different_type(mock_immutable_list):
    other = object()
    assert not mock_immutable_list == other

def test_immutable_list_not_eq_different_head(mock_immutable_list):
    other = ImmutableList()
    other.head = 'different head'
    other.tail = 'tail'
    other.is_empty = False

    assert not mock_immutable_list == other

def test_immutable_list_not_eq_different_tail(mock_immutable_list):
    other = ImmutableList()
    other.head = 'head'
    other.tail = 'different tail'
    other.is_empty = False

    assert not mock_immutable_list == other

def test_immutable_list_not_eq_different_is_empty(mock_immutable_list):
    other = ImmutableList()
    other.head = 'head'
    other.tail = 'tail'
    other.is_empty = True

    assert not mock_immutable_list == other
