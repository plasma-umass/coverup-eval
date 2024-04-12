# file lib/ansible/plugins/filter/core.py:279-287
# lines [279, 280, 281, 282, 283, 284, 285, 287]
# branches ['281->282', '281->287']

import pytest
import uuid
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import to_uuid

def test_to_uuid_with_invalid_namespace(mocker):
    invalid_namespace = 'not-a-valid-uuid'
    with pytest.raises(AnsibleFilterError) as excinfo:
        to_uuid('test_string', namespace=invalid_namespace)
    assert "Invalid value" in str(excinfo.value)

def test_to_uuid_with_valid_namespace():
    valid_namespace = '6ba7b810-9dad-11d1-80b4-00c04fd430c8'
    result = to_uuid('test_string', namespace=valid_namespace)
    assert isinstance(result, str)
    assert uuid.UUID(result)  # This will raise a ValueError if result is not a valid UUID

def test_to_uuid_with_uuid_object_namespace():
    uuid_namespace = uuid.uuid4()
    result = to_uuid('test_string', namespace=uuid_namespace)
    assert isinstance(result, str)
    assert uuid.UUID(result)  # This will raise a ValueError if result is not a valid UUID
