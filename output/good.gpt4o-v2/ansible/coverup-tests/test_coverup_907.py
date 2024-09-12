# file: lib/ansible/plugins/filter/core.py:71-73
# asked: {"lines": [71, 73], "branches": []}
# gained: {"lines": [71, 73], "branches": []}

import pytest
from ansible.plugins.filter.core import to_nice_json

def test_to_nice_json():
    data = {"key": "value"}
    expected_output = '{\n    "key": "value"\n}'
    
    result = to_nice_json(data, indent=4, sort_keys=True)
    
    assert result == expected_output

def test_to_nice_json_with_args_and_kwargs():
    data = {"key": "value"}
    expected_output = '{\n    "key": "value"\n}'
    
    result = to_nice_json(data, 4, True)
    
    assert result == expected_output
