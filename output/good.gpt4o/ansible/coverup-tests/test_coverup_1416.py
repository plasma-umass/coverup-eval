# file lib/ansible/parsing/ajson.py:18-42
# lines [35, 36, 37, 38, 40]
# branches ['34->35', '36->37', '36->38', '39->40']

import pytest
import json
from ansible.parsing.ajson import AnsibleJSONDecoder, VaultLib, AnsibleVaultEncryptedUnicode, wrap_var

@pytest.fixture
def mock_vault_lib(mocker):
    mock_vault = mocker.patch('ansible.parsing.ajson.VaultLib')
    return mock_vault

def test_ansible_json_decoder_vault(mock_vault_lib):
    secrets = 'mysecret'
    AnsibleJSONDecoder.set_secrets(secrets)
    
    json_data = '{"__ansible_vault": "encrypted_value"}'
    result = json.loads(json_data, cls=AnsibleJSONDecoder)
    
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault == mock_vault_lib.return_value

def test_ansible_json_decoder_unsafe():
    json_data = '{"__ansible_unsafe": "unsafe_value"}'
    result = json.loads(json_data, cls=AnsibleJSONDecoder)
    
    assert result == wrap_var("unsafe_value")
