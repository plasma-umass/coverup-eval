# file: lib/ansible/playbook/block.py:389-390
# asked: {"lines": [389, 390], "branches": []}
# gained: {"lines": [389], "branches": []}

import pytest
from ansible.playbook.block import Block

class MockBase:
    pass

class MockConditional:
    pass

class MockCollectionSearch:
    pass

class MockTaggable:
    pass

class MockBlock(MockBase, MockConditional, MockCollectionSearch, MockTaggable):
    def __init__(self, block, rescue, always):
        self.block = block
        self.rescue = rescue
        self.always = always

    def has_tasks(self):
        return len(self.block) > 0 or len(self.rescue) > 0 or len(self.always) > 0

@pytest.fixture
def block_with_tasks():
    return MockBlock(block=[1], rescue=[], always=[])

@pytest.fixture
def block_with_rescue():
    return MockBlock(block=[], rescue=[1], always=[])

@pytest.fixture
def block_with_always():
    return MockBlock(block=[], rescue=[], always=[1])

@pytest.fixture
def block_without_tasks():
    return MockBlock(block=[], rescue=[], always=[])

def test_has_tasks_with_tasks(block_with_tasks):
    assert block_with_tasks.has_tasks() is True

def test_has_tasks_with_rescue(block_with_rescue):
    assert block_with_rescue.has_tasks() is True

def test_has_tasks_with_always(block_with_always):
    assert block_with_always.has_tasks() is True

def test_has_tasks_without_tasks(block_without_tasks):
    assert block_without_tasks.has_tasks() is False
