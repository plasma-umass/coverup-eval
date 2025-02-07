# file: lib/ansible/playbook/block.py:72-74
# asked: {"lines": [72, 74], "branches": []}
# gained: {"lines": [72, 74], "branches": []}

import pytest
from ansible.playbook.block import Block

def test_block_ne():
    block1 = Block()
    block2 = Block()
    
    # Ensure both blocks have different UUIDs
    block1._uuid = '12345'
    block2._uuid = '67890'
    
    assert block1 != block2

    # Ensure both blocks have the same UUIDs
    block2._uuid = '12345'
    
    assert not block1 != block2
