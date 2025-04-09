# file: pysnooper/utils.py:67-78
# asked: {"lines": [71, 72, 75], "branches": [[74, 75]]}
# gained: {"lines": [71, 72, 75], "branches": [[74, 75]]}

import pytest
from unittest.mock import Mock, patch
from pysnooper.utils import get_shortish_repr

def test_get_shortish_repr_normal_case():
    item = "This is a test string"
    result = get_shortish_repr(item)
    assert result == repr(item).replace('\r', '').replace('\n', '')

def test_get_shortish_repr_with_custom_repr():
    item = "test"
    custom_repr = [(str, lambda x: f"custom: {x}")]
    result = get_shortish_repr(item, custom_repr=custom_repr)
    assert result == "custom: test"

def test_get_shortish_repr_with_exception_in_repr_function():
    item = Mock()
    item.__repr__ = Mock(side_effect=Exception("repr failed"))
    result = get_shortish_repr(item)
    assert result == "REPR FAILED"

def test_get_shortish_repr_with_normalize():
    item = "test\nstring"
    with patch('pysnooper.utils.normalize_repr', return_value="normalized") as mock_normalize:
        result = get_shortish_repr(item, normalize=True)
        mock_normalize.assert_called_once_with(repr(item).replace('\r', '').replace('\n', ''))
        assert result == "normalized"

def test_get_shortish_repr_with_max_length():
    item = "This is a very long test string that needs to be truncated"
    max_length = 20
    with patch('pysnooper.utils.truncate', return_value="truncated") as mock_truncate:
        result = get_shortish_repr(item, max_length=max_length)
        mock_truncate.assert_called_once_with(repr(item).replace('\r', '').replace('\n', ''), max_length)
        assert result == "truncated"

def test_get_shortish_repr_with_all_options():
    item = "This is a test string\nwith new lines"
    custom_repr = [(str, lambda x: f"custom: {x}")]
    max_length = 20
    with patch('pysnooper.utils.normalize_repr', return_value="normalized") as mock_normalize, \
         patch('pysnooper.utils.truncate', return_value="truncated") as mock_truncate:
        result = get_shortish_repr(item, custom_repr=custom_repr, max_length=max_length, normalize=True)
        mock_normalize.assert_called_once_with("custom: This is a test stringwith new lines")
        mock_truncate.assert_called_once_with("normalized", max_length)
        assert result == "truncated"
