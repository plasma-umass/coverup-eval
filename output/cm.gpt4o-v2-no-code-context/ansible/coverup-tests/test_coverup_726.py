# file: lib/ansible/playbook/block.py:389-390
# asked: {"lines": [389, 390], "branches": []}
# gained: {"lines": [389, 390], "branches": []}

import pytest
from ansible.playbook.block import Block

@pytest.fixture
def block_instance():
    class MockBase:
        pass

    class MockConditional:
        pass

    class MockCollectionSearch:
        pass

    class MockTaggable:
        pass

    class MockBlock(Block, MockBase, MockConditional, MockCollectionSearch, MockTaggable):
        def __init__(self, block, rescue, always):
            self.block = block
            self.rescue = rescue
            self.always = always

    return MockBlock

def test_has_tasks_with_tasks(block_instance):
    block = block_instance(block=[1], rescue=[], always=[])
    assert block.has_tasks() is True

def test_has_tasks_with_rescue(block_instance):
    block = block_instance(block=[], rescue=[1], always=[])
    assert block.has_tasks() is True

def test_has_tasks_with_always(block_instance):
    block = block_instance(block=[], rescue=[], always=[1])
    assert block.has_tasks() is True

def test_has_tasks_without_tasks(block_instance):
    block = block_instance(block=[], rescue=[], always=[])
    assert block.has_tasks() is False
