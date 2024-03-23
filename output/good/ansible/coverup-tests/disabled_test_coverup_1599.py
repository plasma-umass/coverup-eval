# file lib/ansible/playbook/block.py:170-177
# lines [171, 172, 173, 175, 177]
# branches ['171->172', '171->177', '172->173', '172->175']

import pytest
from ansible.playbook.block import Block

# Mock class to simulate the parent behavior
class MockParent:
    def get_dep_chain(self):
        return ['mock_dep']

@pytest.fixture
def block():
    # Setup
    b = Block()
    yield b
    # Teardown
    b._dep_chain = None
    b._parent = None

def test_get_dep_chain_with_parent(mocker, block):
    # Mock the _parent attribute with an instance of MockParent
    block._parent = MockParent()
    # Assert that the dep_chain is retrieved from the parent
    assert block.get_dep_chain() == ['mock_dep']

def test_get_dep_chain_without_parent(block):
    # Assert that the dep_chain is None when there is no parent
    assert block.get_dep_chain() is None

def test_get_dep_chain_with_existing_dep_chain(block):
    # Set a dep_chain directly
    block._dep_chain = ['existing_dep']
    # Assert that the existing dep_chain is returned
    assert block.get_dep_chain() == ['existing_dep']
