# file lib/ansible/playbook/block.py:392-396
# lines [393, 394, 396]
# branches ['393->394', '393->396']

import pytest
from ansible.playbook.block import Block

# Assuming that the Block class has a constructor that accepts a parent parameter
# and that the parent class has a get_include_params method.

class MockParent:
    def get_include_params(self):
        return {'mock_key': 'mock_value'}

@pytest.fixture
def block_with_parent():
    parent = MockParent()
    block = Block()
    block._parent = parent
    return block

@pytest.fixture
def block_without_parent():
    block = Block()
    block._parent = None
    return block

def test_get_include_params_with_parent(block_with_parent):
    params = block_with_parent.get_include_params()
    assert params == {'mock_key': 'mock_value'}

def test_get_include_params_without_parent(block_without_parent):
    params = block_without_parent.get_include_params()
    assert params == {}
