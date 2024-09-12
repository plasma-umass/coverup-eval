# file: lib/ansible/utils/vars.py:58-79
# asked: {"lines": [58, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[70, 0], [70, 71], [72, 73], [72, 77]]}
# gained: {"lines": [58, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[70, 0], [70, 71], [72, 73], [72, 77]]}

import pytest
from ansible.errors import AnsibleError
from collections.abc import MutableMapping
from unittest.mock import Mock
import json

# Mocking the necessary functions
def dumps(obj):
    return json.dumps(obj)

def to_native(obj):
    return str(obj)

# Importing the function to be tested
from ansible.utils.vars import _validate_mutable_mappings

class TestValidateMutableMappings:
    def test_both_are_mutable_mappings(self):
        a = {'key1': 'value1'}
        b = {'key2': 'value2'}
        _validate_mutable_mappings(a, b)  # Should not raise an error

    def test_first_is_not_mutable_mapping(self):
        a = ['not', 'a', 'dict']
        b = {'key2': 'value2'}
        with pytest.raises(AnsibleError) as excinfo:
            _validate_mutable_mappings(a, b)
        assert "expected dicts but got a 'list' and a 'dict'" in str(excinfo.value)

    def test_second_is_not_mutable_mapping(self):
        a = {'key1': 'value1'}
        b = ['not', 'a', 'dict']
        with pytest.raises(AnsibleError) as excinfo:
            _validate_mutable_mappings(a, b)
        assert "expected dicts but got a 'dict' and a 'list'" in str(excinfo.value)

    def test_neither_is_mutable_mapping(self):
        a = ['not', 'a', 'dict']
        b = ['also', 'not', 'a', 'dict']
        with pytest.raises(AnsibleError) as excinfo:
            _validate_mutable_mappings(a, b)
        assert "expected dicts but got a 'list' and a 'list'" in str(excinfo.value)

    def test_dumps_raises_exception(self, monkeypatch):
        a = {'key1': 'value1'}
        b = Mock()
        b.__class__.__name__ = 'MockClass'
        b.side_effect = Exception("dumps error")

        monkeypatch.setattr('ansible.utils.vars.dumps', lambda x: (_ for _ in ()).throw(Exception("dumps error")))
        monkeypatch.setattr('ansible.utils.vars.to_native', to_native)

        with pytest.raises(AnsibleError) as excinfo:
            _validate_mutable_mappings(a, b)
        assert "expected dicts but got a 'dict' and a 'MockClass'" in str(excinfo.value)
