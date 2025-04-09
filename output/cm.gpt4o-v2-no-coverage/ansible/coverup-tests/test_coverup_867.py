# file: lib/ansible/playbook/block.py:65-66
# asked: {"lines": [65, 66], "branches": []}
# gained: {"lines": [65, 66], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.playbook.block import Block

@pytest.fixture
def block_instance():
    return Block()

def test_block_repr(block_instance):
    block_instance._uuid = '1234-5678'
    block_instance._parent = None
    repr_str = repr(block_instance)
    assert repr_str == "BLOCK(uuid=1234-5678)(id=%s)(parent=None)" % id(block_instance)

