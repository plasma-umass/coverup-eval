# file: lib/ansible/playbook/block.py:170-177
# asked: {"lines": [170, 171, 172, 173, 175, 177], "branches": [[171, 172], [171, 177], [172, 173], [172, 175]]}
# gained: {"lines": [170, 171, 172, 173, 175, 177], "branches": [[171, 172], [171, 177], [172, 173], [172, 175]]}

import pytest
from ansible.playbook.block import Block

class MockParent:
    def get_dep_chain(self):
        return ['parent_dep']

@pytest.fixture
def block_with_parent():
    return Block(parent_block=MockParent())

@pytest.fixture
def block_without_parent():
    return Block()

def test_get_dep_chain_with_parent(block_with_parent):
    dep_chain = block_with_parent.get_dep_chain()
    assert dep_chain == ['parent_dep']

def test_get_dep_chain_without_parent(block_without_parent):
    dep_chain = block_without_parent.get_dep_chain()
    assert dep_chain is None

def test_get_dep_chain_with_existing_chain(block_without_parent):
    block_without_parent._dep_chain = ['existing_dep']
    dep_chain = block_without_parent.get_dep_chain()
    assert dep_chain == ['existing_dep']
