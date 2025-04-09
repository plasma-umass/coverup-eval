# file: lib/ansible/plugins/loader.py:1148-1157
# asked: {"lines": [1150, 1151], "branches": [[1149, 1150]]}
# gained: {"lines": [1150, 1151], "branches": [[1149, 1150]]}

import pytest
from unittest import mock
from ansible.plugins.loader import _configure_collection_loader, AnsibleCollectionConfig, display

@pytest.fixture(autouse=True)
def reset_ansible_collection_config():
    original_finder = AnsibleCollectionConfig._collection_finder
    AnsibleCollectionConfig._collection_finder = None
    yield
    AnsibleCollectionConfig._collection_finder = original_finder

def test_configure_collection_loader_already_configured(monkeypatch):
    mock_warning = mock.Mock()
    monkeypatch.setattr(display, 'warning', mock_warning)
    
    AnsibleCollectionConfig._collection_finder = True  # Simulate already configured state
    
    _configure_collection_loader()
    
    mock_warning.assert_called_once_with('AnsibleCollectionFinder has already been configured')
