# file: lib/ansible/plugins/filter/encryption.py:20-43
# asked: {"lines": [34], "branches": []}
# gained: {"lines": [34], "branches": []}

import pytest
from jinja2.exceptions import UndefinedError
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.module_utils.six import string_types, binary_type
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.parsing.vault import VaultSecret, VaultLib
from ansible.module_utils._text import to_bytes, to_native
from jinja2.runtime import Undefined
from ansible.plugins.filter.encryption import do_vault

def test_do_vault_with_undefined_error(mocker):
    mocker.patch('ansible.parsing.vault.VaultLib.encrypt', side_effect=UndefinedError)
    with pytest.raises(UndefinedError):
        do_vault('data', 'secret')

def test_do_vault_with_ansible_filter_type_error_for_secret():
    with pytest.raises(AnsibleFilterTypeError):
        do_vault('data', 123)

def test_do_vault_with_ansible_filter_type_error_for_data():
    with pytest.raises(AnsibleFilterTypeError):
        do_vault(123, 'secret')

def test_do_vault_with_ansible_filter_error(mocker):
    mocker.patch('ansible.parsing.vault.VaultLib.encrypt', side_effect=Exception('encryption error'))
    with pytest.raises(AnsibleFilterError) as excinfo:
        do_vault('data', 'secret')
    assert 'Unable to encrypt: encryption error' in str(excinfo.value)

def test_do_vault_success():
    result = do_vault('data', 'secret')
    assert isinstance(result, str)

def test_do_vault_wrap_object():
    result = do_vault('data', 'secret', wrap_object=True)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
