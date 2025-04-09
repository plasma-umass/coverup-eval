# file: lib/ansible/plugins/filter/core.py:71-73
# asked: {"lines": [71, 73], "branches": []}
# gained: {"lines": [71, 73], "branches": []}

import pytest
from ansible.plugins.filter.core import to_nice_json

def test_to_nice_json_default_parameters():
    data = {"key": "value"}
    expected_output = '{\n    "key": "value"\n}'
    assert to_nice_json(data) == expected_output

def test_to_nice_json_custom_indent():
    data = {"key": "value"}
    expected_output = '{\n  "key": "value"\n}'
    assert to_nice_json(data, indent=2) == expected_output

def test_to_nice_json_sort_keys_false():
    data = {"b": "value2", "a": "value1"}
    expected_output = '{\n    "b": "value2",\n    "a": "value1"\n}'
    assert to_nice_json(data, sort_keys=False) == expected_output

def test_to_nice_json_with_additional_args():
    data = {"key": "value"}
    expected_output = '{\n    "key": "value"\n}'
    assert to_nice_json(data, 4, True) == expected_output

def test_to_nice_json_with_additional_kwargs():
    data = {"key": "value"}
    expected_output = '{\n    "key": "value"\n}'
    assert to_nice_json(data, indent=4, sort_keys=True) == expected_output
