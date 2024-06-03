# file lib/ansible/playbook/block.py:76-87
# lines [82, 84, 85, 87]
# branches ['84->85', '84->87']

import pytest
from unittest.mock import Mock

# Assuming the Block class and its dependencies are imported from ansible.playbook.block
from ansible.playbook.block import Block

@pytest.fixture
def block_with_parent():
    parent_block = Mock()
    parent_block.get_vars.return_value = {'parent_var': 'value'}
    
    block = Block()
    block.vars = {'block_var': 'value'}
    block._parent = parent_block
    
    return block

def test_block_get_vars_with_parent(block_with_parent):
    result = block_with_parent.get_vars()
    
    assert 'block_var' in result
    assert result['block_var'] == 'value'
    assert 'parent_var' in result
    assert result['parent_var'] == 'value'
    
    # Clean up
    block_with_parent._parent = None
