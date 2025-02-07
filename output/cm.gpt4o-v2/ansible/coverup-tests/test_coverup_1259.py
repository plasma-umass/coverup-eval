# file: lib/ansible/utils/vars.py:58-79
# asked: {"lines": [75, 76], "branches": []}
# gained: {"lines": [75, 76], "branches": []}

import pytest
from ansible.errors import AnsibleError
from ansible.utils.vars import _validate_mutable_mappings
from unittest.mock import patch

def test_validate_mutable_mappings_with_non_serializable_object():
    class NonSerializable:
        def __str__(self):
            return "NonSerializable instance"

    a = {"key": "value"}
    b = NonSerializable()

    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings(a, b)
    
    assert "failed to combine variables, expected dicts but got a 'dict' and a 'NonSerializable'" in str(excinfo.value)

def test_validate_mutable_mappings_with_serializable_and_non_serializable_objects():
    class NonSerializable:
        def __str__(self):
            return "NonSerializable instance"

    a = NonSerializable()
    b = NonSerializable()

    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings(a, b)
    
    assert "failed to combine variables, expected dicts but got a 'NonSerializable' and a 'NonSerializable'" in str(excinfo.value)

def test_validate_mutable_mappings_with_serializable_object():
    a = {"key": "value"}
    b = {"another_key": "another_value"}

    try:
        _validate_mutable_mappings(a, b)
    except AnsibleError:
        pytest.fail("AnsibleError raised unexpectedly")

