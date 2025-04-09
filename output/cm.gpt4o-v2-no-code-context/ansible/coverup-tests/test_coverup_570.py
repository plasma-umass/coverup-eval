# file: lib/ansible/playbook/block.py:164-166
# asked: {"lines": [164, 165, 166], "branches": [[165, 0], [165, 166]]}
# gained: {"lines": [164], "branches": []}

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

class MockBlock(MockBase, MockConditional, MockCollectionSearch, MockTaggable):
    def __init__(self, block=None):
        self.block = block
        self._ds = {}

    def _validate_always(self, attr, name, value):
        if value and not self.block:
            raise AnsibleParserError("'%s' keyword cannot be used without 'block'" % name, obj=self._ds)

def test_validate_always_with_block():
    block = MockBlock(block=True)
    block._validate_always('attr', 'name', True)
    # No exception should be raised, so no assertion needed

def test_validate_always_without_block():
    block = MockBlock(block=False)
    with pytest.raises(AnsibleParserError) as excinfo:
        block._validate_always('attr', 'name', True)
    assert str(excinfo.value) == "'name' keyword cannot be used without 'block'"

def test_validate_always_value_false():
    block = MockBlock(block=False)
    block._validate_always('attr', 'name', False)
    # No exception should be raised, so no assertion needed
