# file lib/ansible/plugins/action/include_vars.py:153-173
# lines [153, 154, 155, 156, 157, 159, 160, 162, 163, 164, 167, 169, 170, 171, 173]
# branches ['154->155', '154->169', '155->156', '155->162', '159->exit', '159->160', '169->exit', '169->170']

import os
from unittest.mock import MagicMock
from ansible.plugins.action import include_vars
from ansible.utils.path import unfrackpath
import pytest

# Mock the necessary components to test ActionModule._set_root_dir
class MockTask:
    def __init__(self, role=None, data_source=None):
        self._role = role
        self._ds = MagicMock(_data_source=data_source)

class MockRole:
    def __init__(self, role_path):
        self._role_path = role_path

@pytest.fixture
def action_module(mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('ansible.plugins.action.include_vars.ActionBase._execute_module')
    action_module = include_vars.ActionModule(task={}, connection=mocker.MagicMock(), play_context=None, loader=None, templar=None, shared_loader_obj=None)
    return action_module

def test_set_root_dir_with_role_and_vars_in_source_dir(action_module, tmp_path, mocker):
    role_path = tmp_path / "roles" / "testrole"
    role_path.mkdir(parents=True)
    source_dir = "vars/somefile.yml"
    role = MockRole(str(role_path))
    task = MockTask(role=role)
    action_module._task = task
    action_module.source_dir = source_dir

    action_module._set_root_dir()

    expected_path = os.path.join(str(role_path), source_dir)
    assert action_module.source_dir == expected_path

def test_set_root_dir_with_role_and_no_vars_in_source_dir(action_module, tmp_path, mocker):
    role_path = tmp_path / "roles" / "testrole"
    role_path.mkdir(parents=True)
    source_dir = "somefile.yml"
    role = MockRole(str(role_path))
    task = MockTask(role=role)
    action_module._task = task
    action_module.source_dir = source_dir

    action_module._set_root_dir()

    expected_path = os.path.join(str(role_path), 'vars', source_dir)
    assert action_module.source_dir == expected_path

def test_set_root_dir_without_role_but_with_data_source(action_module, tmp_path, mocker):
    data_source = tmp_path / "some" / "path" / "vars_file.yml"
    data_source.parent.mkdir(parents=True)
    source_dir = "somefile.yml"
    task = MockTask(data_source=str(data_source))
    action_module._task = task
    action_module.source_dir = source_dir

    action_module._set_root_dir()

    expected_path = os.path.join(str(data_source.parent), source_dir)
    assert action_module.source_dir == expected_path
