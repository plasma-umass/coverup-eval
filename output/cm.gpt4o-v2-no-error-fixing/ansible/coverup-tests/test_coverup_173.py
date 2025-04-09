# file: lib/ansible/utils/vars.py:58-79
# asked: {"lines": [58, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[70, 0], [70, 71], [72, 73], [72, 77]]}
# gained: {"lines": [58, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[70, 0], [70, 71], [72, 73], [72, 77]]}

import pytest
from ansible.errors import AnsibleError
from ansible.module_utils.common._collections_compat import MutableMapping
from ansible.module_utils._text import to_native
from json import dumps

# Assuming _validate_mutable_mappings is imported from ansible.utils.vars
from ansible.utils.vars import _validate_mutable_mappings

class TestValidateMutableMappings:
    
    def test_valid_mutable_mappings(self):
        class MyMapping(MutableMapping):
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
        
        a = MyMapping()
        b = MyMapping()
        # Should not raise an error
        _validate_mutable_mappings(a, b)
    
    def test_invalid_mutable_mappings(self):
        a = {}
        b = []
        with pytest.raises(AnsibleError) as excinfo:
            _validate_mutable_mappings(a, b)
        assert "failed to combine variables, expected dicts but got a 'dict' and a 'list'" in str(excinfo.value)
    
    def test_invalid_mutable_mappings_with_non_serializable(self):
        class NonSerializable:
            pass
        
        a = {}
        b = NonSerializable()
        with pytest.raises(AnsibleError) as excinfo:
            _validate_mutable_mappings(a, b)
        assert "failed to combine variables, expected dicts but got a 'dict' and a 'NonSerializable'" in str(excinfo.value)
