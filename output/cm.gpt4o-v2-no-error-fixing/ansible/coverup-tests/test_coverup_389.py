# file: lib/ansible/playbook/base.py:871-876
# asked: {"lines": [871, 873, 874, 876], "branches": [[873, 874], [873, 876]]}
# gained: {"lines": [871, 873, 874, 876], "branches": [[873, 874], [873, 876]]}

import pytest
from ansible.playbook.base import Base

class MockParent:
    def get_dep_chain(self):
        return "mock_chain"

@pytest.fixture
def base_with_parent():
    base = Base()
    base._parent = MockParent()
    return base

@pytest.fixture
def base_without_parent():
    base = Base()
    base._parent = None
    return base

def test_get_dep_chain_with_parent(base_with_parent):
    assert base_with_parent.get_dep_chain() == "mock_chain"

def test_get_dep_chain_without_parent(base_without_parent):
    assert base_without_parent.get_dep_chain() is None
