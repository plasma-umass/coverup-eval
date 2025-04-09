# file: lib/ansible/playbook/block.py:95-103
# asked: {"lines": [95, 96, 97, 98, 99, 100, 101, 102, 103], "branches": [[98, 99], [98, 103], [99, 100], [99, 103], [100, 99], [100, 101]]}
# gained: {"lines": [95, 96, 97, 98, 99, 100, 101, 102, 103], "branches": [[98, 99], [98, 103], [99, 100], [99, 103], [100, 99], [100, 101]]}

import pytest
from ansible.playbook.block import Block

@pytest.fixture
def block_instance():
    return Block()

def test_is_block_with_block_key(block_instance):
    ds = {'block': 'some_value'}
    assert block_instance.is_block(ds) == True

def test_is_block_with_rescue_key(block_instance):
    ds = {'rescue': 'some_value'}
    assert block_instance.is_block(ds) == True

def test_is_block_with_always_key(block_instance):
    ds = {'always': 'some_value'}
    assert block_instance.is_block(ds) == True

def test_is_block_with_no_block_keys(block_instance):
    ds = {'some_key': 'some_value'}
    assert block_instance.is_block(ds) == False

def test_is_block_with_non_dict(block_instance):
    ds = ['not', 'a', 'dict']
    assert block_instance.is_block(ds) == False
