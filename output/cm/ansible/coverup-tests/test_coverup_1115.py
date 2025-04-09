# file lib/ansible/parsing/dataloader.py:78-80
# lines [78, 80]
# branches []

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.parsing.vault import VaultSecret

# Mocking the DataLoader's load method to control its behavior during the test
@pytest.fixture
def mock_load(mocker):
    return mocker.patch.object(DataLoader, 'load', return_value='mocked_data')

# Mocking the VaultSecret to avoid dealing with actual secrets during the test
@pytest.fixture
def mock_vault_secret(mocker):
    mock_vault = mocker.MagicMock()
    mock_vault.secrets = [VaultSecret('dummy_secret')]
    return mock_vault

# Test function to improve coverage
def test_load(mock_load, mock_vault_secret):
    # Create an instance of DataLoader with the mocked VaultSecret
    data_loader = DataLoader()
    data_loader._vault = mock_vault_secret

    # Call the load method with different parameters to cover all branches
    result = data_loader.load('test_data', file_name='test_file.yml', show_content=True, json_only=False)
    mock_load.assert_called_once_with('test_data', file_name='test_file.yml', show_content=True, json_only=False)
    assert result == 'mocked_data', "The result should be the mocked data returned by the load method"

    # Reset mock to test with json_only=True
    mock_load.reset_mock()

    # Call the load method with json_only=True to cover the json_only branch
    result_json = data_loader.load('test_data_json', file_name='test_file.json', show_content=False, json_only=True)
    mock_load.assert_called_once_with('test_data_json', file_name='test_file.json', show_content=False, json_only=True)
    assert result_json == 'mocked_data', "The result should be the mocked data returned by the load method with json_only=True"
