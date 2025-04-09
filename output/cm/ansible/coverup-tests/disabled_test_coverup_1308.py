# file lib/ansible/playbook/block.py:76-87
# lines [82, 84, 85, 87]
# branches ['84->85', '84->87']

import pytest
from ansible.playbook.block import Block

# Mock class to simulate the parent with get_vars method
class MockParent:
    def get_vars(self):
        return {'parent_var': 'parent_value'}

@pytest.fixture
def mock_block(mocker):
    block = Block()
    block.vars = {'block_var': 'block_value'}
    mocker.patch.object(block, '_parent', new=MockParent())
    return block

def test_block_get_vars_with_parent(mock_block):
    # Test to cover lines 82-87
    result = mock_block.get_vars()
    assert 'block_var' in result
    assert result['block_var'] == 'block_value'
    assert 'parent_var' in result
    assert result['parent_var'] == 'parent_value'
