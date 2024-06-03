# file lib/ansible/playbook/block.py:170-177
# lines [170, 171, 172, 173, 175, 177]
# branches ['171->172', '171->177', '172->173', '172->175']

import pytest
from unittest.mock import Mock

# Assuming the Block class is imported from ansible.playbook.block
from ansible.playbook.block import Block

class TestBlock:
    @pytest.fixture
    def block(self):
        return Block()

    def test_get_dep_chain_none(self, block):
        block._dep_chain = None
        block._parent = None
        assert block.get_dep_chain() is None

    def test_get_dep_chain_from_parent(self, mocker):
        parent_block = Mock()
        parent_block.get_dep_chain.return_value = ['parent_dep']
        block = Block()
        block._dep_chain = None
        block._parent = parent_block
        assert block.get_dep_chain() == ['parent_dep']
        parent_block.get_dep_chain.assert_called_once()

    def test_get_dep_chain_copy(self, block):
        block._dep_chain = ['dep1', 'dep2']
        block._parent = None
        result = block.get_dep_chain()
        assert result == ['dep1', 'dep2']
        assert result is not block._dep_chain  # Ensure a copy is returned
