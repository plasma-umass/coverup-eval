# file: lib/ansible/plugins/filter/encryption.py:20-43
# asked: {"lines": [22, 23, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 41, 43], "branches": [[22, 23], [22, 25], [25, 26], [25, 28], [38, 39], [38, 41]]}
# gained: {"lines": [22, 23, 25, 26, 28, 29, 30, 31, 32, 33, 35, 36, 38, 39, 41, 43], "branches": [[22, 23], [22, 25], [25, 26], [25, 28], [38, 39], [38, 41]]}

import pytest
from ansible.plugins.filter.encryption import do_vault, AnsibleFilterTypeError, AnsibleFilterError
from ansible.parsing.vault import VaultSecret, VaultLib
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.errors import AnsibleError, AnsibleUndefinedVariable
from ansible.module_utils._text import to_bytes, to_native
from ansible.module_utils.six import string_types, binary_type

def test_do_vault_invalid_secret_type():
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        do_vault(data="some_data", secret=12345)
    assert "Secret passed is required to be a string" in str(excinfo.value)

def test_do_vault_invalid_data_type():
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        do_vault(data=12345, secret="some_secret")
    assert "Can only vault strings" in str(excinfo.value)

def test_do_vault_encryption_error(mocker):
    mocker.patch.object(VaultLib, 'encrypt', side_effect=Exception("encryption failed"))
    with pytest.raises(AnsibleFilterError) as excinfo:
        do_vault(data="some_data", secret="some_secret")
    assert "Unable to encrypt" in str(excinfo.value)
    assert "encryption failed" in str(excinfo.value.orig_exc)

def test_do_vault_wrap_object():
    result = do_vault(data="some_data", secret="some_secret", wrap_object=True)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)

def test_do_vault_no_wrap_object():
    result = do_vault(data="some_data", secret="some_secret", wrap_object=False)
    assert isinstance(result, string_types)
