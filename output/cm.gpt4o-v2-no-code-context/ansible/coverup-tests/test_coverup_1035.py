# file: lib/ansible/playbook/block.py:164-166
# asked: {"lines": [165, 166], "branches": [[165, 0], [165, 166]]}
# gained: {"lines": [165, 166], "branches": [[165, 0], [165, 166]]}

import pytest
from ansible.playbook.block import Block
from ansible.errors import AnsibleParserError

class MockBase:
    pass

class MockConditional:
    pass

class MockCollectionSearch:
    pass

class MockTaggable:
    pass

class TestBlock(MockBase, MockConditional, MockCollectionSearch, MockTaggable, Block):
    def __init__(self, block, _ds):
        self.block = block
        self._ds = _ds

def test_validate_always_raises_error():
    block_instance = TestBlock(block=None, _ds={})
    with pytest.raises(AnsibleParserError, match="'test_attr' keyword cannot be used without 'block'"):
        block_instance._validate_always(attr='test_attr', name='test_attr', value=True)

def test_validate_always_no_error():
    block_instance = TestBlock(block=True, _ds={})
    try:
        block_instance._validate_always(attr='test_attr', name='test_attr', value=True)
    except AnsibleParserError:
        pytest.fail("AnsibleParserError was raised unexpectedly")
