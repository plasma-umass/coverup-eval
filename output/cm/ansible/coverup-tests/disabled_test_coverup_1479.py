# file lib/ansible/playbook/block.py:164-166
# lines []
# branches ['165->exit']

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.block import Block

# Assuming the Block class has a constructor that accepts parameters for initialization
# and that self._ds is a valid attribute that gets set during initialization.

class TestBlock:
    def test_validate_always_without_block_raises_error(self):
        # Setup the Block object with block set to None
        block_obj = Block()
        block_obj._ds = "dummy_ds"
        block_obj.block = None

        # Test the _validate_always method to ensure it raises the AnsibleParserError
        with pytest.raises(AnsibleParserError) as excinfo:
            block_obj._validate_always(attr=None, name='always', value=True)

        # Assert that the exception message is correct
        assert "'always' keyword cannot be used without 'block'" in str(excinfo.value)

    def test_validate_always_with_block_does_not_raise_error(self):
        # Setup the Block object with block set to a dummy value
        block_obj = Block()
        block_obj._ds = "dummy_ds"
        block_obj.block = "dummy_block"

        # Test the _validate_always method to ensure it does not raise an error
        try:
            block_obj._validate_always(attr=None, name='always', value=True)
        except AnsibleParserError:
            pytest.fail("AnsibleParserError was raised unexpectedly!")
