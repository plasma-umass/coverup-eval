# file lib/ansible/playbook/block.py:76-87
# lines [76, 82, 84, 85, 87]
# branches ['84->85', '84->87']

import pytest
from ansible.playbook.block import Block

# Mocking the Base class since it's not provided in the snippet
class MockBase:
    def __init__(self):
        self.vars = {}

# Mocking the Conditional class since it's not provided in the snippet
class MockConditional:
    pass

# Mocking the CollectionSearch class since it's not provided in the snippet
class MockCollectionSearch:
    pass

# Mocking the Taggable class since it's not provided in the snippet
class MockTaggable:
    pass

# Creating a mock Block class with the necessary mixins
class MockBlock(MockBase, MockConditional, MockCollectionSearch, MockTaggable, Block):
    def __init__(self):
        MockBase.__init__(self)
        Block.__init__(self)

# Test function to cover the missing branch when self._parent is not None
def test_block_get_vars_with_parent():
    # Create a block with no parent
    block_without_parent = MockBlock()
    block_without_parent.vars = {'var1': 'value1'}

    # Create a parent block with its own vars
    parent_block = MockBlock()
    parent_block.vars = {'var2': 'value2'}

    # Set the parent of the block
    block_without_parent._parent = parent_block

    # Call get_vars on the block and verify that it includes vars from the parent
    vars = block_without_parent.get_vars()
    assert vars == {'var1': 'value1', 'var2': 'value2'}
