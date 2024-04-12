# file lib/ansible/playbook/block.py:389-390
# lines [390]
# branches []

import pytest
from ansible.playbook.block import Block

# Assuming the Block class has attributes `block`, `rescue`, and `always`
# which are lists of tasks.

@pytest.fixture
def empty_block():
    block = Block()
    block.block = []
    block.rescue = []
    block.always = []
    return block

@pytest.fixture
def non_empty_block():
    block = Block()
    block.block = ['task1']
    block.rescue = []
    block.always = []
    return block

@pytest.fixture
def non_empty_rescue():
    block = Block()
    block.block = []
    block.rescue = ['task2']
    block.always = []
    return block

@pytest.fixture
def non_empty_always():
    block = Block()
    block.block = []
    block.rescue = []
    block.always = ['task3']
    return block

def test_has_tasks_with_empty_block(empty_block):
    assert not empty_block.has_tasks()

def test_has_tasks_with_non_empty_block(non_empty_block):
    assert non_empty_block.has_tasks()

def test_has_tasks_with_non_empty_rescue(non_empty_rescue):
    assert non_empty_rescue.has_tasks()

def test_has_tasks_with_non_empty_always(non_empty_always):
    assert non_empty_always.has_tasks()
