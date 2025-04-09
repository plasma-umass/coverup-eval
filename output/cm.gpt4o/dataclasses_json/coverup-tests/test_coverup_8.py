# file dataclasses_json/core.py:283-292
# lines [283, 290, 291, 292]
# branches []

import pytest
from unittest.mock import patch

# Assuming _decode_dict_keys is imported from dataclasses_json.core
from dataclasses_json.core import _decode_dict_keys

def test_decode_dict_keys_with_none_key_type():
    xs = {'1': 'one', '2': 'two'}
    infer_missing = False

    result = list(_decode_dict_keys(None, xs, infer_missing))
    assert result == ['1', '2']

def test_decode_dict_keys_with_any_key_type():
    from typing import Any
    xs = {'1': 'one', '2': 'two'}
    infer_missing = False

    result = list(_decode_dict_keys(Any, xs, infer_missing))
    assert result == ['1', '2']

def test_decode_dict_keys_with_int_key_type():
    xs = {'1': 'one', '2': 'two'}
    infer_missing = False

    result = list(_decode_dict_keys(int, xs, infer_missing))
    assert result == [1, 2]

def test_decode_dict_keys_with_str_key_type():
    xs = {'1': 'one', '2': 'two'}
    infer_missing = False

    result = list(_decode_dict_keys(str, xs, infer_missing))
    assert result == ['1', '2']
