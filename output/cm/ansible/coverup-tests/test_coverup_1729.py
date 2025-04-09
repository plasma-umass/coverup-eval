# file lib/ansible/playbook/block.py:164-166
# lines []
# branches ['165->exit']

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.block import Block

# Assuming that the Block class has a constructor that accepts parameters for initialization
# and that self._ds is a valid attribute that gets set during initialization.

def test_validate_always_with_block(mocker):
    # Mock the Block constructor to avoid side effects
    mocker.patch.object(Block, '__init__', return_value=None)
    
    # Create an instance of Block without calling the actual constructor
    block = Block()
    
    # Manually set the _ds attribute to simulate the data structure
    block._ds = {'dummy': 'data'}
    
    # Set block attribute to a non-None value to simulate the presence of a block
    block.block = 'some_block'
    
    # Test the _validate_always method to ensure it does not raise an AnsibleParserError
    # when 'block' is present
    try:
        block._validate_always('attr', 'always', True)
    except AnsibleParserError:
        pytest.fail("AnsibleParserError was raised unexpectedly!")
