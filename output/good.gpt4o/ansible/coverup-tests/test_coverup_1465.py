# file lib/ansible/playbook/block.py:224-243
# lines []
# branches ['237->239', '239->243']

import pytest
from unittest.mock import Mock

# Assuming the Block class and its dependencies are imported from ansible.playbook.block
from ansible.playbook.block import Block

class TestBlock:
    @pytest.fixture
    def block_instance(self):
        # Mocking the dependencies and attributes of Block
        block = Block()
        block._valid_attrs = ['attr1', 'attr2', 'block', 'rescue', 'always']
        block.attr1 = 'value1'
        block.attr2 = 'value2'
        block.get_dep_chain = Mock(return_value='dep_chain_value')
        block._role = Mock()
        block._role.serialize = Mock(return_value='role_serialized')
        block._parent = Mock()
        block._parent.copy = Mock(return_value=block._parent)
        block._parent.serialize = Mock(return_value='parent_serialized')
        block._parent.__class__.__name__ = 'ParentClass'
        return block

    def test_serialize_with_role_and_parent(self, block_instance):
        block_instance._role = Mock()
        block_instance._role.serialize = Mock(return_value='role_serialized')
        block_instance._parent = Mock()
        block_instance._parent.copy = Mock(return_value=block_instance._parent)
        block_instance._parent.serialize = Mock(return_value='parent_serialized')
        block_instance._parent.__class__.__name__ = 'ParentClass'

        result = block_instance.serialize()

        assert result['attr1'] == 'value1'
        assert result['attr2'] == 'value2'
        assert result['dep_chain'] == 'dep_chain_value'
        assert result['role'] == 'role_serialized'
        assert result['parent'] == 'parent_serialized'
        assert result['parent_type'] == 'ParentClass'

    def test_serialize_without_role_and_parent(self, block_instance):
        block_instance._role = None
        block_instance._parent = None

        result = block_instance.serialize()

        assert result['attr1'] == 'value1'
        assert result['attr2'] == 'value2'
        assert result['dep_chain'] == 'dep_chain_value'
        assert 'role' not in result
        assert 'parent' not in result
        assert 'parent_type' not in result
