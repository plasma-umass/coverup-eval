# file: lib/ansible/playbook/block.py:68-70
# asked: {"lines": [68, 70], "branches": []}
# gained: {"lines": [68, 70], "branches": []}

import pytest
from ansible.playbook.block import Block

class MockBlock(Block):
    def __init__(self, uuid):
        self._uuid = uuid

@pytest.fixture
def block1():
    return MockBlock(uuid="1234")

@pytest.fixture
def block2():
    return MockBlock(uuid="1234")

@pytest.fixture
def block3():
    return MockBlock(uuid="5678")

def test_block_equality(block1, block2, block3):
    assert block1 == block2
    assert block1 != block3
