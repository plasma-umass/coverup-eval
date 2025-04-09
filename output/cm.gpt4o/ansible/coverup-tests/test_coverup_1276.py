# file lib/ansible/utils/vars.py:58-79
# lines [75, 76]
# branches []

import pytest
from ansible.errors import AnsibleError
from ansible.utils.vars import _validate_mutable_mappings
from collections.abc import MutableMapping
from unittest.mock import patch

class NonSerializableObject:
    def __str__(self):
        return "NonSerializableObject"

class TestMutableMappings:
    def test_validate_mutable_mappings_non_serializable(self, mocker):
        # Create a mock for the dumps function to raise an exception
        mock_dumps = mocker.patch('ansible.utils.vars.dumps', side_effect=Exception("Serialization Error"))
        
        a = NonSerializableObject()
        b = NonSerializableObject()
        
        with pytest.raises(AnsibleError) as excinfo:
            _validate_mutable_mappings(a, b)
        
        assert "failed to combine variables, expected dicts but got a 'NonSerializableObject' and a 'NonSerializableObject'" in str(excinfo.value)
        assert "NonSerializableObject" in str(excinfo.value)
        
        # Ensure that the mock was called
        assert mock_dumps.call_count == 2
