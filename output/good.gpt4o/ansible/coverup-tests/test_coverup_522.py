# file lib/ansible/parsing/utils/yaml.py:46-56
# lines [46, 49, 50, 51, 53, 54, 55, 56]
# branches []

import pytest
from unittest import mock
from ansible.parsing.utils.yaml import _safe_load

class MockAnsibleLoader:
    def __init__(self, stream, file_name=None, vault_secrets=None):
        self.stream = stream
        self.file_name = file_name
        self.vault_secrets = vault_secrets

    def get_single_data(self):
        return "mocked_data"

    def dispose(self):
        pass

def test_safe_load(mocker):
    mocker.patch('ansible.parsing.utils.yaml.AnsibleLoader', MockAnsibleLoader)
    
    # Test with a stream and ensure get_single_data is called
    stream = "test_stream"
    result = _safe_load(stream)
    assert result == "mocked_data"
    
    # Test with a stream and file_name
    file_name = "test_file"
    result = _safe_load(stream, file_name)
    assert result == "mocked_data"
    
    # Test with a stream, file_name, and vault_secrets
    vault_secrets = "test_secrets"
    result = _safe_load(stream, file_name, vault_secrets)
    assert result == "mocked_data"
    
    # Test the dispose method is called
    mock_loader_instance = MockAnsibleLoader(stream)
    mocker.patch('ansible.parsing.utils.yaml.AnsibleLoader', return_value=mock_loader_instance)
    mock_loader_instance.dispose = mock.Mock()
    
    _safe_load(stream)
    mock_loader_instance.dispose.assert_called_once()

    # Test the AttributeError handling
    mock_loader_instance.dispose.side_effect = AttributeError
    _safe_load(stream)  # Should not raise an exception
