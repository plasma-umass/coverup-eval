# file lib/ansible/playbook/block.py:170-177
# lines [177]
# branches ['171->177']

import pytest
from ansible.playbook.block import Block

# Mock class to simulate the parent behavior
class MockParent:
    def get_dep_chain(self):
        return ['dependency1', 'dependency2']

@pytest.fixture
def block():
    # Setup
    b = Block()
    yield b
    # Teardown
    b._dep_chain = None

def test_get_dep_chain_with_parent(mocker, block):
    # Mock the _parent attribute to return a predefined dependency chain
    mocker.patch.object(block, '_parent', new=MockParent())
    
    # Assert that the dependency chain is retrieved from the parent
    assert block.get_dep_chain() == ['dependency1', 'dependency2']

def test_get_dep_chain_without_parent(block):
    # Assert that None is returned when there is no parent
    assert block.get_dep_chain() is None

def test_get_dep_chain_with_existing_dep_chain(block):
    # Set a dependency chain directly
    block._dep_chain = ['dependency3', 'dependency4']
    
    # Assert that the existing dependency chain is returned
    assert block.get_dep_chain() == ['dependency3', 'dependency4']
