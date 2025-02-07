# file: lib/ansible/playbook/base.py:871-876
# asked: {"lines": [873, 874, 876], "branches": [[873, 874], [873, 876]]}
# gained: {"lines": [873, 874, 876], "branches": [[873, 874], [873, 876]]}

import pytest
from unittest.mock import MagicMock

from ansible.playbook.base import Base

@pytest.fixture
def base_instance():
    instance = Base()
    instance._parent = None  # Ensure the _parent attribute exists
    return instance

def test_get_dep_chain_with_parent(monkeypatch, base_instance):
    parent_mock = MagicMock()
    parent_mock.get_dep_chain.return_value = "parent_chain"
    monkeypatch.setattr(base_instance, '_parent', parent_mock)
    
    result = base_instance.get_dep_chain()
    
    assert result == "parent_chain"
    parent_mock.get_dep_chain.assert_called_once()

def test_get_dep_chain_without_parent(monkeypatch, base_instance):
    monkeypatch.setattr(base_instance, '_parent', None)
    
    result = base_instance.get_dep_chain()
    
    assert result is None
