# file: lib/ansible/plugins/filter/encryption.py:20-43
# asked: {"lines": [34], "branches": []}
# gained: {"lines": [34], "branches": []}

import pytest
from jinja2.exceptions import UndefinedError
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.plugins.filter.encryption import do_vault
from ansible.module_utils.six import string_types, binary_type

def test_do_vault_with_undefined_error(mocker):
    mocker.patch('ansible.parsing.vault.VaultLib.encrypt', side_effect=UndefinedError)
    with pytest.raises(UndefinedError):
        do_vault('data', 'secret')

def test_do_vault_with_ansible_filter_type_error_for_secret():
    with pytest.raises(AnsibleFilterTypeError, match="Secret passed is required to be a string, instead we got: <class 'int'>"):
        do_vault('data', 123)

def test_do_vault_with_ansible_filter_type_error_for_data():
    with pytest.raises(AnsibleFilterTypeError, match="Can only vault strings, instead we got: <class 'int'>"):
        do_vault(123, 'secret')

def test_do_vault_with_ansible_filter_error(mocker):
    mocker.patch('ansible.parsing.vault.VaultLib.encrypt', side_effect=Exception('encryption error'))
    with pytest.raises(AnsibleFilterError, match="Unable to encrypt: encryption error"):
        do_vault('data', 'secret')
