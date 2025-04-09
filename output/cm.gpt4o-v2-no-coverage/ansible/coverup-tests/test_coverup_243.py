# file: lib/ansible/playbook/block.py:283-293
# asked: {"lines": [283, 284, 285, 286, 287, 288, 290, 291, 292, 293], "branches": [[285, 286], [285, 287], [287, 288], [287, 290], [291, 0], [291, 292], [292, 0], [292, 293]]}
# gained: {"lines": [283, 284, 285, 286, 287, 288, 290, 291, 292, 293], "branches": [[285, 286], [285, 287], [287, 288], [287, 290], [291, 0], [291, 292], [292, 0], [292, 293]]}

import pytest
from unittest.mock import Mock, create_autospec
from ansible.playbook.block import Block
from ansible.playbook.base import Base
from ansible.playbook.conditional import Conditional
from ansible.playbook.collectionsearch import CollectionSearch
from ansible.playbook.taggable import Taggable

@pytest.fixture
def block():
    return Block()

def test_set_loader_with_parent(block, mocker):
    mock_loader = Mock()
    mock_parent = create_autospec(Block, instance=True)
    block._parent = mock_parent
    block._role = None
    block._dep_chain = None

    block.set_loader(mock_loader)

    mock_parent.set_loader.assert_called_once_with(mock_loader)
    assert block._loader == mock_loader

def test_set_loader_with_role(block, mocker):
    mock_loader = Mock()
    mock_role = create_autospec(Block, instance=True)
    block._parent = None
    block._role = mock_role
    block._dep_chain = None

    block.set_loader(mock_loader)

    mock_role.set_loader.assert_called_once_with(mock_loader)
    assert block._loader == mock_loader

def test_set_loader_with_dep_chain(block, mocker):
    mock_loader = Mock()
    mock_dep = create_autospec(Block, instance=True)
    block._parent = None
    block._role = None
    block._dep_chain = [mock_dep]

    block.set_loader(mock_loader)

    mock_dep.set_loader.assert_called_once_with(mock_loader)
    assert block._loader == mock_loader

def test_set_loader_no_parent_role_dep_chain(block, mocker):
    mock_loader = Mock()
    block._parent = None
    block._role = None
    block._dep_chain = None

    block.set_loader(mock_loader)

    assert block._loader == mock_loader
