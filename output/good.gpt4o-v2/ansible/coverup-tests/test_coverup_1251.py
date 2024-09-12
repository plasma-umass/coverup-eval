# file: lib/ansible/plugins/loader.py:1148-1157
# asked: {"lines": [1150, 1151], "branches": [[1149, 1150]]}
# gained: {"lines": [1150, 1151], "branches": [[1149, 1150]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.loader import _configure_collection_loader
from ansible.utils.collection_loader import AnsibleCollectionConfig

@pytest.fixture(autouse=True)
def reset_collection_finder(monkeypatch):
    # Ensure that the collection_finder is reset before each test
    original_finder = AnsibleCollectionConfig.collection_finder
    monkeypatch.setattr(AnsibleCollectionConfig, "_collection_finder", None)
    yield
    monkeypatch.setattr(AnsibleCollectionConfig, "_collection_finder", original_finder)

def test_configure_collection_loader_already_configured(monkeypatch):
    mock_display = MagicMock()
    monkeypatch.setattr("ansible.plugins.loader.display", mock_display)
    
    # Set the collection_finder to simulate it being already configured
    monkeypatch.setattr(AnsibleCollectionConfig, "_collection_finder", True)
    
    _configure_collection_loader()
    
    # Check that the warning was called
    mock_display.warning.assert_called_once_with('AnsibleCollectionFinder has already been configured')

def test_configure_collection_loader_not_configured(monkeypatch):
    mock_display = MagicMock()
    monkeypatch.setattr("ansible.plugins.loader.display", mock_display)
    
    mock_finder = MagicMock()
    monkeypatch.setattr("ansible.plugins.loader._AnsibleCollectionFinder", mock_finder)
    
    mock_config = MagicMock()
    monkeypatch.setattr("ansible.plugins.loader.C.config.get_config_value", mock_config)
    
    _configure_collection_loader()
    
    # Check that the warning was not called
    mock_display.warning.assert_not_called()
    
    # Check that the finder was instantiated and installed
    mock_finder.assert_called_once()
    mock_finder()._install.assert_called_once()
