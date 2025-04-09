# file: lib/ansible/parsing/utils/yaml.py:46-56
# asked: {"lines": [46, 49, 50, 51, 53, 54, 55, 56], "branches": []}
# gained: {"lines": [46, 49, 50, 51, 53, 54, 55, 56], "branches": []}

import pytest
from ansible.parsing.utils.yaml import _safe_load
from ansible.parsing.yaml.loader import AnsibleLoader
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_ansible_loader(monkeypatch):
    mock_loader = MagicMock(spec=AnsibleLoader)
    monkeypatch.setattr('ansible.parsing.utils.yaml.AnsibleLoader', mock_loader)
    return mock_loader

def test_safe_load_with_dispose(mock_ansible_loader):
    stream = "test_stream"
    file_name = "test_file"
    vault_secrets = "test_secrets"
    
    mock_loader_instance = mock_ansible_loader.return_value
    mock_loader_instance.get_single_data.return_value = "test_data"
    
    result = _safe_load(stream, file_name, vault_secrets)
    
    mock_ansible_loader.assert_called_once_with(stream, file_name, vault_secrets)
    mock_loader_instance.get_single_data.assert_called_once()
    mock_loader_instance.dispose.assert_called_once()
    
    assert result == "test_data"

def test_safe_load_without_dispose(mock_ansible_loader):
    stream = "test_stream"
    file_name = "test_file"
    vault_secrets = "test_secrets"
    
    mock_loader_instance = mock_ansible_loader.return_value
    mock_loader_instance.get_single_data.return_value = "test_data"
    del mock_loader_instance.dispose
    
    result = _safe_load(stream, file_name, vault_secrets)
    
    mock_ansible_loader.assert_called_once_with(stream, file_name, vault_secrets)
    mock_loader_instance.get_single_data.assert_called_once()
    
    assert result == "test_data"
