# file: lib/ansible/playbook/block.py:392-396
# asked: {"lines": [392, 393, 394, 396], "branches": [[393, 394], [393, 396]]}
# gained: {"lines": [392, 393, 394, 396], "branches": [[393, 394], [393, 396]]}

import pytest
from unittest.mock import MagicMock

# Assuming the Block class is defined in ansible/playbook/block.py
from ansible.playbook.block import Block

class TestBlock:

    @pytest.fixture
    def block_with_parent(self):
        parent = MagicMock()
        block = Block()
        block._parent = parent
        return block

    @pytest.fixture
    def block_without_parent(self):
        block = Block()
        block._parent = None
        return block

    def test_get_include_params_with_parent(self, block_with_parent):
        block_with_parent._parent.get_include_params.return_value = {'key': 'value'}
        result = block_with_parent.get_include_params()
        assert result == {'key': 'value'}
        block_with_parent._parent.get_include_params.assert_called_once()

    def test_get_include_params_without_parent(self, block_without_parent):
        result = block_without_parent.get_include_params()
        assert result == {}
