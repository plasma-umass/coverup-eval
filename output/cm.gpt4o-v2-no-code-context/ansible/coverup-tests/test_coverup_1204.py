# file: lib/ansible/parsing/ajson.py:18-42
# asked: {"lines": [], "branches": [[36, 38]]}
# gained: {"lines": [], "branches": [[36, 38]]}

import json
import pytest
from ansible.parsing.ajson import AnsibleJSONDecoder, VaultLib, AnsibleVaultEncryptedUnicode, wrap_var

@pytest.fixture
def mock_vault_lib(mocker):
    mock_vault = mocker.patch('ansible.parsing.ajson.VaultLib')
    return mock_vault

def test_ansible_json_decoder_with_vault(mock_vault_lib):
    secrets = 'mysecret'
    AnsibleJSONDecoder.set_secrets(secrets)
    
    json_data = '{"__ansible_vault": "encrypted_value"}'
    decoded_data = json.loads(json_data, cls=AnsibleJSONDecoder)
    
    assert isinstance(decoded_data, AnsibleVaultEncryptedUnicode)
    assert decoded_data.vault == AnsibleJSONDecoder._vaults['default']

def test_ansible_json_decoder_without_vault():
    json_data = '{"__ansible_vault": "encrypted_value"}'
    decoded_data = json.loads(json_data, cls=AnsibleJSONDecoder)
    
    assert isinstance(decoded_data, AnsibleVaultEncryptedUnicode)
    assert decoded_data.vault is None

def test_ansible_json_decoder_with_unsafe():
    json_data = '{"__ansible_unsafe": "unsafe_value"}'
    decoded_data = json.loads(json_data, cls=AnsibleJSONDecoder)
    
    assert decoded_data == wrap_var("unsafe_value")

def test_ansible_json_decoder_regular_key():
    json_data = '{"regular_key": "regular_value"}'
    decoded_data = json.loads(json_data, cls=AnsibleJSONDecoder)
    
    assert decoded_data == {"regular_key": "regular_value"}
