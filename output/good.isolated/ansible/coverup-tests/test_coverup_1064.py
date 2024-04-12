# file lib/ansible/parsing/yaml/objects.py:134-135
# lines [134, 135]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_bytes

@pytest.fixture
def mock_to_native(mocker):
    return mocker.patch('ansible.parsing.yaml.objects.to_native', return_value='mocked_native_string')

def test_ansible_vault_encrypted_unicode_str(mock_to_native):
    # Setup the AnsibleVaultEncryptedUnicode object with some data
    ciphertext = 'encrypted_data'
    vault_encrypted_data = AnsibleVaultEncryptedUnicode(ciphertext)

    # Call the __str__ method to trigger the to_native function
    result = str(vault_encrypted_data)

    # Assert that the to_native function was called with the correct parameters
    mock_to_native.assert_called_once_with(ciphertext, errors='surrogate_or_strict')

    # Assert that the result of __str__ is the mocked native string
    assert result == 'mocked_native_string'

    # Clean up is handled by the fixture and pytest's garbage collection
