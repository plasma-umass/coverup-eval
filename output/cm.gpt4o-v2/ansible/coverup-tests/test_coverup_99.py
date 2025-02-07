# file: lib/ansible/plugins/filter/encryption.py:20-43
# asked: {"lines": [20, 22, 23, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 41, 43], "branches": [[22, 23], [22, 25], [25, 26], [25, 28], [38, 39], [38, 41]]}
# gained: {"lines": [20, 22, 23, 25, 26, 28, 29, 30, 31, 32, 33, 35, 36, 38, 39, 41, 43], "branches": [[22, 23], [22, 25], [25, 26], [25, 28], [38, 39], [38, 41]]}

import pytest
from jinja2.runtime import Undefined
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.parsing.vault import VaultSecret, VaultLib
from ansible.module_utils._text import to_native, to_bytes
from ansible.module_utils.six import string_types, binary_type
from ansible.plugins.filter.encryption import do_vault

def test_do_vault_invalid_secret_type():
    with pytest.raises(AnsibleFilterTypeError, match="Secret passed is required to be a string"):
        do_vault("data", 123)

def test_do_vault_invalid_data_type():
    with pytest.raises(AnsibleFilterTypeError, match="Can only vault strings"):
        do_vault(123, "secret")

def test_do_vault_encryption_error(monkeypatch):
    def mock_encrypt(*args, **kwargs):
        raise Exception("Encryption failed")
    
    monkeypatch.setattr(VaultLib, "encrypt", mock_encrypt)
    
    with pytest.raises(AnsibleFilterError, match="Unable to encrypt: Encryption failed"):
        do_vault("data", "secret")

def test_do_vault_wrap_object():
    result = do_vault("data", "secret", wrap_object=True)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)

def test_do_vault_no_wrap_object():
    result = do_vault("data", "secret", wrap_object=False)
    assert isinstance(result, str)

def test_do_vault_success():
    result = do_vault("data", "secret")
    assert isinstance(result, str)
