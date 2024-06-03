# file lib/ansible/playbook/block.py:68-70
# lines [68, 70]
# branches []

import pytest
from unittest.mock import Mock

# Assuming the Block class is imported from ansible.playbook.block
from ansible.playbook.block import Block

class TestBlock:
    def test_block_equality(self):
        # Create two Block instances with the same _uuid
        block1 = Block()
        block2 = Block()
        
        # Mock the _uuid attribute
        block1._uuid = '1234'
        block2._uuid = '1234'
        
        # Assert that the two blocks are considered equal
        assert block1 == block2

    def test_block_inequality(self):
        # Create two Block instances with different _uuid
        block1 = Block()
        block2 = Block()
        
        # Mock the _uuid attribute
        block1._uuid = '1234'
        block2._uuid = '5678'
        
        # Assert that the two blocks are considered not equal
        assert block1 != block2
