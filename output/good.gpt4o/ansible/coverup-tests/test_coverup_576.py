# file lib/ansible/playbook/role_include.py:59-66
# lines [59, 61, 63, 64, 65, 66]
# branches []

import pytest
from ansible.playbook.role_include import IncludeRole

def test_include_role_initialization():
    block = "test_block"
    role = "test_role"
    task_include = "test_task_include"
    
    include_role = IncludeRole(block=block, role=role, task_include=task_include)
    
    assert include_role._from_files == {}
    assert include_role._parent_role == role
    assert include_role._role_name is None
    assert include_role._role_path is None
