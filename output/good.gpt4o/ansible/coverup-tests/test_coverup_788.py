# file lib/ansible/playbook/block.py:72-74
# lines [72, 74]
# branches []

import pytest
from unittest.mock import Mock

# Assuming the Block class is imported from ansible.playbook.block
from ansible.playbook.block import Block

class TestBlock:
    def test_block_ne(self):
        # Create two Block instances with different _uuid values
        block1 = Block()
        block2 = Block()
        
        # Mock the _uuid attributes
        block1._uuid = 'uuid1'
        block2._uuid = 'uuid2'
        
        # Assert that the __ne__ method returns True for different _uuid values
        assert block1 != block2
        
        # Now set the _uuid attributes to be the same
        block2._uuid = 'uuid1'
        
        # Assert that the __ne__ method returns False for the same _uuid values
        assert not block1 != block2
