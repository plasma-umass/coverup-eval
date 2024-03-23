# file lib/ansible/playbook/block.py:72-74
# lines [72, 74]
# branches []

import pytest
from ansible.playbook.block import Block

# Assuming the Block class has an __init__ method that initializes self._uuid
# If not, the Block class definition should be adjusted to include initialization of _uuid

@pytest.fixture
def create_blocks():
    block1 = Block()
    block1._uuid = '12345'
    block2 = Block()
    block2._uuid = '12345'
    block3 = Block()
    block3._uuid = '67890'
    return block1, block2, block3

def test_block_ne(create_blocks):
    block1, block2, block3 = create_blocks
    assert not (block1 != block2), "Blocks with the same UUID should be considered equal"
    assert block1 != block3, "Blocks with different UUIDs should not be considered equal"
