# file lib/ansible/playbook/block.py:95-103
# lines [95, 96, 97, 98, 99, 100, 101, 102, 103]
# branches ['98->99', '98->103', '99->100', '99->103', '100->99', '100->101']

import pytest
from ansible.playbook.block import Block

def test_is_block_with_dict_containing_block():
    ds = {'block': 'some_value'}
    assert Block.is_block(ds) == True

def test_is_block_with_dict_containing_rescue():
    ds = {'rescue': 'some_value'}
    assert Block.is_block(ds) == True

def test_is_block_with_dict_containing_always():
    ds = {'always': 'some_value'}
    assert Block.is_block(ds) == True

def test_is_block_with_dict_not_containing_block_rescue_always():
    ds = {'other_key': 'some_value'}
    assert Block.is_block(ds) == False

def test_is_block_with_non_dict():
    ds = ['block', 'rescue', 'always']
    assert Block.is_block(ds) == False
