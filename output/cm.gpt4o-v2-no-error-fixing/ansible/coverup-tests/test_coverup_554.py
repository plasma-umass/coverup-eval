# file: lib/ansible/playbook/block.py:65-66
# asked: {"lines": [65, 66], "branches": []}
# gained: {"lines": [65, 66], "branches": []}

import pytest
from ansible.playbook.block import Block

@pytest.fixture
def block_instance():
    return Block()

def test_block_repr(block_instance):
    # Mocking the attributes to ensure __repr__ can be called
    block_instance._uuid = "1234-5678"
    block_instance._parent = None

    # Call the __repr__ method and check the output
    repr_output = repr(block_instance)
    assert repr_output == "BLOCK(uuid=1234-5678)(id=%s)(parent=None)" % id(block_instance)
