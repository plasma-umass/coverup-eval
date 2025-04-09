# file: lib/ansible/playbook/block.py:95-103
# asked: {"lines": [95, 96, 97, 98, 99, 100, 101, 102, 103], "branches": [[98, 99], [98, 103], [99, 100], [99, 103], [100, 99], [100, 101]]}
# gained: {"lines": [95, 96, 97, 98, 99, 100, 101, 102, 103], "branches": [[98, 99], [98, 103], [99, 100], [99, 103], [100, 99], [100, 101]]}

import pytest
from ansible.playbook.block import Block

def test_is_block_with_block_key():
    ds = {'block': []}
    assert Block.is_block(ds) is True

def test_is_block_with_rescue_key():
    ds = {'rescue': []}
    assert Block.is_block(ds) is True

def test_is_block_with_always_key():
    ds = {'always': []}
    assert Block.is_block(ds) is True

def test_is_block_with_no_block_keys():
    ds = {'tasks': []}
    assert Block.is_block(ds) is False

def test_is_block_with_non_dict():
    ds = ['block']
    assert Block.is_block(ds) is False
