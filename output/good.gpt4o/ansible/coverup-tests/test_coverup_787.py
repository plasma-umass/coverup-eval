# file lib/ansible/playbook/block.py:65-66
# lines [65, 66]
# branches []

import pytest
from unittest.mock import Mock

# Assuming the Block class is imported from ansible.playbook.block
from ansible.playbook.block import Block

def test_block_repr():
    # Mocking the parent and uuid attributes
    mock_parent = Mock()
    mock_uuid = '1234-5678-9012'
    
    # Creating an instance of Block with mocked attributes
    block = Block()
    block._parent = mock_parent
    block._uuid = mock_uuid
    
    # Expected representation string
    expected_repr = "BLOCK(uuid=1234-5678-9012)(id=%s)(parent=%s)" % (id(block), mock_parent)
    
    # Asserting the __repr__ output
    assert repr(block) == expected_repr
