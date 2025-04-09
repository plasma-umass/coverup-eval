# file: lib/ansible/parsing/utils/yaml.py:46-56
# asked: {"lines": [46, 49, 50, 51, 53, 54, 55, 56], "branches": []}
# gained: {"lines": [46, 49, 50, 51, 53, 54, 55, 56], "branches": []}

import pytest
from ansible.parsing.utils.yaml import _safe_load
from ansible.parsing.yaml.loader import AnsibleLoader

def test_safe_load_with_dispose(mocker):
    mock_stream = mocker.Mock()
    mock_file_name = "test_file"
    mock_vault_secrets = {"secret": "value"}

    mock_loader = mocker.patch('ansible.parsing.utils.yaml.AnsibleLoader', autospec=True)
    mock_loader_instance = mock_loader.return_value
    mock_loader_instance.get_single_data.return_value = "data"

    result = _safe_load(mock_stream, mock_file_name, mock_vault_secrets)

    assert result == "data"
    mock_loader_instance.get_single_data.assert_called_once()
    mock_loader_instance.dispose.assert_called_once()

def test_safe_load_without_dispose(mocker):
    mock_stream = mocker.Mock()
    mock_file_name = "test_file"
    mock_vault_secrets = {"secret": "value"}

    mock_loader = mocker.patch('ansible.parsing.utils.yaml.AnsibleLoader', autospec=True)
    mock_loader_instance = mock_loader.return_value
    mock_loader_instance.get_single_data.return_value = "data"
    del mock_loader_instance.dispose

    result = _safe_load(mock_stream, mock_file_name, mock_vault_secrets)

    assert result == "data"
    mock_loader_instance.get_single_data.assert_called_once()
    assert not hasattr(mock_loader_instance, 'dispose')
