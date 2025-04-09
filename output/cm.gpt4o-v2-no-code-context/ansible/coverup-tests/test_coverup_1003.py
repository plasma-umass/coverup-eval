# file: lib/ansible/parsing/ajson.py:18-42
# asked: {"lines": [35, 36, 37, 38, 40], "branches": [[34, 35], [36, 37], [36, 38], [39, 40]]}
# gained: {"lines": [35, 36, 37, 38, 40], "branches": [[34, 35], [36, 37], [39, 40]]}

import json
import pytest
from ansible.parsing.ajson import AnsibleJSONDecoder, VaultLib, AnsibleVaultEncryptedUnicode, wrap_var

def test_ansible_json_decoder_vault(monkeypatch):
    class MockVaultLib:
        def __init__(self, secrets):
            self.secrets = secrets

    class MockAnsibleVaultEncryptedUnicode:
        def __init__(self, value):
            self.value = value
            self.vault = None

    def mock_wrap_var(value):
        return f"wrapped_{value}"

    monkeypatch.setattr('ansible.parsing.ajson.VaultLib', MockVaultLib)
    monkeypatch.setattr('ansible.parsing.ajson.AnsibleVaultEncryptedUnicode', MockAnsibleVaultEncryptedUnicode)
    monkeypatch.setattr('ansible.parsing.ajson.wrap_var', mock_wrap_var)

    secrets = {'secret_key': 'secret_value'}
    AnsibleJSONDecoder.set_secrets(secrets)

    json_data = '{"__ansible_vault": "encrypted_value"}'
    decoder = AnsibleJSONDecoder()
    result = json.loads(json_data, cls=AnsibleJSONDecoder)

    assert isinstance(result, MockAnsibleVaultEncryptedUnicode)
    assert result.value == "encrypted_value"
    assert result.vault.secrets == secrets

def test_ansible_json_decoder_unsafe(monkeypatch):
    def mock_wrap_var(value):
        return f"wrapped_{value}"

    monkeypatch.setattr('ansible.parsing.ajson.wrap_var', mock_wrap_var)

    json_data = '{"__ansible_unsafe": "unsafe_value"}'
    decoder = AnsibleJSONDecoder()
    result = json.loads(json_data, cls=AnsibleJSONDecoder)

    assert result == "wrapped_unsafe_value"
