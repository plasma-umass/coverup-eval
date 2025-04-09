# file: lib/ansible/playbook/block.py:72-74
# asked: {"lines": [72, 74], "branches": []}
# gained: {"lines": [72, 74], "branches": []}

import pytest
from unittest.mock import Mock

from ansible.playbook.block import Block

class TestBlock:

    def test_ne_method(self):
        # Create two Block instances with different _uuid values
        block1 = Block()
        block2 = Block()
        
        # Mock the _uuid attribute
        block1._uuid = '12345'
        block2._uuid = '67890'
        
        # Assert that the __ne__ method returns True for different _uuid values
        assert block1 != block2

        # Set the same _uuid for both instances
        block2._uuid = '12345'
        
        # Assert that the __ne__ method returns False for same _uuid values
        assert not block1 != block2
