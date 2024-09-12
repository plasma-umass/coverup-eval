# file: lib/ansible/playbook/block.py:65-66
# asked: {"lines": [65, 66], "branches": []}
# gained: {"lines": [65, 66], "branches": []}

import pytest
from ansible.playbook.block import Block

@pytest.fixture
def block_instance():
    return Block()

def test_block_repr(block_instance):
    block_instance._uuid = "test-uuid"
    block_instance._parent = "test-parent"
    repr_str = repr(block_instance)
    assert repr_str == "BLOCK(uuid=test-uuid)(id=%s)(parent=test-parent)" % id(block_instance)
