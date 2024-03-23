# file lib/ansible/playbook/block.py:95-103
# lines [95, 96, 97, 98, 99, 100, 101, 102, 103]
# branches ['98->99', '98->103', '99->100', '99->103', '100->99', '100->101']

import pytest
from ansible.playbook.block import Block

def test_is_block_with_block_key(mocker):
    # Setup
    ds_with_block = {'block': []}
    ds_with_rescue = {'rescue': []}
    ds_with_always = {'always': []}
    ds_without_block_keys = {'tasks': []}

    # Test block key
    assert Block.is_block(ds_with_block) is True, "is_block should return True for dict containing 'block' key"

    # Test rescue key
    assert Block.is_block(ds_with_rescue) is True, "is_block should return True for dict containing 'rescue' key"

    # Test always key
    assert Block.is_block(ds_with_always) is True, "is_block should return True for dict containing 'always' key"

    # Test dict without block, rescue, or always keys
    assert Block.is_block(ds_without_block_keys) is False, "is_block should return False for dict not containing 'block', 'rescue', or 'always' keys"

    # Test non-dict input
    assert Block.is_block([]) is False, "is_block should return False for non-dict input"
    assert Block.is_block(None) is False, "is_block should return False for None input"
    assert Block.is_block("string") is False, "is_block should return False for string input"
