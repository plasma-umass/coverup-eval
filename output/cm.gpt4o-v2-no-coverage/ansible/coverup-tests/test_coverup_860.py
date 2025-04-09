# file: lib/ansible/playbook/block.py:72-74
# asked: {"lines": [72, 74], "branches": []}
# gained: {"lines": [72, 74], "branches": []}

import pytest
from unittest.mock import Mock

from ansible.playbook.block import Block

@pytest.fixture
def block_instance():
    block = Block()
    block._uuid = "1234"
    return block

@pytest.fixture
def other_block_instance():
    other_block = Block()
    other_block._uuid = "5678"
    return other_block

def test_block_ne(block_instance, other_block_instance):
    assert block_instance != other_block_instance

def test_block_eq(block_instance):
    other_block = Mock(spec=Block)
    other_block._uuid = "1234"
    assert block_instance == other_block
