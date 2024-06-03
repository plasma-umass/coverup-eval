# file lib/ansible/playbook/block.py:134-147
# lines [134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 146, 147]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.block import Block
from ansible.errors import AnsibleParserError

@pytest.fixture
def mock_load_list_of_tasks(mocker):
    return mocker.patch('ansible.playbook.block.load_list_of_tasks')

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

def test_load_rescue_success(block_instance, mock_load_list_of_tasks):
    mock_load_list_of_tasks.return_value = 'expected_result'
    ds = {'some': 'data'}
    result = block_instance._load_rescue('attr', ds)
    assert result == 'expected_result'

def test_load_rescue_failure(block_instance, mock_load_list_of_tasks):
    mock_load_list_of_tasks.side_effect = AssertionError('test error')
    ds = {'some': 'data'}
    with pytest.raises(AnsibleParserError) as excinfo:
        block_instance._load_rescue('attr', ds)
    assert 'A malformed block was encountered while loading rescue.' in str(excinfo.value)
