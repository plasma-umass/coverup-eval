# file: lib/ansible/playbook/block.py:389-390
# asked: {"lines": [389, 390], "branches": []}
# gained: {"lines": [389, 390], "branches": []}

import pytest
from ansible.playbook.block import Block

@pytest.fixture
def block_instance():
    return Block()

def test_has_tasks_with_empty_lists(block_instance):
    block_instance.block = []
    block_instance.rescue = []
    block_instance.always = []
    assert not block_instance.has_tasks()

def test_has_tasks_with_non_empty_block(block_instance):
    block_instance.block = [1]
    block_instance.rescue = []
    block_instance.always = []
    assert block_instance.has_tasks()

def test_has_tasks_with_non_empty_rescue(block_instance):
    block_instance.block = []
    block_instance.rescue = [1]
    block_instance.always = []
    assert block_instance.has_tasks()

def test_has_tasks_with_non_empty_always(block_instance):
    block_instance.block = []
    block_instance.rescue = []
    block_instance.always = [1]
    assert block_instance.has_tasks()
