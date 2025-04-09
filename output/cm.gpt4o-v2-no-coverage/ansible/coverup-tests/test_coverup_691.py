# file: lib/ansible/playbook/block.py:164-166
# asked: {"lines": [164, 165, 166], "branches": [[165, 0], [165, 166]]}
# gained: {"lines": [164, 165, 166], "branches": [[165, 0], [165, 166]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.block import Block

class MockBlock(Block):
    def __init__(self, block=None, ds=None):
        self.block = block
        self._ds = ds

def test_validate_always_with_block():
    block = MockBlock(block=True)
    block._validate_always(attr=None, name='always', value=True)
    # No exception should be raised

def test_validate_always_without_block():
    block = MockBlock(block=False, ds={'some': 'data'})
    with pytest.raises(AnsibleParserError) as excinfo:
        block._validate_always(attr=None, name='always', value=True)
    assert str(excinfo.value) == "'always' keyword cannot be used without 'block'"
    assert excinfo.value.obj == {'some': 'data'}

def test_validate_always_without_value():
    block = MockBlock(block=False)
    block._validate_always(attr=None, name='always', value=False)
    # No exception should be raised
