# file: lib/ansible/playbook/helpers.py:84-320
# asked: {"lines": [123, 126, 127, 129, 154, 156, 162, 163, 164, 166, 169, 173, 174, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 191, 192, 193, 194, 196, 197, 198, 199, 200, 201, 202, 203, 204, 206, 208, 209, 210, 212, 214, 215, 216, 217, 218, 219, 222, 223, 224, 225, 226, 227, 229, 231, 232, 233, 234, 235, 236, 242, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 257, 260, 261, 266, 267, 268, 270, 289, 292, 293, 294, 296, 299, 302, 303, 304, 307, 308], "branches": [[126, 127], [126, 129], [153, 154], [155, 156], [161, 162], [162, 163], [162, 169], [163, 164], [163, 166], [178, 179], [178, 180], [180, 181], [180, 214], [181, 182], [181, 184], [187, 188], [187, 196], [197, 198], [197, 199], [199, 200], [199, 201], [202, 203], [202, 206], [208, 209], [208, 212], [214, 215], [214, 231], [226, 227], [226, 229], [232, 233], [232, 235], [235, 236], [235, 242], [260, 261], [260, 266], [266, 267], [266, 270], [267, 103], [267, 268], [288, 289], [291, 292], [292, 293], [292, 299], [293, 294], [293, 296]]}
# gained: {"lines": [123, 126, 127, 129, 154, 156, 162, 163, 164, 289, 292, 293, 294], "branches": [[126, 127], [126, 129], [153, 154], [155, 156], [161, 162], [162, 163], [163, 164], [288, 289], [291, 292], [292, 293], [293, 294]]}

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.helpers import load_list_of_tasks
from ansible.errors import AnsibleAssertionError, AnsibleParserError
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.template import Templar
from ansible.playbook.block import Block
from ansible.playbook.handler import Handler
from ansible.playbook.task import Task
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.role_include import IncludeRole
from ansible.playbook.handler_task_include import HandlerTaskInclude

@pytest.fixture
def mock_loader():
    loader = Mock()
    loader.get_basedir.return_value = '/basedir'
    return loader

@pytest.fixture
def mock_variable_manager():
    variable_manager = Mock()
    variable_manager.get_vars.return_value = {}
    return variable_manager

@pytest.fixture
def mock_play():
    return Mock()

@pytest.fixture
def mock_block():
    return Mock()

@pytest.fixture
def mock_role():
    role = Mock()
    role._role_path = '/role_path'
    return role

@pytest.fixture
def mock_task_include():
    return Mock()

def test_load_list_of_tasks_invalid_ds_type():
    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks("not_a_list", None)

def test_load_list_of_tasks_invalid_task_ds_type():
    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks([1, 2, 3], None)

def test_load_list_of_tasks_ansible_parser_error(mock_loader, mock_variable_manager, mock_play):
    task_ds = {'invalid': 'task'}
    ds = [task_ds]
    with patch.object(ModuleArgsParser, 'parse', side_effect=AnsibleParserError("error")):
        with pytest.raises(AnsibleParserError):
            load_list_of_tasks(ds, mock_play, loader=mock_loader, variable_manager=mock_variable_manager)

def test_load_list_of_tasks_ansible_parser_error_with_obj(mock_loader, mock_variable_manager, mock_play):
    task_ds = {'invalid': 'task'}
    ds = [task_ds]
    error = AnsibleParserError("error")
    error.obj = task_ds
    with patch.object(ModuleArgsParser, 'parse', side_effect=error):
        with pytest.raises(AnsibleParserError):
            load_list_of_tasks(ds, mock_play, loader=mock_loader, variable_manager=mock_variable_manager)

def test_load_list_of_tasks_include_tasks_static(mock_loader, mock_variable_manager, mock_play, mock_block, mock_role):
    task_ds = {'include_tasks': 'some_tasks.yml'}
    ds = [task_ds]
    with patch.object(ModuleArgsParser, 'parse', return_value=('include_tasks', {}, None)):
        with patch.object(Templar, 'is_template', return_value=False):
            with patch.object(TaskInclude, 'load', return_value=Mock(loop=None, args={'_raw_params': 'some_tasks.yml'}, all_parents_static=lambda: True)):
                with patch.object(mock_loader, 'path_dwim_relative', return_value='/path/to/some_tasks.yml'):
                    with patch('os.path.exists', return_value=True):
                        with patch.object(mock_loader, 'load_from_file', return_value=[{'name': 'task1'}]):
                            tasks = load_list_of_tasks(ds, mock_play, block=mock_block, role=mock_role, loader=mock_loader, variable_manager=mock_variable_manager)
                            assert len(tasks) == 1

def test_load_list_of_tasks_include_tasks_dynamic(mock_loader, mock_variable_manager, mock_play, mock_block, mock_role):
    task_ds = {'include_tasks': 'some_tasks.yml'}
    ds = [task_ds]
    with patch.object(ModuleArgsParser, 'parse', return_value=('include_tasks', {}, None)):
        with patch.object(Templar, 'is_template', return_value=True):
            with patch.object(TaskInclude, 'load', return_value=Mock(loop=None, args={'_raw_params': 'some_tasks.yml'}, all_parents_static=lambda: True)):
                tasks = load_list_of_tasks(ds, mock_play, block=mock_block, role=mock_role, loader=mock_loader, variable_manager=mock_variable_manager)
                assert len(tasks) == 1

def test_load_list_of_tasks_import_tasks_with_loop(mock_loader, mock_variable_manager, mock_play, mock_block, mock_role):
    task_ds = {'import_tasks': 'some_tasks.yml'}
    ds = [task_ds]
    with patch.object(ModuleArgsParser, 'parse', return_value=('import_tasks', {}, None)):
        with patch.object(TaskInclude, 'load', return_value=Mock(loop=True, args={'_raw_params': 'some_tasks.yml'}, all_parents_static=lambda: True)):
            with pytest.raises(AnsibleParserError):
                load_list_of_tasks(ds, mock_play, block=mock_block, role=mock_role, loader=mock_loader, variable_manager=mock_variable_manager)

def test_load_list_of_tasks_import_role_with_loop(mock_loader, mock_variable_manager, mock_play, mock_block, mock_role):
    task_ds = {'import_role': 'some_role'}
    ds = [task_ds]
    with patch.object(ModuleArgsParser, 'parse', return_value=('import_role', {}, None)):
        with patch.object(IncludeRole, 'load', return_value=Mock(loop=True, args={'_raw_params': 'some_role'}, all_parents_static=lambda: True)):
            with pytest.raises(AnsibleParserError):
                load_list_of_tasks(ds, mock_play, block=mock_block, role=mock_role, loader=mock_loader, variable_manager=mock_variable_manager)

def test_load_list_of_tasks_include_role_static(mock_loader, mock_variable_manager, mock_play, mock_block, mock_role):
    task_ds = {'include_role': 'some_role'}
    ds = [task_ds]
    with patch.object(ModuleArgsParser, 'parse', return_value=('include_role', {}, None)):
        with patch.object(IncludeRole, 'load', return_value=Mock(loop=None, args={'_raw_params': 'some_role'}, all_parents_static=lambda: True)):
            tasks = load_list_of_tasks(ds, mock_play, block=mock_block, role=mock_role, loader=mock_loader, variable_manager=mock_variable_manager)
            assert len(tasks) == 1

def test_load_list_of_tasks_include_role_dynamic(mock_loader, mock_variable_manager, mock_play, mock_block, mock_role):
    task_ds = {'include_role': 'some_role'}
    ds = [task_ds]
    with patch.object(ModuleArgsParser, 'parse', return_value=('include_role', {}, None)):
        with patch.object(IncludeRole, 'load', return_value=Mock(loop=None, args={'_raw_params': 'some_role'}, all_parents_static=lambda: True)):
            tasks = load_list_of_tasks(ds, mock_play, block=mock_block, role=mock_role, loader=mock_loader, variable_manager=mock_variable_manager)
            assert len(tasks) == 1
