# file lib/ansible/parsing/dataloader.py:75-76
# lines [75, 76]
# branches []

import pytest
from ansible.parsing.dataloader import DataLoader

# Test function to cover set_vault_secrets method
def test_set_vault_secrets(mocker):
    # Setup
    mock_vault = mocker.MagicMock()
    data_loader = DataLoader()
    data_loader._vault = mock_vault

    # Test DataLoader with mocked VaultLib
    test_secrets = [('test_cipher', 'test_secret')]
    data_loader.set_vault_secrets(test_secrets)

    # Assertions
    assert mock_vault.secrets == test_secrets, "Vault secrets were not set correctly"
