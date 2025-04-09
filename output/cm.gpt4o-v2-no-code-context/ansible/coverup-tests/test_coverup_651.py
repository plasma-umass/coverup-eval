# file: lib/ansible/playbook/task_include.py:49-51
# asked: {"lines": [49, 50, 51], "branches": []}
# gained: {"lines": [49, 50, 51], "branches": []}

import pytest
from ansible.playbook.task_include import TaskInclude

def test_task_include_init(mocker):
    block = mocker.Mock()
    role = mocker.Mock()
    task_include = mocker.Mock()
    
    task_include_instance = TaskInclude(block=block, role=role, task_include=task_include)
    
    assert task_include_instance.statically_loaded is False
