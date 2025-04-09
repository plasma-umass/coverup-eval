# file: lib/ansible/plugins/filter/encryption.py:20-43
# asked: {"lines": [34], "branches": []}
# gained: {"lines": [34], "branches": []}

import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.module_utils.six import string_types, binary_type
from jinja2.runtime import Undefined
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.parsing.vault import VaultSecret, VaultLib
from ansible.module_utils._text import to_native, to_bytes
from jinja2.exceptions import UndefinedError
from ansible.plugins.filter.encryption import do_vault

def test_do_vault_valid_string_secret():
    data = "my secret data"
    secret = "mysecret"
    result = do_vault(data, secret)
    assert isinstance(result, string_types)

def test_do_vault_valid_binary_secret():
    data = "my secret data"
    secret = b"mysecret"
    result = do_vault(data, secret)
    assert isinstance(result, string_types)

def test_do_vault_invalid_secret_type():
    data = "my secret data"
    secret = 12345
    with pytest.raises(AnsibleFilterTypeError):
        do_vault(data, secret)

def test_do_vault_invalid_data_type():
    data = 12345
    secret = "mysecret"
    with pytest.raises(AnsibleFilterTypeError):
        do_vault(data, secret)

def test_do_vault_wrap_object():
    data = "my secret data"
    secret = "mysecret"
    result = do_vault(data, secret, wrap_object=True)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)

def test_do_vault_undefined_error(mocker):
    data = "my secret data"
    secret = "mysecret"
    mocker.patch('ansible.parsing.vault.VaultLib.encrypt', side_effect=UndefinedError)
    with pytest.raises(UndefinedError):
        do_vault(data, secret)

def test_do_vault_general_exception(mocker):
    data = "my secret data"
    secret = "mysecret"
    mocker.patch('ansible.parsing.vault.VaultLib.encrypt', side_effect=Exception("Encryption failed"))
    with pytest.raises(AnsibleFilterError, match="Unable to encrypt: Encryption failed"):
        do_vault(data, secret)
