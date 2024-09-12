# file: lib/ansible/plugins/filter/encryption.py:46-70
# asked: {"lines": [48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68, 70], "branches": [[48, 49], [48, 51], [51, 52], [51, 54], [57, 58], [57, 60], [60, 61], [60, 68]]}
# gained: {"lines": [48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68, 70], "branches": [[48, 49], [48, 51], [51, 52], [51, 54], [57, 58], [57, 60], [60, 61], [60, 68]]}

import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.parsing.vault import VaultSecret, VaultLib, is_encrypted
from jinja2.runtime import Undefined
from jinja2.exceptions import UndefinedError
from unittest.mock import patch, MagicMock
from ansible.module_utils._text import to_bytes

from ansible.plugins.filter.encryption import do_unvault

def test_do_unvault_invalid_secret_type():
    with pytest.raises(AnsibleFilterTypeError, match="Secret passed is required to be as string"):
        do_unvault("vault", 123)

def test_do_unvault_invalid_vault_type():
    with pytest.raises(AnsibleFilterTypeError, match="Vault should be in the form of a string"):
        do_unvault(123, "secret")

def test_do_unvault_ansible_vault_encrypted_unicode():
    mock_vault = MagicMock(spec=AnsibleVaultEncryptedUnicode)
    mock_vault.data = "encrypted_data"
    secret = "secret"
    result = do_unvault(mock_vault, secret)
    assert result == "encrypted_data"
    assert mock_vault.vault is not None

def test_do_unvault_encrypted_vault():
    secret = "secret"
    encrypted_vault = "$ANSIBLE_VAULT;1.1;AES256"
    
    with patch("ansible.parsing.vault.VaultLib.decrypt", return_value="decrypted_data") as mock_decrypt:
        result = do_unvault(encrypted_vault, secret)
        mock_decrypt.assert_called_once_with(encrypted_vault)
        assert result == "decrypted_data"

def test_do_unvault_encrypted_vault_undefined_error():
    secret = "secret"
    encrypted_vault = "$ANSIBLE_VAULT;1.1;AES256"
    
    with patch("ansible.parsing.vault.VaultLib.decrypt", side_effect=UndefinedError):
        with pytest.raises(UndefinedError):
            do_unvault(encrypted_vault, secret)

def test_do_unvault_encrypted_vault_generic_error():
    secret = "secret"
    encrypted_vault = "$ANSIBLE_VAULT;1.1;AES256"
    
    with patch("ansible.parsing.vault.VaultLib.decrypt", side_effect=Exception("Decryption failed")):
        with pytest.raises(AnsibleFilterError, match="Unable to decrypt: Decryption failed"):
            do_unvault(encrypted_vault, secret)

def test_do_unvault_non_encrypted_vault():
    secret = "secret"
    vault = "non_encrypted_data"
    result = do_unvault(vault, secret)
    assert result == "non_encrypted_data"
