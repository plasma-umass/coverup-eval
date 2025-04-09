# file: lib/ansible/playbook/task_include.py:53-61
# asked: {"lines": [53, 54, 55, 56, 57, 58, 61], "branches": []}
# gained: {"lines": [53, 54, 55, 56, 57, 58, 61], "branches": []}

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.block import Block
from ansible.playbook.role import Role
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def mock_task_include(mocker):
    mocker.patch('ansible.playbook.task_include.TaskInclude.check_options', return_value='mock_task')
    mocker.patch('ansible.playbook.task_include.TaskInclude.load_data', return_value='mock_data')

def test_task_include_load_with_all_params(mock_task_include):
    block = Block()
    role = Role()
    task_include = TaskInclude()
    variable_manager = VariableManager()
    loader = DataLoader()
    data = {'some': 'data'}

    task = TaskInclude.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)
    
    assert task == 'mock_task'

def test_task_include_load_with_minimal_params(mock_task_include):
    data = {'some': 'data'}

    task = TaskInclude.load(data)
    
    assert task == 'mock_task'
