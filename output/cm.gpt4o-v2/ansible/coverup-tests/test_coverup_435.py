# file: lib/ansible/plugins/filter/core.py:279-287
# asked: {"lines": [279, 280, 281, 282, 283, 284, 285, 287], "branches": [[281, 282], [281, 287]]}
# gained: {"lines": [279, 280, 281, 282, 283, 284, 285, 287], "branches": [[281, 282], [281, 287]]}

import pytest
import uuid
from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_native, to_text
from ansible.plugins.filter.core import to_uuid

UUID_NAMESPACE_ANSIBLE = uuid.UUID('361E6D51-FAEC-444A-9079-341386DA8E2E')

def test_to_uuid_valid_namespace():
    result = to_uuid('test_string', UUID_NAMESPACE_ANSIBLE)
    assert result == to_text(uuid.uuid5(UUID_NAMESPACE_ANSIBLE, to_native('test_string', errors='surrogate_or_strict')))

def test_to_uuid_invalid_namespace():
    with pytest.raises(AnsibleFilterError) as excinfo:
        to_uuid('test_string', 'invalid_namespace')
    assert "Invalid value 'invalid_namespace' for 'namespace'" in str(excinfo.value)

def test_to_uuid_default_namespace():
    result = to_uuid('test_string')
    assert result == to_text(uuid.uuid5(UUID_NAMESPACE_ANSIBLE, to_native('test_string', errors='surrogate_or_strict')))
