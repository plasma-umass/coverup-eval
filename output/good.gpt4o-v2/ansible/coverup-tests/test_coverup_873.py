# file: lib/ansible/playbook/role_include.py:68-70
# asked: {"lines": [68, 70], "branches": []}
# gained: {"lines": [68, 70], "branches": []}

import pytest
from ansible.playbook.role_include import IncludeRole

@pytest.fixture
def include_role_instance():
    return IncludeRole()

def test_get_name_with_name(include_role_instance, mocker):
    mocker.patch.object(include_role_instance, 'name', 'test_name')
    assert include_role_instance.get_name() == 'test_name'

def test_get_name_without_name(include_role_instance, mocker):
    mocker.patch.object(include_role_instance, 'name', None)
    mocker.patch.object(include_role_instance, 'action', 'test_action', create=True)
    mocker.patch.object(include_role_instance, '_role_name', 'test_role_name', create=True)
    assert include_role_instance.get_name() == 'test_action : test_role_name'
