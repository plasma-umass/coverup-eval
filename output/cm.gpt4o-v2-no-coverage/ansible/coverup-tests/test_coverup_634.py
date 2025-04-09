# file: lib/ansible/playbook/role/definition.py:237-240
# asked: {"lines": [237, 238, 239, 240], "branches": [[238, 239], [238, 240]]}
# gained: {"lines": [237, 238, 239, 240], "branches": [[238, 239], [238, 240]]}

import pytest
from ansible.playbook.role.definition import RoleDefinition

@pytest.fixture
def role_definition():
    return RoleDefinition()

def test_get_name_with_fqcn(role_definition, mocker):
    mocker.patch.object(role_definition, '_role_collection', 'collection')
    mocker.patch.object(role_definition, 'role', 'role_name')
    assert role_definition.get_name(include_role_fqcn=True) == 'collection.role_name'

def test_get_name_without_fqcn(role_definition, mocker):
    mocker.patch.object(role_definition, 'role', 'role_name')
    assert role_definition.get_name(include_role_fqcn=False) == 'role_name'

def test_get_name_with_fqcn_no_collection(role_definition, mocker):
    mocker.patch.object(role_definition, '_role_collection', None)
    mocker.patch.object(role_definition, 'role', 'role_name')
    assert role_definition.get_name(include_role_fqcn=True) == 'role_name'

def test_get_name_with_fqcn_no_role(role_definition, mocker):
    mocker.patch.object(role_definition, '_role_collection', 'collection')
    mocker.patch.object(role_definition, 'role', None)
    assert role_definition.get_name(include_role_fqcn=True) == 'collection'
