# file: lib/ansible/playbook/block.py:149-162
# asked: {"lines": [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 161, 162], "branches": []}
# gained: {"lines": [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 161, 162], "branches": []}

import pytest
from ansible.playbook.block import Block
from ansible.errors import AnsibleParserError
from unittest.mock import Mock, patch

@pytest.fixture
def block_instance():
    block = Block()
    block._play = Mock()
    block._role = Mock()
    block._variable_manager = Mock()
    block._loader = Mock()
    block._use_handlers = Mock()
    block._ds = Mock()
    return block

def test_load_always_success(block_instance):
    ds = [{'name': 'test_task'}]
    attr = 'always'
    
    with patch('ansible.playbook.block.load_list_of_tasks', return_value=ds) as mock_load:
        result = block_instance._load_always(attr, ds)
        mock_load.assert_called_once_with(
            ds,
            play=block_instance._play,
            block=block_instance,
            role=block_instance._role,
            task_include=None,
            variable_manager=block_instance._variable_manager,
            loader=block_instance._loader,
            use_handlers=block_instance._use_handlers
        )
        assert result == ds

def test_load_always_failure(block_instance):
    ds = [{'name': 'test_task'}]
    attr = 'always'
    
    with patch('ansible.playbook.block.load_list_of_tasks', side_effect=AssertionError) as mock_load:
        with pytest.raises(AnsibleParserError) as excinfo:
            block_instance._load_always(attr, ds)
        assert "A malformed block was encountered while loading always" in str(excinfo.value)
        mock_load.assert_called_once_with(
            ds,
            play=block_instance._play,
            block=block_instance,
            role=block_instance._role,
            task_include=None,
            variable_manager=block_instance._variable_manager,
            loader=block_instance._loader,
            use_handlers=block_instance._use_handlers
        )
