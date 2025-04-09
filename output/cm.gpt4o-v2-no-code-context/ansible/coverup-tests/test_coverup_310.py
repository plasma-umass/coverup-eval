# file: lib/ansible/playbook/block.py:134-147
# asked: {"lines": [134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 146, 147], "branches": []}
# gained: {"lines": [134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 146, 147], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.playbook.block import Block
from ansible.errors import AnsibleParserError

@pytest.fixture
def block_instance():
    play = MagicMock()
    role = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    use_handlers = MagicMock()
    ds = MagicMock()
    block = Block()
    block._play = play
    block._role = role
    block._variable_manager = variable_manager
    block._loader = loader
    block._use_handlers = use_handlers
    block._ds = ds
    return block

def test_load_rescue_success(block_instance):
    ds = MagicMock()
    with patch('ansible.playbook.block.load_list_of_tasks', return_value='expected_result') as mock_load_list_of_tasks:
        result = block_instance._load_rescue('rescue', ds)
        mock_load_list_of_tasks.assert_called_once_with(
            ds,
            play=block_instance._play,
            block=block_instance,
            role=block_instance._role,
            task_include=None,
            variable_manager=block_instance._variable_manager,
            loader=block_instance._loader,
            use_handlers=block_instance._use_handlers,
        )
        assert result == 'expected_result'

def test_load_rescue_failure(block_instance):
    ds = MagicMock()
    with patch('ansible.playbook.block.load_list_of_tasks', side_effect=AssertionError('test error')) as mock_load_list_of_tasks:
        with pytest.raises(AnsibleParserError) as excinfo:
            block_instance._load_rescue('rescue', ds)
        assert str(excinfo.value) == "A malformed block was encountered while loading rescue.. test error"
        assert excinfo.value.obj == block_instance._ds
        assert isinstance(excinfo.value.orig_exc, AssertionError)
        mock_load_list_of_tasks.assert_called_once_with(
            ds,
            play=block_instance._play,
            block=block_instance,
            role=block_instance._role,
            task_include=None,
            variable_manager=block_instance._variable_manager,
            loader=block_instance._loader,
            use_handlers=block_instance._use_handlers,
        )
