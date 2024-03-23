# file lib/ansible/playbook/helpers.py:33-81
# lines [33, 41, 43, 44, 46, 47, 48, 49, 50, 54, 55, 56, 57, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 81]
# branches ['43->44', '43->46', '47->48', '47->81', '49->50', '49->81', '55->56', '55->66', '66->49', '66->67', '67->66', '67->68']

import pytest
from ansible.playbook.helpers import load_list_of_blocks

# Mock Block class to avoid import and circular dependency issues
class MockBlock:
    @staticmethod
    def is_block(data):
        return isinstance(data, dict) and 'block' in data

    @staticmethod
    def load(data, **kwargs):
        return {'loaded': True, 'data': data}

# Replace the actual Block class with the mock
@pytest.fixture(autouse=True)
def mock_block_class(mocker):
    mocker.patch('ansible.playbook.block.Block', new=MockBlock)

def test_load_list_of_blocks_with_implicit_blocks():
    # Setup
    play = object()  # Mock play object
    ds = [
        {'name': 'task1', 'debug': 'var=fact1'},
        {'name': 'task2', 'debug': 'var=fact2'},
        {'block': [{'name': 'task3', 'debug': 'var=fact3'}]},
        {'name': 'task4', 'debug': 'var=fact4'}
    ]

    # Execute
    result = load_list_of_blocks(ds, play)

    # Verify
    assert len(result) == 3  # Two implicit blocks and one explicit block
    assert result[0]['data'] == [{'name': 'task1', 'debug': 'var=fact1'}, {'name': 'task2', 'debug': 'var=fact2'}]
    assert result[1]['data'] == {'block': [{'name': 'task3', 'debug': 'var=fact3'}]}
    assert result[2]['data'] == [{'name': 'task4', 'debug': 'var=fact4'}]  # Corrected to match the expected list structure

    # Cleanup is handled by pytest's fixture scope
