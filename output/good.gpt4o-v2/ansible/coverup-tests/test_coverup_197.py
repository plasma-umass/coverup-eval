# file: lib/ansible/playbook/block.py:283-293
# asked: {"lines": [283, 284, 285, 286, 287, 288, 290, 291, 292, 293], "branches": [[285, 286], [285, 287], [287, 288], [287, 290], [291, 0], [291, 292], [292, 0], [292, 293]]}
# gained: {"lines": [283, 284, 285, 286, 287, 288, 290, 291, 292, 293], "branches": [[285, 286], [285, 287], [287, 288], [287, 290], [291, 0], [291, 292], [292, 0], [292, 293]]}

import pytest
from unittest.mock import Mock
from ansible.playbook.block import Block

@pytest.fixture
def loader():
    return Mock()

@pytest.fixture
def parent_block():
    return Mock()

@pytest.fixture
def role():
    return Mock()

@pytest.fixture
def block(parent_block, role):
    return Block(parent_block=parent_block, role=role)

def test_set_loader_with_parent(block, loader, parent_block):
    block._parent = parent_block
    parent_block.get_dep_chain = Mock(return_value=[])
    block.set_loader(loader)
    parent_block.set_loader.assert_called_once_with(loader)
    assert block._loader == loader

def test_set_loader_with_role(block, loader, role):
    block._parent = None
    block._role = role
    role.get_dep_chain = Mock(return_value=[])
    block.set_loader(loader)
    role.set_loader.assert_called_once_with(loader)
    assert block._loader == loader

def test_set_loader_with_dep_chain(block, loader):
    dep1 = Mock()
    dep2 = Mock()
    block.get_dep_chain = Mock(return_value=[dep1, dep2])
    block.set_loader(loader)
    dep1.set_loader.assert_called_once_with(loader)
    dep2.set_loader.assert_called_once_with(loader)
    assert block._loader == loader

def test_set_loader_no_parent_no_role_no_dep_chain(block, loader):
    block._parent = None
    block._role = None
    block.get_dep_chain = Mock(return_value=[])
    block.set_loader(loader)
    assert block._loader == loader
