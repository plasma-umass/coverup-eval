# file: lib/ansible/plugins/filter/core.py:71-73
# asked: {"lines": [71, 73], "branches": []}
# gained: {"lines": [71, 73], "branches": []}

import pytest
from ansible.plugins.filter.core import to_nice_json
import json

def test_to_nice_json_basic():
    data = {"key": "value"}
    result = to_nice_json(data)
    expected = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '))
    assert result == expected

def test_to_nice_json_with_indent():
    data = {"key": "value"}
    result = to_nice_json(data, indent=2)
    expected = json.dumps(data, indent=2, sort_keys=True, separators=(',', ': '))
    assert result == expected

def test_to_nice_json_without_sort_keys():
    data = {"key": "value"}
    result = to_nice_json(data, sort_keys=False)
    expected = json.dumps(data, indent=4, sort_keys=False, separators=(',', ': '))
    assert result == expected

def test_to_nice_json_with_additional_args():
    data = {"key": "value"}
    result = to_nice_json(data, indent=2, sort_keys=False, ensure_ascii=False)
    expected = json.dumps(data, indent=2, sort_keys=False, separators=(',', ': '), ensure_ascii=False)
    assert result == expected
