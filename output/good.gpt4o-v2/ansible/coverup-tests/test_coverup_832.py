# file: lib/ansible/playbook/block.py:68-70
# asked: {"lines": [68, 70], "branches": []}
# gained: {"lines": [68, 70], "branches": []}

import pytest
from ansible.playbook.block import Block

def test_block_equality():
    block1 = Block()
    block2 = Block()
    block1._uuid = "12345"
    block2._uuid = "12345"
    assert block1 == block2

def test_block_inequality():
    block1 = Block()
    block2 = Block()
    block1._uuid = "12345"
    block2._uuid = "67890"
    assert block1 != block2
