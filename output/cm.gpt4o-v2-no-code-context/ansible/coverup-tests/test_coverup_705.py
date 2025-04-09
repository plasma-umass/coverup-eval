# file: lib/ansible/playbook/block.py:68-70
# asked: {"lines": [68, 70], "branches": []}
# gained: {"lines": [68, 70], "branches": []}

import pytest
from ansible.playbook.block import Block

class MockUUID:
    def __init__(self, uuid):
        self._uuid = uuid

@pytest.fixture
def block1():
    block = Block()
    block._uuid = '1234'
    return block

@pytest.fixture
def block2():
    block = Block()
    block._uuid = '1234'
    return block

@pytest.fixture
def block3():
    block = Block()
    block._uuid = '5678'
    return block

def test_block_equality(block1, block2, block3):
    assert block1 == block2, "Blocks with the same UUID should be equal"
    assert block1 != block3, "Blocks with different UUIDs should not be equal"

def test_block_equality_with_mockuuid(block1):
    mock_uuid = MockUUID('1234')
    assert block1 == mock_uuid, "Block should be equal to an object with the same UUID"
    mock_uuid_diff = MockUUID('5678')
    assert block1 != mock_uuid_diff, "Block should not be equal to an object with a different UUID"
