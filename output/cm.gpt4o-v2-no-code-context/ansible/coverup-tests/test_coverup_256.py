# file: lib/ansible/utils/vars.py:58-79
# asked: {"lines": [58, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[70, 0], [70, 71], [72, 73], [72, 77]]}
# gained: {"lines": [58, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[70, 0], [70, 71], [72, 73], [72, 77]]}

import pytest
from ansible.errors import AnsibleError
from ansible.utils.vars import _validate_mutable_mappings
from collections.abc import MutableMapping

class MockMutableMapping(MutableMapping):
    def __init__(self, *args, **kwargs):
        self.store = dict(*args, **kwargs)

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

def test_validate_mutable_mappings_with_valid_mappings():
    a = MockMutableMapping({'key1': 'value1'})
    b = MockMutableMapping({'key2': 'value2'})
    # This should not raise an exception
    _validate_mutable_mappings(a, b)

def test_validate_mutable_mappings_with_invalid_mappings():
    a = {'key1': 'value1'}
    b = ['key2', 'value2']
    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings(a, b)
    assert "failed to combine variables, expected dicts but got a 'dict' and a 'list'" in str(excinfo.value)

def test_validate_mutable_mappings_with_non_serializable_object(mocker):
    class NonSerializable:
        pass

    a = NonSerializable()
    b = {'key': 'value'}

    mocker.patch('ansible.utils.vars.dumps', side_effect=Exception("Cannot serialize"))

    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings(a, b)
    assert "failed to combine variables, expected dicts but got a 'NonSerializable' and a 'dict'" in str(excinfo.value)
