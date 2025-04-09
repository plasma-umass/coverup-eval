# file: lib/ansible/playbook/block.py:392-396
# asked: {"lines": [392, 393, 394, 396], "branches": [[393, 394], [393, 396]]}
# gained: {"lines": [392, 393, 394, 396], "branches": [[393, 394], [393, 396]]}

import pytest
from unittest.mock import Mock
from ansible.playbook.block import Block

class TestBlock:
    def test_get_include_params_with_parent(self):
        parent_mock = Mock()
        parent_mock.get_include_params.return_value = {'key': 'value'}
        
        block = Block()
        block._parent = parent_mock
        
        result = block.get_include_params()
        
        assert result == {'key': 'value'}
        parent_mock.get_include_params.assert_called_once()

    def test_get_include_params_without_parent(self):
        block = Block()
        block._parent = None
        
        result = block.get_include_params()
        
        assert result == {}
