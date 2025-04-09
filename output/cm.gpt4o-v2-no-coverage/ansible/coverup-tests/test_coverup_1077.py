# file: lib/ansible/playbook/helpers.py:84-320
# asked: {"lines": [100, 105, 108, 109, 110, 111, 112, 113, 114, 115, 116, 118, 123, 126, 127, 129, 133, 134, 136, 138, 139, 140, 141, 142, 143, 144, 147, 148, 153, 154, 155, 156, 158, 159, 161, 162, 163, 164, 166, 169, 173, 174, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 191, 192, 193, 194, 196, 197, 198, 199, 200, 201, 202, 203, 204, 206, 208, 209, 210, 212, 214, 215, 216, 217, 218, 219, 222, 223, 224, 225, 226, 227, 229, 231, 232, 233, 234, 235, 236, 242, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 257, 260, 261, 266, 267, 268, 270, 272, 273, 276, 277, 278, 279, 280, 281, 282, 287, 288, 289, 291, 292, 293, 294, 296, 299, 302, 303, 304, 307, 308, 311, 314], "branches": [[99, 100], [104, 105], [107, 108], [126, 127], [126, 129], [131, 133], [133, 134], [133, 136], [153, 154], [153, 155], [155, 156], [155, 158], [161, 162], [161, 272], [162, 163], [162, 169], [163, 164], [163, 166], [178, 179], [178, 180], [180, 181], [180, 214], [181, 182], [181, 184], [187, 188], [187, 196], [197, 198], [197, 199], [199, 200], [199, 201], [202, 203], [202, 206], [208, 209], [208, 212], [214, 215], [214, 231], [226, 227], [226, 229], [232, 233], [232, 235], [235, 236], [235, 242], [260, 261], [260, 266], [266, 267], [266, 270], [267, 103], [267, 268], [275, 276], [288, 289], [288, 291], [291, 292], [291, 311], [292, 293], [292, 299], [293, 294], [293, 296], [313, 314]]}
# gained: {"lines": [100, 105, 108, 109, 110, 111, 112, 113, 114, 115, 116, 118, 133, 136, 138, 139, 140, 141, 142, 143, 144, 147, 148, 153, 155, 158, 159, 161, 272, 273, 276, 277, 278, 279, 280, 281, 282, 287, 288, 291, 311, 314], "branches": [[99, 100], [104, 105], [107, 108], [131, 133], [133, 136], [153, 155], [155, 158], [161, 272], [275, 276], [288, 291], [291, 311], [313, 314]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleParserError, AnsibleUndefinedVariable, AnsibleAssertionError
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

def test_load_list_of_tasks_with_non_list_ds():
    from ansible.playbook.helpers import load_list_of_tasks
    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks("not_a_list", None)

def test_load_list_of_tasks_with_non_dict_task_ds(mock_play, mock_loader, mock_variable_manager):
    from ansible.playbook.helpers import load_list_of_tasks
    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks(["not_a_dict"], mock_play, loader=mock_loader, variable_manager=mock_variable_manager)

def test_load_list_of_tasks_with_block(mock_play, mock_loader, mock_variable_manager):
    from ansible.playbook.helpers import load_list_of_tasks
    task_ds = {'block': []}
    with patch.object(Block, 'load', return_value="block_loaded") as mock_block_load:
        result = load_list_of_tasks([task_ds], mock_play, loader=mock_loader, variable_manager=mock_variable_manager)
        assert result == ["block_loaded"]
        mock_block_load.assert_called_once()

def test_load_list_of_tasks_with_task_include(mock_play, mock_loader, mock_variable_manager):
    from ansible.playbook.helpers import load_list_of_tasks
    task_ds = {'include': 'some_task'}
    with patch.object(ModuleArgsParser, 'parse', return_value=('include', {}, None)):
        with patch.object(TaskInclude, 'load', return_value=MagicMock(statically_loaded=True, args={'_raw_params': 'some_task'})) as mock_task_include_load:
            with patch.object(Templar, 'template', return_value='some_task'):
                with patch('os.path.exists', return_value=True):
                    with patch('ansible.playbook.helpers.load_list_of_blocks', return_value=[MagicMock()]):
                        result = load_list_of_tasks([task_ds], mock_play, loader=mock_loader, variable_manager=mock_variable_manager)
                        assert len(result) == 1
                        assert isinstance(result[0], MagicMock)
                        mock_task_include_load.assert_called_once()

def test_load_list_of_tasks_with_handler(mock_play, mock_loader, mock_variable_manager):
    from ansible.playbook.helpers import load_list_of_tasks
    task_ds = {'action': 'some_action'}
    with patch.object(ModuleArgsParser, 'parse', return_value=('some_action', {}, None)):
        with patch.object(Handler, 'load', return_value="handler_loaded") as mock_handler_load:
            result = load_list_of_tasks([task_ds], mock_play, loader=mock_loader, variable_manager=mock_variable_manager, use_handlers=True)
            assert result == ["handler_loaded"]
            mock_handler_load.assert_called_once()

def test_load_list_of_tasks_with_task(mock_play, mock_loader, mock_variable_manager):
    from ansible.playbook.helpers import load_list_of_tasks
    task_ds = {'action': 'some_action'}
    with patch.object(ModuleArgsParser, 'parse', return_value=('some_action', {}, None)):
        with patch.object(Task, 'load', return_value="task_loaded") as mock_task_load:
            result = load_list_of_tasks([task_ds], mock_play, loader=mock_loader, variable_manager=mock_variable_manager)
            assert result == ["task_loaded"]
            mock_task_load.assert_called_once()

def test_load_list_of_tasks_with_include_role(mock_play, mock_loader, mock_variable_manager):
    from ansible.playbook.helpers import load_list_of_tasks
    task_ds = {'include_role': 'some_role'}
    with patch.object(ModuleArgsParser, 'parse', return_value=('include_role', {}, None)):
        with patch.object(IncludeRole, 'load', return_value=MagicMock(statically_loaded=True, args={'_raw_params': 'some_role'})) as mock_include_role_load:
            with patch.object(Templar, 'template', return_value='some_role'):
                with patch('os.path.exists', return_value=True):
                    with patch('ansible.playbook.helpers.load_list_of_blocks', return_value=[MagicMock()]):
                        result = load_list_of_tasks([task_ds], mock_play, loader=mock_loader, variable_manager=mock_variable_manager)
                        assert len(result) == 1
                        assert isinstance(result[0], MagicMock)
                        mock_include_role_load.assert_called_once()
