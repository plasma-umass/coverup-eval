# file: lib/ansible/playbook/block.py:76-87
# asked: {"lines": [76, 82, 84, 85, 87], "branches": [[84, 85], [84, 87]]}
# gained: {"lines": [76, 82, 84, 85, 87], "branches": [[84, 85], [84, 87]]}

import pytest
from ansible.playbook.block import Block

class MockParent:
    def get_vars(self):
        return {'parent_var': 'value'}

@pytest.fixture
def block_with_parent():
    parent = MockParent()
    block = Block(parent_block=parent)
    block.vars = {'block_var': 'value'}
    return block

@pytest.fixture
def block_without_parent():
    block = Block()
    block.vars = {'block_var': 'value'}
    return block

def test_get_vars_with_parent(block_with_parent):
    result = block_with_parent.get_vars()
    assert result == {'block_var': 'value', 'parent_var': 'value'}

def test_get_vars_without_parent(block_without_parent):
    result = block_without_parent.get_vars()
    assert result == {'block_var': 'value'}
