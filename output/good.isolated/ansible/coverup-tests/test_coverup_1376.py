# file lib/ansible/parsing/dataloader.py:129-140
# lines [133, 134]
# branches ['132->133']

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.parsing.vault import is_encrypted

# Mock the is_encrypted function to return False
@pytest.fixture
def mock_is_encrypted(mocker):
    mocker.patch('ansible.parsing.vault.is_encrypted', return_value=False)

def test_decrypt_if_vault_data_not_encrypted(mock_is_encrypted):
    # Create an instance of DataLoader
    data_loader = DataLoader()

    # Create a byte string that represents non-encrypted vault data
    b_vault_data = b"non-encrypted data"

    # Call the _decrypt_if_vault_data method with the non-encrypted data
    decrypted_data, show_content = data_loader._decrypt_if_vault_data(b_vault_data)

    # Assert that the decrypted_data is the same as the original non-encrypted data
    assert decrypted_data == b_vault_data

    # Assert that the show_content flag is True
    assert show_content is True
