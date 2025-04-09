# file lib/ansible/parsing/dataloader.py:129-140
# lines [129, 132, 133, 134, 136, 137, 139, 140]
# branches ['132->133', '132->136']

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.parsing.vault import VaultLib, is_encrypted, parse_vaulttext_envelope

# Mocking the necessary VaultLib methods
@pytest.fixture
def mock_vault_lib(mocker):
    mock_vault = mocker.MagicMock(spec=VaultLib)
    mock_vault.decrypt.return_value = b'decrypted_data'
    return mock_vault

# Test function to cover the missing lines/branches
def test_decrypt_if_vault_data_with_encrypted_data(mock_vault_lib, mocker):
    # Mocking the is_encrypted function to return True
    mocker.patch('ansible.parsing.dataloader.is_encrypted', return_value=True)
    # Mocking the parse_vaulttext_envelope function to return expected values
    mocker.patch('ansible.parsing.dataloader.parse_vaulttext_envelope', return_value=(b'ciphertext', b'version', 'cipher_name', 'vault_id'))

    # Create an instance of DataLoader with the mocked VaultLib
    data_loader = DataLoader()
    data_loader._vault = mock_vault_lib

    # Encrypted data to be decrypted
    b_vault_data = b'encrypted_data'
    b_file_name = b'fake_file_name'

    # Call the method under test
    b_data, show_content = data_loader._decrypt_if_vault_data(b_vault_data, b_file_name)

    # Assertions to verify the postconditions
    assert b_data == b'decrypted_data'
    assert show_content is False
    # Verify that the decrypt method was called with the correct parameters
    mock_vault_lib.decrypt.assert_called_once_with(b_vault_data, filename=b_file_name)
