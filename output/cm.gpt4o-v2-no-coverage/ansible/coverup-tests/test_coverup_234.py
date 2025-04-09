# file: lib/ansible/playbook/block.py:224-243
# asked: {"lines": [224, 230, 231, 232, 233, 235, 237, 238, 239, 240, 241, 243], "branches": [[231, 232], [231, 235], [232, 231], [232, 233], [237, 238], [237, 239], [239, 240], [239, 243]]}
# gained: {"lines": [224, 230, 231, 232, 233, 235, 237, 238, 239, 240, 241, 243], "branches": [[231, 232], [231, 235], [232, 231], [232, 233], [237, 238], [237, 239], [239, 240], [239, 243]]}

import pytest
from unittest.mock import MagicMock

# Assuming the Block class and its dependencies are imported from ansible.playbook.block
from ansible.playbook.block import Block
from ansible.playbook.base import Base
from ansible.playbook.conditional import Conditional
from ansible.playbook.collectionsearch import CollectionSearch
from ansible.playbook.taggable import Taggable

class MockRole:
    def serialize(self):
        return {'role': 'mock_role'}

class MockParent:
    def get_dep_chain(self):
        return ['mock_dep_chain']

    def copy(self, exclude_tasks=False):
        return self

    def serialize(self):
        return {'parent': 'mock_parent'}

class TestBlock:
    @pytest.fixture
    def block(self):
        block = Block()
        block._valid_attrs = ['attr1', 'attr2', 'block', 'rescue', 'always']
        block.attr1 = 'value1'
        block.attr2 = 'value2'
        block._role = None
        block._parent = None
        block._dep_chain = None
        return block

    def test_serialize_no_role_no_parent(self, block):
        serialized = block.serialize()
        assert serialized == {
            'attr1': 'value1',
            'attr2': 'value2',
            'dep_chain': None
        }

    def test_serialize_with_role(self, block):
        block._role = MockRole()
        serialized = block.serialize()
        assert serialized == {
            'attr1': 'value1',
            'attr2': 'value2',
            'dep_chain': None,
            'role': {'role': 'mock_role'}
        }

    def test_serialize_with_parent(self, block):
        block._parent = MockParent()
        serialized = block.serialize()
        assert serialized == {
            'attr1': 'value1',
            'attr2': 'value2',
            'dep_chain': ['mock_dep_chain'],
            'parent': {'parent': 'mock_parent'},
            'parent_type': 'MockParent'
        }

    def test_serialize_with_role_and_parent(self, block):
        block._role = MockRole()
        block._parent = MockParent()
        serialized = block.serialize()
        assert serialized == {
            'attr1': 'value1',
            'attr2': 'value2',
            'dep_chain': ['mock_dep_chain'],
            'role': {'role': 'mock_role'},
            'parent': {'parent': 'mock_parent'},
            'parent_type': 'MockParent'
        }
