# file: lib/ansible/playbook/block.py:361-387
# asked: {"lines": [361, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 379, 380, 381, 382, 383, 384, 385, 387], "branches": [[368, 369], [368, 377], [369, 370], [369, 373], [371, 368], [371, 372], [373, 368], [373, 376]]}
# gained: {"lines": [361, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 379, 380, 381, 382, 383, 384, 385, 387], "branches": [[368, 369], [368, 377], [369, 370], [369, 373], [371, 372], [373, 376]]}

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.block import Block

@pytest.fixture
def mock_play():
    return Mock()

@pytest.fixture
def mock_task():
    task = Mock()
    task.action = 'some_action'
    task.implicit = False
    task.evaluate_tags = Mock(return_value=True)
    return task

@pytest.fixture
def mock_block(mock_play):
    return Block(play=mock_play)

def test_filter_tagged_tasks_with_empty_block(mock_block):
    mock_block.block = []
    mock_block.rescue = []
    mock_block.always = []
    result = mock_block.filter_tagged_tasks(all_vars={})
    assert result.block == []
    assert result.rescue == []
    assert result.always == []

def test_filter_tagged_tasks_with_tasks(mock_block, mock_task):
    mock_block.block = [mock_task]
    mock_block.rescue = [mock_task]
    mock_block.always = [mock_task]
    result = mock_block.filter_tagged_tasks(all_vars={})
    assert result.block == [mock_task]
    assert result.rescue == [mock_task]
    assert result.always == [mock_task]

def test_filter_tagged_tasks_with_nested_block(mock_block, mock_task):
    nested_block = Block(play=mock_block._play)
    nested_block.block = [mock_task]
    mock_block.block = [nested_block]
    result = mock_block.filter_tagged_tasks(all_vars={})
    assert len(result.block) == 1
    assert isinstance(result.block[0], Block)
    assert result.block[0].block == [mock_task]

def test_filter_tagged_tasks_with_meta_action(mock_block, mock_task):
    with patch('ansible.constants._ACTION_META', new_callable=lambda: ['some_action']):
        mock_task.action = 'some_action'
        mock_task.implicit = True
        mock_block.block = [mock_task]
        result = mock_block.filter_tagged_tasks(all_vars={})
        assert result.block == [mock_task]

def test_filter_tagged_tasks_with_include_action(mock_block, mock_task):
    with patch('ansible.constants._ACTION_INCLUDE', new_callable=lambda: ['some_action']):
        mock_task.action = 'some_action'
        mock_task.evaluate_tags = Mock(return_value=True)
        mock_block.block = [mock_task]
        result = mock_block.filter_tagged_tasks(all_vars={})
        assert result.block == [mock_task]
