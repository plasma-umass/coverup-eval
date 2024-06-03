# file lib/ansible/playbook/block.py:164-166
# lines [164, 165, 166]
# branches ['165->exit', '165->166']

import pytest
from ansible.playbook.block import Block
from ansible.errors import AnsibleParserError

class MockBlock(Block):
    def __init__(self):
        super().__init__()
        self._ds = {}  # Mock the _ds attribute

def test_validate_always_raises_error():
    block_instance = MockBlock()
    block_instance.block = None  # Ensure block is None to trigger the error

    with pytest.raises(AnsibleParserError) as excinfo:
        block_instance._validate_always(attr=None, name='test_name', value=True)
    
    assert "'test_name' keyword cannot be used without 'block'" in str(excinfo.value)
