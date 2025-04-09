# file: lib/ansible/plugins/filter/core.py:202-208
# asked: {"lines": [202, 203, 207, 208], "branches": [[203, 207], [203, 208]]}
# gained: {"lines": [202, 203, 207, 208], "branches": [[203, 207], [203, 208]]}

import pytest
from ansible.plugins.filter.core import from_yaml
from ansible.module_utils.six import string_types
import yaml

def test_from_yaml_with_string(monkeypatch):
    test_data = "key: value"
    
    def mock_yaml_load(data):
        return yaml.safe_load(data)
    
    monkeypatch.setattr('ansible.plugins.filter.core.yaml_load', mock_yaml_load)
    
    result = from_yaml(test_data)
    assert result == {'key': 'value'}

def test_from_yaml_with_non_string():
    test_data = {'key': 'value'}
    result = from_yaml(test_data)
    assert result == {'key': 'value'}
