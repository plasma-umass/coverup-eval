# file: lib/ansible/plugins/filter/core.py:211-217
# asked: {"lines": [212, 216, 217], "branches": [[212, 216], [212, 217]]}
# gained: {"lines": [212, 216, 217], "branches": [[212, 216], [212, 217]]}

import pytest
from ansible.plugins.filter.core import from_yaml_all
from ansible.module_utils.six import string_types
from ansible.module_utils._text import to_text
import yaml

def test_from_yaml_all_string(monkeypatch):
    test_data = "---\nitem1: value1\nitem2: value2\n"
    
    def mock_yaml_load_all(data):
        return list(yaml.safe_load_all(data))
    
    monkeypatch.setattr('ansible.plugins.filter.core.yaml_load_all', mock_yaml_load_all)
    
    result = from_yaml_all(test_data)
    assert result == [{'item1': 'value1', 'item2': 'value2'}]

def test_from_yaml_all_non_string():
    test_data = [{'item1': 'value1', 'item2': 'value2'}]
    result = from_yaml_all(test_data)
    assert result == test_data
