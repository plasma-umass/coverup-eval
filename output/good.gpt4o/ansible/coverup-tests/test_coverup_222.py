# file lib/ansible/playbook/block.py:283-293
# lines [283, 284, 285, 286, 287, 288, 290, 291, 292, 293]
# branches ['285->286', '285->287', '287->288', '287->290', '291->exit', '291->292', '292->exit', '292->293']

import pytest
from unittest.mock import Mock

# Assuming the necessary imports for Block, Base, Conditional, CollectionSearch, Taggable
from ansible.playbook.block import Block

class TestBlock:
    @pytest.fixture
    def block(self):
        # Mocking the parent and role attributes
        block = Block()
        block._parent = None
        block._role = None
        block.get_dep_chain = Mock(return_value=[])
        return block

    def test_set_loader_with_parent(self, block):
        parent = Mock()
        block._parent = parent
        loader = Mock()
        
        block.set_loader(loader)
        
        parent.set_loader.assert_called_once_with(loader)

    def test_set_loader_with_role(self, block):
        role = Mock()
        block._role = role
        loader = Mock()
        
        block.set_loader(loader)
        
        role.set_loader.assert_called_once_with(loader)

    def test_set_loader_with_dep_chain(self, block):
        dep1 = Mock()
        dep2 = Mock()
        block.get_dep_chain = Mock(return_value=[dep1, dep2])
        loader = Mock()
        
        block.set_loader(loader)
        
        dep1.set_loader.assert_called_once_with(loader)
        dep2.set_loader.assert_called_once_with(loader)
