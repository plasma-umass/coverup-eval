# file lib/ansible/playbook/role/definition.py:65-67
# lines [65, 66, 67]
# branches []

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.role.definition import RoleDefinition

def test_role_definition_load_not_implemented():
    with pytest.raises(AnsibleError) as excinfo:
        RoleDefinition.load(data={})
    assert "not implemented" in str(excinfo.value)
