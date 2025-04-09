# file lib/ansible/playbook/block.py:68-70
# lines [68, 70]
# branches []

import pytest
from ansible.playbook.block import Block

# Assuming the Block class has a _uuid attribute and it is accessible.
# If it's not accessible directly, one would typically use a method or a fixture to set it up.

def test_block_equality(mocker):
    # Create two Block instances with the same _uuid
    block1 = Block()
    block2 = Block()
    mocker.patch.object(block1, '_uuid', 'unique_id_123')
    mocker.patch.object(block2, '_uuid', 'unique_id_123')

    # Assert that the two blocks are equal
    assert block1 == block2

    # Create another Block instance with a different _uuid
    block3 = Block()
    mocker.patch.object(block3, '_uuid', 'unique_id_456')

    # Assert that the first block is not equal to the third block
    assert block1 != block3
