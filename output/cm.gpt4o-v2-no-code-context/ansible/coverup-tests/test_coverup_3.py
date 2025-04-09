# file: lib/ansible/playbook/helpers.py:84-320
# asked: {"lines": [84, 91, 92, 93, 94, 95, 96, 97, 99, 100, 102, 103, 104, 105, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 118, 120, 121, 122, 123, 126, 127, 129, 131, 133, 134, 136, 138, 139, 140, 141, 142, 143, 144, 147, 148, 153, 154, 155, 156, 158, 159, 161, 162, 163, 164, 166, 169, 173, 174, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 191, 192, 193, 194, 196, 197, 198, 199, 200, 201, 202, 203, 204, 206, 208, 209, 210, 212, 214, 215, 216, 217, 218, 219, 222, 223, 224, 225, 226, 227, 229, 231, 232, 233, 234, 235, 236, 242, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 257, 260, 261, 266, 267, 268, 270, 272, 273, 275, 276, 277, 278, 279, 280, 281, 282, 287, 288, 289, 291, 292, 293, 294, 296, 299, 302, 303, 304, 307, 308, 311, 313, 314, 316, 318, 320], "branches": [[99, 100], [99, 102], [103, 104], [103, 320], [104, 105], [104, 107], [107, 108], [107, 120], [126, 127], [126, 129], [131, 133], [131, 275], [133, 134], [133, 136], [153, 154], [153, 155], [155, 156], [155, 158], [161, 162], [161, 272], [162, 163], [162, 169], [163, 164], [163, 166], [178, 179], [178, 180], [180, 181], [180, 214], [181, 182], [181, 184], [187, 188], [187, 196], [197, 198], [197, 199], [199, 200], [199, 201], [202, 203], [202, 206], [208, 209], [208, 212], [214, 215], [214, 231], [226, 227], [226, 229], [232, 233], [232, 235], [235, 236], [235, 242], [260, 261], [260, 266], [266, 267], [266, 270], [267, 103], [267, 268], [275, 276], [275, 313], [288, 289], [288, 291], [291, 292], [291, 311], [292, 293], [292, 299], [293, 294], [293, 296], [313, 314], [313, 316]]}
# gained: {"lines": [84, 91, 92, 93, 94, 95, 96, 97, 99, 100, 102, 103, 104, 105, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 118, 120, 121, 122, 131, 133, 134, 136, 138, 139, 140, 141, 142, 143, 144, 147, 148, 153, 155, 158, 159, 161, 272, 273, 275, 276, 277, 278, 279, 280, 281, 282, 287, 288, 291, 311, 313, 314, 316, 318, 320], "branches": [[99, 100], [99, 102], [103, 104], [103, 320], [104, 105], [104, 107], [107, 108], [107, 120], [131, 133], [131, 275], [133, 134], [133, 136], [153, 155], [155, 158], [161, 272], [275, 276], [275, 313], [288, 291], [291, 311], [313, 314], [313, 316]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.playbook.helpers import load_list_of_tasks
from ansible.errors import AnsibleAssertionError, AnsibleParserError
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.template import Templar

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_variable_manager():
    return MagicMock()

@pytest.fixture
def mock_play():
    return MagicMock()

@pytest.fixture
def mock_block():
    return MagicMock()

@pytest.fixture
def mock_role():
    return MagicMock()

@pytest.fixture
def mock_task_include():
    return MagicMock()

def test_load_list_of_tasks_invalid_ds_type():
    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks("not_a_list", None)

def test_load_list_of_tasks_invalid_task_ds_type():
    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks([1, 2, 3], None)

def test_load_list_of_tasks_block(mock_loader, mock_variable_manager, mock_play, mock_block, mock_role, mock_task_include):
    ds = [{'block': 'some_block'}]
    with patch('ansible.playbook.block.Block.load', return_value=MagicMock()) as mock_block_load:
        result = load_list_of_tasks(ds, mock_play, block=mock_block, role=mock_role, task_include=mock_task_include, variable_manager=mock_variable_manager, loader=mock_loader)
        assert len(result) == 1
        mock_block_load.assert_called_once()

def test_load_list_of_tasks_task_include(mock_loader, mock_variable_manager, mock_play, mock_block, mock_role, mock_task_include):
    ds = [{'include': 'some_include'}]
    with patch('ansible.playbook.task_include.TaskInclude.load', return_value=MagicMock()) as mock_task_include_load:
        with patch('ansible.parsing.mod_args.ModuleArgsParser.parse', return_value=('include', {}, None)):
            result = load_list_of_tasks(ds, mock_play, block=mock_block, role=mock_role, task_include=mock_task_include, variable_manager=mock_variable_manager, loader=mock_loader)
            assert len(result) == 1
            mock_task_include_load.assert_called_once()

def test_load_list_of_tasks_handler_task_include(mock_loader, mock_variable_manager, mock_play, mock_block, mock_role, mock_task_include):
    ds = [{'include': 'some_include'}]
    with patch('ansible.playbook.handler_task_include.HandlerTaskInclude.load', return_value=MagicMock()) as mock_handler_task_include_load:
        with patch('ansible.parsing.mod_args.ModuleArgsParser.parse', return_value=('include', {}, None)):
            result = load_list_of_tasks(ds, mock_play, block=mock_block, role=mock_role, task_include=mock_task_include, use_handlers=True, variable_manager=mock_variable_manager, loader=mock_loader)
            assert len(result) == 1
            mock_handler_task_include_load.assert_called_once()

def test_load_list_of_tasks_include_role(mock_loader, mock_variable_manager, mock_play, mock_block, mock_role, mock_task_include):
    ds = [{'include_role': 'some_role'}]
    with patch('ansible.playbook.role_include.IncludeRole.load', return_value=MagicMock()) as mock_include_role_load:
        with patch('ansible.parsing.mod_args.ModuleArgsParser.parse', return_value=('include_role', {}, None)):
            result = load_list_of_tasks(ds, mock_play, block=mock_block, role=mock_role, task_include=mock_task_include, variable_manager=mock_variable_manager, loader=mock_loader)
            assert len(result) == 1
            mock_include_role_load.assert_called_once()

def test_load_list_of_tasks_handler(mock_loader, mock_variable_manager, mock_play, mock_block, mock_role, mock_task_include):
    ds = [{'name': 'some_handler'}]
    with patch('ansible.playbook.handler.Handler.load', return_value=MagicMock()) as mock_handler_load:
        with patch('ansible.parsing.mod_args.ModuleArgsParser.parse', return_value=('handler', {}, None)):
            result = load_list_of_tasks(ds, mock_play, block=mock_block, role=mock_role, task_include=mock_task_include, use_handlers=True, variable_manager=mock_variable_manager, loader=mock_loader)
            assert len(result) == 1
            mock_handler_load.assert_called_once()

def test_load_list_of_tasks_task(mock_loader, mock_variable_manager, mock_play, mock_block, mock_role, mock_task_include):
    ds = [{'name': 'some_task'}]
    with patch('ansible.playbook.task.Task.load', return_value=MagicMock()) as mock_task_load:
        with patch('ansible.parsing.mod_args.ModuleArgsParser.parse', return_value=('task', {}, None)):
            result = load_list_of_tasks(ds, mock_play, block=mock_block, role=mock_role, task_include=mock_task_include, variable_manager=mock_variable_manager, loader=mock_loader)
            assert len(result) == 1
            mock_task_load.assert_called_once()
