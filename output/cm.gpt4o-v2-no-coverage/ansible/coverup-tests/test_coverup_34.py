# file: lib/ansible/playbook/helpers.py:33-81
# asked: {"lines": [33, 41, 43, 44, 46, 47, 48, 49, 50, 54, 55, 56, 57, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 81], "branches": [[43, 44], [43, 46], [47, 48], [47, 81], [49, 50], [49, 81], [55, 56], [55, 66], [66, 49], [66, 67], [67, 66], [67, 68]]}
# gained: {"lines": [33, 41, 43, 44, 46, 47, 48, 49, 50, 54, 55, 56, 57, 59, 60, 61, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 81], "branches": [[43, 44], [43, 46], [47, 48], [47, 81], [49, 50], [49, 81], [55, 56], [55, 66], [66, 49], [66, 67], [67, 66], [67, 68]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleAssertionError
from ansible.playbook.helpers import load_list_of_blocks
from ansible.playbook.block import Block

@pytest.fixture
def mock_block(mocker):
    mock_block = mocker.patch('ansible.playbook.block.Block')
    mock_block.is_block.side_effect = lambda ds: isinstance(ds, dict) and any(k in ds for k in ('block', 'rescue', 'always'))
    mock_block.load.side_effect = lambda data, play, parent_block, role, task_include, use_handlers, variable_manager, loader: MagicMock()
    return mock_block

def test_load_list_of_blocks_with_none():
    result = load_list_of_blocks(None, play=None)
    assert result == []

def test_load_list_of_blocks_with_empty_list():
    result = load_list_of_blocks([], play=None)
    assert result == []

def test_load_list_of_blocks_with_invalid_type():
    with pytest.raises(AnsibleAssertionError):
        load_list_of_blocks("invalid_type", play=None)

def test_load_list_of_blocks_with_implicit_blocks(mock_block):
    ds = [{'task': 'task1'}, {'task': 'task2'}, {'block': 'block1'}]
    result = load_list_of_blocks(ds, play=None)
    assert len(result) == 2
    assert mock_block.load.call_count == 2

def test_load_list_of_blocks_with_explicit_blocks(mock_block):
    ds = [{'block': 'block1'}, {'block': 'block2'}]
    result = load_list_of_blocks(ds, play=None)
    assert len(result) == 2
    assert mock_block.load.call_count == 2

def test_load_list_of_blocks_with_mixed_blocks(mock_block):
    ds = [{'task': 'task1'}, {'block': 'block1'}, {'task': 'task2'}, {'block': 'block2'}]
    result = load_list_of_blocks(ds, play=None)
    assert len(result) == 4
    assert mock_block.load.call_count == 4
