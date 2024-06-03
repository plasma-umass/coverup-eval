# file pysnooper/utils.py:90-95
# lines [90, 91, 92, 93, 95]
# branches ['91->93', '91->95']

import pytest
from unittest import mock
from pysnooper.utils import ensure_tuple
from collections.abc import Iterable

def test_ensure_tuple_with_iterable():
    # Test with an iterable that is not a string
    result = ensure_tuple([1, 2, 3])
    assert result == (1, 2, 3)

def test_ensure_tuple_with_string():
    # Test with a string
    result = ensure_tuple("abc")
    assert result == ("abc",)

def test_ensure_tuple_with_non_iterable():
    # Test with a non-iterable
    result = ensure_tuple(123)
    assert result == (123,)

def test_ensure_tuple_with_mocked_iterable(mocker):
    # Test with a mocked iterable that is not a string
    mock_iterable = mocker.Mock(spec=Iterable)
    mock_iterable.__iter__ = mocker.Mock(return_value=iter([1, 2, 3]))
    result = ensure_tuple(mock_iterable)
    assert result == (1, 2, 3)
