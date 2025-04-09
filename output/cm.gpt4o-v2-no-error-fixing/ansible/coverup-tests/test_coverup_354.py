# file: lib/ansible/playbook/block.py:76-87
# asked: {"lines": [76, 82, 84, 85, 87], "branches": [[84, 85], [84, 87]]}
# gained: {"lines": [76, 82, 84, 85, 87], "branches": [[84, 85], [84, 87]]}

import pytest
from unittest.mock import MagicMock

from ansible.playbook.block import Block

@pytest.fixture
def block_with_parent():
    parent_block = MagicMock(spec=Block)
    parent_block.get_vars.return_value = {'parent_var': 'value'}
    block = Block()
    block.vars = {'block_var': 'value'}
    block._parent = parent_block
    return block

@pytest.fixture
def block_without_parent():
    block = Block()
    block.vars = {'block_var': 'value'}
    block._parent = None
    return block

def test_get_vars_with_parent(block_with_parent):
    result = block_with_parent.get_vars()
    assert result == {'block_var': 'value', 'parent_var': 'value'}

def test_get_vars_without_parent(block_without_parent):
    result = block_without_parent.get_vars()
    assert result == {'block_var': 'value'}
