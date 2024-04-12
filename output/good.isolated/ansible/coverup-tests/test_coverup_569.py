# file lib/ansible/playbook/base.py:871-876
# lines [871, 873, 874, 876]
# branches ['873->874', '873->876']

import pytest
from ansible.playbook.base import Base

class MockParent(Base):
    def get_dep_chain(self):
        return "mock_dep_chain"

@pytest.fixture
def base_instance():
    base = Base()
    yield base
    del base

@pytest.fixture
def base_instance_with_parent():
    base = Base()
    base._parent = MockParent()
    yield base
    del base._parent
    del base

def test_get_dep_chain_without_parent(base_instance):
    assert base_instance.get_dep_chain() is None

def test_get_dep_chain_with_parent(base_instance_with_parent):
    assert base_instance_with_parent.get_dep_chain() == "mock_dep_chain"
