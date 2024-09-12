# file: lib/ansible/parsing/ajson.py:18-42
# asked: {"lines": [35, 36, 37, 38, 40], "branches": [[34, 35], [36, 37], [36, 38], [39, 40]]}
# gained: {"lines": [35, 36, 37, 38, 40], "branches": [[34, 35], [36, 37], [39, 40]]}

import pytest
from ansible.parsing.ajson import AnsibleJSONDecoder
from ansible.parsing.vault import VaultLib
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.utils.unsafe_proxy import wrap_var

@pytest.fixture
def mock_vault_lib(mocker):
    mock_vault = mocker.patch('ansible.parsing.ajson.VaultLib')
    return mock_vault

def test_ansible_vault_encrypted_unicode(monkeypatch, mock_vault_lib):
    secrets = 'mysecret'
    AnsibleJSONDecoder.set_secrets(secrets)
    
    # Mock AnsibleVaultEncryptedUnicode
    mock_vault_unicode = mock_vault_lib.return_value
    monkeypatch.setattr('ansible.parsing.ajson.AnsibleVaultEncryptedUnicode', lambda x: mock_vault_unicode)
    
    decoder = AnsibleJSONDecoder()
    result = decoder.object_hook({'__ansible_vault': 'encrypted_value'})
    
    assert result == mock_vault_unicode
    assert result.vault == mock_vault_lib.return_value

def test_wrap_var(monkeypatch):
    value = 'unsafe_value'
    wrapped_value = wrap_var(value)
    
    decoder = AnsibleJSONDecoder()
    result = decoder.object_hook({'__ansible_unsafe': value})
    
    assert result == wrapped_value
