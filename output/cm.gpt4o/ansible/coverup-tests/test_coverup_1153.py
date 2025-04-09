# file lib/ansible/plugins/filter/core.py:279-287
# lines [280, 281, 282, 283, 284, 285, 287]
# branches ['281->282', '281->287']

import pytest
import uuid
from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_native, to_text
from ansible.plugins.filter.core import to_uuid

def test_to_uuid_invalid_namespace():
    invalid_namespace = "invalid-namespace"
    with pytest.raises(AnsibleFilterError) as excinfo:
        to_uuid("test-string", invalid_namespace)
    assert "Invalid value" in str(excinfo.value)

def test_to_uuid_valid_namespace():
    valid_namespace = uuid.uuid4()
    result = to_uuid("test-string", valid_namespace)
    assert isinstance(result, str)
    assert len(result) == 36  # UUID length

def test_to_uuid_default_namespace():
    result = to_uuid("test-string")
    assert isinstance(result, str)
    assert len(result) == 36  # UUID length
