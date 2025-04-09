# file lib/ansible/playbook/block.py:164-166
# lines [164, 165, 166]
# branches ['165->exit', '165->166']

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.block import Block

# Assuming the Block class has other necessary methods and attributes
# that are not shown in the provided code snippet.

def test_validate_always_without_block(mocker):
    # Mock the necessary parts of the Block class
    mocker.patch.object(Block, '__init__', return_value=None)
    
    block_instance = Block()
    block_instance._ds = {}  # Mock the data structure
    block_instance.block = None  # Set block to None to simulate the absence of 'block'

    # Test that AnsibleParserError is raised when 'always' is used without 'block'
    with pytest.raises(AnsibleParserError) as excinfo:
        block_instance._validate_always('always', 'always', True)
    
    # Assert that the exception message is correct
    assert "'always' keyword cannot be used without 'block'" in str(excinfo.value)
