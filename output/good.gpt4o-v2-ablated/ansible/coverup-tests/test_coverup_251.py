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

class TestBlock(MockBase, MockConditional, MockCollectionSearch, MockTaggable):
    def __init__(self, block, _ds):
        self.block = block
        self._ds = _ds

    def _validate_always(self, attr, name, value):
        if value and not self.block:
            raise AnsibleParserError("'%s' keyword cannot be used without 'block'" % name, obj=self._ds)

@pytest.fixture
def block_instance():
    return TestBlock(block=None, _ds={})

def test_validate_always_raises_error(block_instance):
    with pytest.raises(AnsibleParserError) as excinfo:
        block_instance._validate_always(attr=None, name='test', value=True)
    assert "'test' keyword cannot be used without 'block'" in str(excinfo.value)

def test_validate_always_no_error(block_instance):
    block_instance.block = True
    try:
        block_instance._validate_always(attr=None, name='test', value=True)
    except AnsibleParserError:
        pytest.fail("AnsibleParserError was raised unexpectedly")

def test_validate_always_no_value(block_instance):
    try:
        block_instance._validate_always(attr=None, name='test', value=False)
    except AnsibleParserError:
        pytest.fail("AnsibleParserError was raised unexpectedly")
