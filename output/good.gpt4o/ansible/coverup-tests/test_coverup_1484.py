# file lib/ansible/playbook/block.py:76-87
# lines []
# branches ['84->87']

import pytest
from unittest.mock import MagicMock

# Assuming the Block class and its dependencies are imported from ansible.playbook.block
from ansible.playbook.block import Block

class TestBlock:
    def test_get_vars_with_parent(self, mocker):
        # Mock the parent object and its get_vars method
        parent_mock = MagicMock()
        parent_mock.get_vars.return_value = {'parent_var': 'value'}

        # Create an instance of Block with a parent
        block = Block()
        block._parent = parent_mock
        block.vars = {'block_var': 'value'}

        # Call the get_vars method
        result = block.get_vars()

        # Assert that the parent's vars are included in the result
        assert result == {'block_var': 'value', 'parent_var': 'value'}

        # Clean up
        block._parent = None

    def test_get_vars_without_parent(self):
        # Create an instance of Block without a parent
        block = Block()
        block._parent = None
        block.vars = {'block_var': 'value'}

        # Call the get_vars method
        result = block.get_vars()

        # Assert that only the block's vars are included in the result
        assert result == {'block_var': 'value'}
