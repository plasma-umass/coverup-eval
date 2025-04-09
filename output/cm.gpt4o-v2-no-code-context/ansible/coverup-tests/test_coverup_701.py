# file: lib/ansible/playbook/block.py:65-66
# asked: {"lines": [65, 66], "branches": []}
# gained: {"lines": [65, 66], "branches": []}

import pytest
from unittest.mock import Mock

# Assuming the Block class and its dependencies are imported from ansible.playbook.block
from ansible.playbook.block import Block

class TestBlock:
    def test_repr(self):
        # Mocking dependencies of Block
        mock_base = Mock()
        mock_conditional = Mock()
        mock_collection_search = Mock()
        mock_taggable = Mock()

        # Creating an instance of Block with mocked dependencies
        block = Block()
        block._uuid = '1234-5678'
        block._parent = 'parent_block'

        # Testing the __repr__ method
        repr_str = repr(block)
        expected_str = "BLOCK(uuid=1234-5678)(id=%s)(parent=parent_block)" % id(block)
        assert repr_str == expected_str

        # Clean up
        del block
