# file: lib/ansible/playbook/block.py:164-166
# asked: {"lines": [164, 165, 166], "branches": [[165, 0], [165, 166]]}
# gained: {"lines": [164, 165, 166], "branches": [[165, 0], [165, 166]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.block import Block

class MockBlock(Block):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._ds = {}

def test_validate_always_with_block():
    block = MockBlock()
    block.block = ['some_block']
    block._validate_always('attr', 'name', 'value')
    # No exception should be raised

def test_validate_always_without_block():
    block = MockBlock()
    block.block = []
    with pytest.raises(AnsibleParserError, match="'name' keyword cannot be used without 'block'"):
        block._validate_always('attr', 'name', 'value')
