# file lib/ansible/playbook/block.py:170-177
# lines [170, 171, 172, 173, 175, 177]
# branches ['171->172', '171->177', '172->173', '172->175']

import pytest
from ansible.playbook.block import Block

# Mock class to simulate the parent behavior
class MockParent:
    def get_dep_chain(self):
        return ['parent_dep']

@pytest.fixture
def block():
    return Block()

@pytest.fixture
def block_with_parent():
    block = Block()
    block._parent = MockParent()
    return block

@pytest.fixture
def block_with_dep_chain():
    block = Block()
    block._dep_chain = ['dep1', 'dep2']
    return block

def test_get_dep_chain_without_parent_or_dep_chain(block):
    assert block.get_dep_chain() is None

def test_get_dep_chain_with_parent(block_with_parent):
    assert block_with_parent.get_dep_chain() == ['parent_dep']

def test_get_dep_chain_with_dep_chain(block_with_dep_chain):
    assert block_with_dep_chain.get_dep_chain() == ['dep1', 'dep2']
