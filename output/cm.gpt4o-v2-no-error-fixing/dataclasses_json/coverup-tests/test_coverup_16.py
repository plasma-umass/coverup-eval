# file: dataclasses_json/core.py:283-292
# asked: {"lines": [290, 291, 292], "branches": []}
# gained: {"lines": [290, 291, 292], "branches": []}

import pytest
from dataclasses_json.core import _decode_dict_keys
from typing import Any

def test_decode_dict_keys_with_none_key_type():
    result = list(_decode_dict_keys(None, {'1': 'one', '2': 'two'}, False))
    assert result == ['1', '2']

def test_decode_dict_keys_with_any_key_type():
    result = list(_decode_dict_keys(Any, {'1': 'one', '2': 'two'}, False))
    assert result == ['1', '2']

def test_decode_dict_keys_with_specific_key_type():
    result = list(_decode_dict_keys(int, {'1': 'one', '2': 'two'}, False))
    assert result == [1, 2]
