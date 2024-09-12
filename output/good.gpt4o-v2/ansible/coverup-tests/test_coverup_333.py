# file: lib/ansible/playbook/block.py:134-147
# asked: {"lines": [134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 146, 147], "branches": []}
# gained: {"lines": [134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 146, 147], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.block import Block
from ansible.errors import AnsibleParserError

@pytest.fixture
def block_instance():
    block = Block()
    block._play = MagicMock()
    block._role = MagicMock()
    block._variable_manager = MagicMock()
    block._loader = MagicMock()
    block._use_handlers = MagicMock()
    block._ds = MagicMock()
    return block

def test_load_rescue_success(block_instance):
    with patch('ansible.playbook.block.load_list_of_tasks', return_value='success') as mock_load:
        result = block_instance._load_rescue('attr', 'ds')
        assert result == 'success'
        mock_load.assert_called_once_with(
            'ds',
            play=block_instance._play,
            block=block_instance,
            role=block_instance._role,
            task_include=None,
            variable_manager=block_instance._variable_manager,
            loader=block_instance._loader,
            use_handlers=block_instance._use_handlers
        )

def test_load_rescue_failure(block_instance):
    with patch('ansible.playbook.block.load_list_of_tasks', side_effect=AssertionError('error')) as mock_load:
        with pytest.raises(AnsibleParserError) as excinfo:
            block_instance._load_rescue('attr', 'ds')
        assert "A malformed block was encountered while loading rescue." in str(excinfo.value)
        assert excinfo.value.obj == block_instance._ds
        assert isinstance(excinfo.value.orig_exc, AssertionError)
        mock_load.assert_called_once_with(
            'ds',
            play=block_instance._play,
            block=block_instance,
            role=block_instance._role,
            task_include=None,
            variable_manager=block_instance._variable_manager,
            loader=block_instance._loader,
            use_handlers=block_instance._use_handlers
        )
