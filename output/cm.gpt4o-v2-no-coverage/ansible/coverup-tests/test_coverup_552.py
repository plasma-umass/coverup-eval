# file: lib/ansible/playbook/role_include.py:168-177
# asked: {"lines": [168, 170, 171, 172, 173, 174, 175, 177], "branches": []}
# gained: {"lines": [168, 170, 171, 172, 173, 174, 175, 177], "branches": []}

import pytest
from ansible.playbook.role_include import IncludeRole
from unittest.mock import MagicMock

@pytest.fixture
def include_role_instance():
    instance = IncludeRole()
    instance.statically_loaded = MagicMock()
    instance._from_files = MagicMock()
    instance._from_files.copy = MagicMock(return_value=MagicMock())
    instance._parent_role = MagicMock()
    instance._role_name = MagicMock()
    instance._role_path = MagicMock()
    return instance

def test_include_role_copy(include_role_instance):
    new_instance = include_role_instance.copy()

    assert new_instance.statically_loaded == include_role_instance.statically_loaded
    assert new_instance._from_files == include_role_instance._from_files.copy()
    assert new_instance._parent_role == include_role_instance._parent_role
    assert new_instance._role_name == include_role_instance._role_name
    assert new_instance._role_path == include_role_instance._role_path
