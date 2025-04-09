# file: lib/ansible/plugins/filter/encryption.py:20-43
# asked: {"lines": [20, 22, 23, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 41, 43], "branches": [[22, 23], [22, 25], [25, 26], [25, 28], [38, 39], [38, 41]]}
# gained: {"lines": [20, 22, 23, 25, 26, 28, 29, 30, 31, 32, 33, 35, 36, 38, 39, 41, 43], "branches": [[22, 23], [22, 25], [25, 26], [25, 28], [38, 39], [38, 41]]}

import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.module_utils._text import to_native, to_bytes
from ansible.module_utils.six import string_types, binary_type
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.parsing.vault import VaultSecret, VaultLib
from jinja2.runtime import Undefined
from jinja2.exceptions import UndefinedError
from unittest.mock import patch

from ansible.plugins.filter.encryption import do_vault

def test_do_vault_with_string_secret():
    secret = "mysecret"
    data = "sensitive data"
    result = do_vault(data, secret)
    assert isinstance(result, str)

def test_do_vault_with_binary_secret():
    secret = b"mysecret"
    data = "sensitive data"
    result = do_vault(data, secret)
    assert isinstance(result, str)

def test_do_vault_with_undefined_secret():
    secret = Undefined(name='secret')
    data = "sensitive data"
    result = do_vault(data, secret)
    assert isinstance(result, str)

def test_do_vault_with_invalid_secret_type():
    secret = 12345
    data = "sensitive data"
    with pytest.raises(AnsibleFilterTypeError):
        do_vault(data, secret)

def test_do_vault_with_invalid_data_type():
    secret = "mysecret"
    data = 12345
    with pytest.raises(AnsibleFilterTypeError):
        do_vault(data, secret)

def test_do_vault_encryption_error():
    secret = "mysecret"
    data = "sensitive data"
    with patch.object(VaultLib, 'encrypt', side_effect=Exception("encryption failed")):
        with pytest.raises(AnsibleFilterError):
            do_vault(data, secret)

def test_do_vault_with_wrap_object():
    secret = "mysecret"
    data = "sensitive data"
    result = do_vault(data, secret, wrap_object=True)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)

def test_do_vault_with_salt():
    secret = "mysecret"
    data = "sensitive data"
    salt = "random_salt"
    result = do_vault(data, secret, salt=salt)
    assert isinstance(result, str)

def test_do_vault_with_vaultid():
    secret = "mysecret"
    data = "sensitive data"
    vaultid = "custom_vault_id"
    result = do_vault(data, secret, vaultid=vaultid)
    assert isinstance(result, str)

def test_do_vault_with_undefined_data():
    secret = "mysecret"
    data = Undefined(name='data')
    result = do_vault(data, secret)
    assert isinstance(result, str)
