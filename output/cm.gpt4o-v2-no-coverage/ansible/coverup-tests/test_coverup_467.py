# file: lib/ansible/playbook/block.py:170-177
# asked: {"lines": [170, 171, 172, 173, 175, 177], "branches": [[171, 172], [171, 177], [172, 173], [172, 175]]}
# gained: {"lines": [170, 171, 172, 173, 175, 177], "branches": [[171, 172], [171, 177], [172, 173], [172, 175]]}

import pytest
from unittest.mock import MagicMock

from ansible.playbook.block import Block

class TestBlock:
    @pytest.fixture
    def block(self):
        return Block()

    def test_get_dep_chain_none(self, block):
        block._dep_chain = None
        block._parent = None
        assert block.get_dep_chain() is None

    def test_get_dep_chain_with_parent(self, block):
        parent_block = MagicMock()
        parent_block.get_dep_chain.return_value = ['parent_dep']
        block._dep_chain = None
        block._parent = parent_block
        assert block.get_dep_chain() == ['parent_dep']
        parent_block.get_dep_chain.assert_called_once()

    def test_get_dep_chain_with_dep_chain(self, block):
        block._dep_chain = ['dep1', 'dep2']
        block._parent = None
        assert block.get_dep_chain() == ['dep1', 'dep2']
