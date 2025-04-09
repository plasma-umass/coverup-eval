# file: lib/ansible/plugins/filter/encryption.py:73-82
# asked: {"lines": [73, 74, 76, 77, 78, 79, 82], "branches": []}
# gained: {"lines": [73, 74, 76, 77, 78, 79, 82], "branches": []}

import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.parsing.vault import VaultSecret, VaultLib
from ansible.module_utils.six import string_types, binary_type
from ansible.module_utils._text import to_bytes, to_native
from jinja2.runtime import Undefined
from jinja2.exceptions import UndefinedError
from ansible.plugins.filter.encryption import FilterModule, do_vault, do_unvault

class TestFilterModule:
    
    def test_filters(self):
        filter_module = FilterModule()
        filters = filter_module.filters()
        assert 'vault' in filters
        assert 'unvault' in filters
        assert filters['vault'] == do_vault
        assert filters['unvault'] == do_unvault

class TestDoVault:
    
    def test_do_vault_valid(self):
        secret = 'mysecret'
        data = 'sensitive data'
        result = do_vault(data, secret)
        assert isinstance(result, string_types)
    
    def test_do_vault_invalid_secret_type(self):
        with pytest.raises(AnsibleFilterTypeError):
            do_vault('data', 123)
    
    def test_do_vault_invalid_data_type(self):
        with pytest.raises(AnsibleFilterTypeError):
            do_vault(123, 'secret')
    
    def test_do_vault_wrap_object(self):
        secret = 'mysecret'
        data = 'sensitive data'
        result = do_vault(data, secret, wrap_object=True)
        assert isinstance(result, AnsibleVaultEncryptedUnicode)

class TestDoUnvault:
    
    def test_do_unvault_valid(self):
        secret = 'mysecret'
        data = 'sensitive data'
        encrypted_data = do_vault(data, secret)
        result = do_unvault(encrypted_data, secret)
        assert result == data
    
    def test_do_unvault_invalid_secret_type(self):
        with pytest.raises(AnsibleFilterTypeError):
            do_unvault('vault', 123)
    
    def test_do_unvault_invalid_vault_type(self):
        with pytest.raises(AnsibleFilterTypeError):
            do_unvault(123, 'secret')
    
    def test_do_unvault_with_AnsibleVaultEncryptedUnicode(self):
        secret = 'mysecret'
        data = 'sensitive data'
        encrypted_data = do_vault(data, secret, wrap_object=True)
        result = do_unvault(encrypted_data, secret)
        assert result == data
