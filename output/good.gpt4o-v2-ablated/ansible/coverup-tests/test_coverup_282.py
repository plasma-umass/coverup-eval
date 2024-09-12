# file: lib/ansible/playbook/role/definition.py:65-67
# asked: {"lines": [65, 66, 67], "branches": []}
# gained: {"lines": [65, 66, 67], "branches": []}

import pytest
from ansible.playbook.role.definition import RoleDefinition
from ansible.errors import AnsibleError

def test_role_definition_load():
    with pytest.raises(AnsibleError, match="not implemented"):
        RoleDefinition.load(data={})
