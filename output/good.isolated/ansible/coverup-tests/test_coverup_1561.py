# file lib/ansible/playbook/block.py:283-293
# lines [284, 285, 286, 287, 288, 290, 291, 292, 293]
# branches ['285->286', '285->287', '287->288', '287->290', '291->exit', '291->292', '292->exit', '292->293']

import pytest
from ansible.playbook.block import Block

class MockLoader:
    pass

class MockParent:
    def set_loader(self, loader):
        self.loader_set = True
    def get_dep_chain(self):
        return []

class MockRole:
    def set_loader(self, loader):
        self.loader_set = True

class MockDep:
    def set_loader(self, loader):
        self.loader_set = True

@pytest.fixture
def block():
    return Block()

@pytest.fixture
def loader():
    return MockLoader()

def test_block_set_loader_with_parent(block, loader):
    parent = MockParent()
    block._parent = parent
    block.set_loader(loader)
    assert parent.loader_set, "Parent's set_loader should be called"

def test_block_set_loader_with_role(block, loader):
    role = MockRole()
    block._role = role
    block.set_loader(loader)
    assert role.loader_set, "Role's set_loader should be called"

def test_block_set_loader_with_dep_chain(block, loader, mocker):
    dep_chain = [MockDep(), MockDep()]
    mocker.patch.object(block, 'get_dep_chain', return_value=dep_chain)
    block.set_loader(loader)
    assert all(dep.loader_set for dep in dep_chain), "All dependencies' set_loader should be called"
