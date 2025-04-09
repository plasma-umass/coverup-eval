# file: dataclasses_json/core.py:283-292
# asked: {"lines": [283, 290, 291, 292], "branches": []}
# gained: {"lines": [283, 290, 291, 292], "branches": []}

import pytest
from typing import Any
from dataclasses_json.core import _decode_dict_keys

def test_decode_dict_keys_with_none_key_type(mocker):
    mock_decode_items = mocker.patch('dataclasses_json.core._decode_items', return_value=[1, 2, 3])
    result = list(_decode_dict_keys(None, [1, 2, 3], False))
    assert result == [1, 2, 3]
    mock_decode_items.assert_called_once()
    called_args = mock_decode_items.call_args[0]
    assert called_args[0](1) == 1  # Check that the lambda function works as expected
    assert called_args[1] == [1, 2, 3]
    assert called_args[2] == False

def test_decode_dict_keys_with_any_key_type(mocker):
    mock_decode_items = mocker.patch('dataclasses_json.core._decode_items', return_value=[1, 2, 3])
    result = list(_decode_dict_keys(Any, [1, 2, 3], False))
    assert result == [1, 2, 3]
    mock_decode_items.assert_called_once()
    called_args = mock_decode_items.call_args[0]
    assert called_args[0](1) == 1  # Check that the lambda function works as expected
    assert called_args[1] == [1, 2, 3]
    assert called_args[2] == False

def test_decode_dict_keys_with_specific_key_type(mocker):
    mock_decode_items = mocker.patch('dataclasses_json.core._decode_items', return_value=['1', '2', '3'])
    result = list(_decode_dict_keys(str, [1, 2, 3], False))
    assert result == ['1', '2', '3']
    mock_decode_items.assert_called_once_with(str, [1, 2, 3], False)
