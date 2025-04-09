# file: lib/ansible/playbook/block.py:392-396
# asked: {"lines": [392, 393, 394, 396], "branches": [[393, 394], [393, 396]]}
# gained: {"lines": [392, 393, 394, 396], "branches": [[393, 394], [393, 396]]}

import pytest
from ansible.playbook.block import Block

class MockParent:
    def get_include_params(self):
        return {'key': 'value'}

@pytest.fixture
def block_with_parent():
    return Block(parent_block=MockParent())

@pytest.fixture
def block_without_parent():
    return Block()

def test_get_include_params_with_parent(block_with_parent):
    result = block_with_parent.get_include_params()
    assert result == {'key': 'value'}

def test_get_include_params_without_parent(block_without_parent):
    result = block_without_parent.get_include_params()
    assert result == {}
