# file lib/ansible/plugins/filter/encryption.py:20-43
# lines [22, 23, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 41, 43]
# branches ['22->23', '22->25', '25->26', '25->28', '38->39', '38->41']

import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.utils.unsafe_proxy import wrap_var
from ansible.module_utils._text import to_bytes, to_native
from ansible.module_utils.six import string_types, binary_type
from ansible.template import Templar
from ansible.parsing.vault import VaultSecret, VaultLib

# Assuming the existence of the do_vault function in the encryption module
from ansible.plugins.filter.encryption import do_vault

def test_do_vault_with_valid_string_secret_and_data(mocker):
    secret = "my_secret"
    data = "my_data"
    vaultid = 'test_vault'
    salt = 'salt'
    wrap_object = True

    # Mocking the VaultLib to avoid actual encryption
    mock_vault_lib = mocker.MagicMock()
    mock_vault_lib.encrypt.return_value = b"encrypted_data"
    mocker.patch('ansible.plugins.filter.encryption.VaultLib', return_value=mock_vault_lib)

    # Call the function with valid parameters
    result = do_vault(data, secret, salt=salt, vaultid=vaultid, wrap_object=wrap_object)

    # Assertions to check if the result is an AnsibleVaultEncryptedUnicode object
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert str(result) == "encrypted_data"

def test_do_vault_with_valid_string_secret_and_data_no_wrap(mocker):
    secret = "my_secret"
    data = "my_data"
    vaultid = 'test_vault'
    salt = 'salt'
    wrap_object = False

    # Mocking the VaultLib to avoid actual encryption
    mock_vault_lib = mocker.MagicMock()
    mock_vault_lib.encrypt.return_value = b"encrypted_data"
    mocker.patch('ansible.plugins.filter.encryption.VaultLib', return_value=mock_vault_lib)

    # Call the function with valid parameters
    result = do_vault(data, secret, salt=salt, vaultid=vaultid, wrap_object=wrap_object)

    # Assertions to check if the result is a native string
    assert isinstance(result, str)
    assert result == "encrypted_data"

def test_do_vault_with_invalid_secret_type():
    secret = 123  # Not a valid string or binary type
    data = "my_data"
    with pytest.raises(AnsibleFilterTypeError):
        do_vault(data, secret)

def test_do_vault_with_invalid_data_type():
    secret = "my_secret"
    data = 123  # Not a valid string or binary type
    with pytest.raises(AnsibleFilterTypeError):
        do_vault(data, secret)

def test_do_vault_encryption_failure(mocker):
    secret = "my_secret"
    data = "my_data"
    vaultid = 'test_vault'
    salt = 'salt'

    # Mocking the VaultLib to raise an exception during encryption
    mock_vault_lib = mocker.MagicMock()
    mock_vault_lib.encrypt.side_effect = Exception("encryption failed")
    mocker.patch('ansible.plugins.filter.encryption.VaultLib', return_value=mock_vault_lib)

    with pytest.raises(AnsibleFilterError) as exc_info:
        do_vault(data, secret, salt=salt, vaultid=vaultid)

    assert "Unable to encrypt" in str(exc_info.value)
