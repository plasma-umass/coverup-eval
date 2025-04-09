# file: lib/ansible/plugins/filter/core.py:71-73
# asked: {"lines": [71, 73], "branches": []}
# gained: {"lines": [71, 73], "branches": []}

import pytest
from ansible.plugins.filter.core import to_nice_json

def test_to_nice_json_default_parameters():
    data = {"key": "value"}
    result = to_nice_json(data)
    assert result == '{\n    "key": "value"\n}'

def test_to_nice_json_custom_indent():
    data = {"key": "value"}
    result = to_nice_json(data, indent=2)
    assert result == '{\n  "key": "value"\n}'

def test_to_nice_json_sort_keys_false():
    data = {"b": 1, "a": 2}
    result = to_nice_json(data, sort_keys=False)
    assert result == '{\n    "b": 1,\n    "a": 2\n}'

def test_to_nice_json_with_additional_args():
    data = {"key": "value"}
    result = to_nice_json(data, indent=2, sort_keys=False, ensure_ascii=False)
    assert result == '{\n  "key": "value"\n}'
