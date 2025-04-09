# file: lib/ansible/playbook/block.py:164-166
# asked: {"lines": [164, 165, 166], "branches": [[165, 0], [165, 166]]}
# gained: {"lines": [164, 165, 166], "branches": [[165, 0], [165, 166]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.block import Block

class MockBlock(Block):
    def __init__(self, block, ds):
        self.block = block
        self._ds = ds

def test_validate_always_raises_error():
    block_instance = MockBlock(block=None, ds={})
    with pytest.raises(AnsibleParserError) as excinfo:
        block_instance._validate_always(attr=None, name='always', value=True)
    assert "'always' keyword cannot be used without 'block'" in str(excinfo.value)

def test_validate_always_no_error():
    block_instance = MockBlock(block=True, ds={})
    try:
        block_instance._validate_always(attr=None, name='always', value=True)
    except AnsibleParserError:
        pytest.fail("AnsibleParserError was raised unexpectedly")
