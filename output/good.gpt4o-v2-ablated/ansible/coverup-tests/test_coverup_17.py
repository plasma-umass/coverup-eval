# file: lib/ansible/playbook/helpers.py:33-81
# asked: {"lines": [33, 41, 43, 44, 46, 47, 48, 49, 50, 54, 55, 56, 57, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 81], "branches": [[43, 44], [43, 46], [47, 48], [47, 81], [49, 50], [49, 81], [55, 56], [55, 66], [66, 49], [66, 67], [67, 66], [67, 68]]}
# gained: {"lines": [33, 41, 43, 44, 46, 47, 48, 49, 50, 54, 55, 56, 57, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 81], "branches": [[43, 44], [43, 46], [47, 48], [47, 81], [49, 50], [49, 81], [55, 56], [55, 66], [66, 49], [66, 67], [67, 66], [67, 68]]}

import pytest
from ansible.playbook.helpers import load_list_of_blocks
from ansible.playbook.block import Block
from ansible.errors import AnsibleAssertionError

class MockBlock:
    @staticmethod
    def is_block(data):
        return isinstance(data, dict) and 'block' in data

    @staticmethod
    def load(data, play, parent_block, role, task_include, use_handlers, variable_manager, loader):
        return {'data': data, 'play': play, 'parent_block': parent_block, 'role': role, 'task_include': task_include, 'use_handlers': use_handlers, 'variable_manager': variable_manager, 'loader': loader}

@pytest.fixture
def mock_block(monkeypatch):
    monkeypatch.setattr('ansible.playbook.block.Block', MockBlock)

def test_load_list_of_blocks_none(mock_block):
    result = load_list_of_blocks(None, play='play')
    assert result == []

def test_load_list_of_blocks_empty_list(mock_block):
    result = load_list_of_blocks([], play='play')
    assert result == []

def test_load_list_of_blocks_invalid_type(mock_block):
    with pytest.raises(AnsibleAssertionError):
        load_list_of_blocks('invalid', play='play')

def test_load_list_of_blocks_single_task(mock_block):
    ds = [{'task': 'task1'}]
    result = load_list_of_blocks(ds, play='play')
    assert len(result) == 1
    assert result[0]['data'] == [{'task': 'task1'}]

def test_load_list_of_blocks_multiple_tasks(mock_block):
    ds = [{'task': 'task1'}, {'task': 'task2'}]
    result = load_list_of_blocks(ds, play='play')
    assert len(result) == 1
    assert result[0]['data'] == [{'task': 'task1'}, {'task': 'task2'}]

def test_load_list_of_blocks_with_block(mock_block):
    ds = [{'block': 'block1'}, {'task': 'task1'}, {'block': 'block2'}]
    result = load_list_of_blocks(ds, play='play')
    assert len(result) == 3
    assert result[0]['data'] == {'block': 'block1'}
    assert result[1]['data'] == [{'task': 'task1'}]
    assert result[2]['data'] == {'block': 'block2'}

def test_load_list_of_blocks_mixed(mock_block):
    ds = [{'task': 'task1'}, {'block': 'block1'}, {'task': 'task2'}, {'block': 'block2'}]
    result = load_list_of_blocks(ds, play='play')
    assert len(result) == 4
    assert result[0]['data'] == [{'task': 'task1'}]
    assert result[1]['data'] == {'block': 'block1'}
    assert result[2]['data'] == [{'task': 'task2'}]
    assert result[3]['data'] == {'block': 'block2'}
