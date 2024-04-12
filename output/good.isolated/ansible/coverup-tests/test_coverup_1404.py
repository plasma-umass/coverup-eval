# file lib/ansible/playbook/helpers.py:33-81
# lines [44]
# branches ['43->44', '47->81']

import pytest
from ansible.playbook.helpers import load_list_of_blocks
from ansible.errors import AnsibleAssertionError

# Mock the Block class to avoid importing the actual Block class
# which could lead to circular dependency issues
class MockBlock:
    @staticmethod
    def is_block(data):
        # Mock the behavior of Block.is_block
        return isinstance(data, dict) and 'block' in data

    @staticmethod
    def load(data, **kwargs):
        # Mock the behavior of Block.load
        return {'loaded': True, 'data': data}

@pytest.fixture
def mock_block(mocker):
    mocker.patch('ansible.playbook.block.Block', new=MockBlock)

def test_load_list_of_blocks_with_non_list_input(mock_block):
    with pytest.raises(AnsibleAssertionError) as excinfo:
        load_list_of_blocks(ds="not a list", play=None)
    assert "should be a list or None but is" in str(excinfo.value)

def test_load_list_of_blocks_with_implicit_blocks(mock_block):
    ds = [
        {'name': 'task 1'},
        {'name': 'task 2'},
        {'block': 'explicit block', 'tasks': [{'name': 'task 3'}]},
    ]
    play = object()  # Mock play object
    blocks = load_list_of_blocks(ds, play)
    assert len(blocks) == 2  # The two tasks should be combined into one implicit block
    assert blocks[0]['data'] == [{'name': 'task 1'}, {'name': 'task 2'}]
    assert blocks[1]['data'] == {'block': 'explicit block', 'tasks': [{'name': 'task 3'}]}
