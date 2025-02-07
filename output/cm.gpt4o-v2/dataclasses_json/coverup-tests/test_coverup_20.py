# file: dataclasses_json/core.py:283-292
# asked: {"lines": [283, 290, 291, 292], "branches": []}
# gained: {"lines": [283, 290, 291, 292], "branches": []}

import pytest
from typing import Any
from dataclasses_json.core import _decode_dict_keys

def test_decode_dict_keys_with_none_key_type(mocker):
    mock_decode_items = mocker.patch('dataclasses_json.core._decode_items', return_value=[1, 2, 3])
    key_type = None
    xs = ['1', '2', '3']
    infer_missing = False

    result = list(_decode_dict_keys(key_type, xs, infer_missing))

    assert result == [1, 2, 3]
    mock_decode_items.assert_called_once()
    called_args = mock_decode_items.call_args[0]
    assert called_args[0](1) == 1  # Check that the lambda function works as expected
    assert called_args[1] == xs
    assert called_args[2] == infer_missing

def test_decode_dict_keys_with_any_key_type(mocker):
    mock_decode_items = mocker.patch('dataclasses_json.core._decode_items', return_value=['a', 'b', 'c'])
    key_type = Any
    xs = ['a', 'b', 'c']
    infer_missing = False

    result = list(_decode_dict_keys(key_type, xs, infer_missing))

    assert result == ['a', 'b', 'c']
    mock_decode_items.assert_called_once()
    called_args = mock_decode_items.call_args[0]
    assert called_args[0](1) == 1  # Check that the lambda function works as expected
    assert called_args[1] == xs
    assert called_args[2] == infer_missing

def test_decode_dict_keys_with_specific_key_type(mocker):
    mock_decode_items = mocker.patch('dataclasses_json.core._decode_items', return_value=['1', '2', '3'])
    key_type = int
    xs = ['1', '2', '3']
    infer_missing = False

    result = list(_decode_dict_keys(key_type, xs, infer_missing))

    assert result == [1, 2, 3]
    mock_decode_items.assert_called_once_with(key_type, xs, infer_missing)
