# file: lib/ansible/playbook/block.py:392-396
# asked: {"lines": [392, 393, 394, 396], "branches": [[393, 394], [393, 396]]}
# gained: {"lines": [392, 393, 394, 396], "branches": [[393, 394], [393, 396]]}

import pytest
from unittest.mock import MagicMock

from ansible.playbook.block import Block
from ansible.playbook.base import Base
from ansible.playbook.conditional import Conditional
from ansible.playbook.collectionsearch import CollectionSearch
from ansible.playbook.taggable import Taggable

class MockParent:
    def get_include_params(self):
        return {'key': 'value'}

class TestBlock:
    def test_get_include_params_with_parent(self):
        parent = MockParent()
        block = Block()
        block._parent = parent

        result = block.get_include_params()
        assert result == {'key': 'value'}

    def test_get_include_params_without_parent(self):
        block = Block()
        block._parent = None

        result = block.get_include_params()
        assert result == {}
