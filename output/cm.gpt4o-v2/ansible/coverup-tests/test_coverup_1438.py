# file: lib/ansible/parsing/ajson.py:18-42
# asked: {"lines": [], "branches": [[36, 38]]}
# gained: {"lines": [], "branches": [[36, 38]]}

import json
import pytest
from ansible.parsing.ajson import AnsibleJSONDecoder
from ansible.parsing.vault import VaultLib
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.utils.unsafe_proxy import wrap_var

@pytest.fixture
def vault_secrets():
    return ['mysecret']

@pytest.fixture
def json_decoder():
    return AnsibleJSONDecoder()

def test_ansible_vault_encrypted_unicode(monkeypatch, vault_secrets, json_decoder):
    # Set up the vault secrets
    AnsibleJSONDecoder.set_secrets(vault_secrets)
    
    # Create a JSON string that includes an Ansible vault encrypted value
    json_str = '{"__ansible_vault": "encrypted_value"}'
    
    # Mock the AnsibleVaultEncryptedUnicode to avoid actual encryption logic
    def mock_init(self, ciphertext):
        self.vault = None
        self._ciphertext = ciphertext
    
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, '__init__', mock_init)
    
    # Decode the JSON string
    result = json.loads(json_str, cls=AnsibleJSONDecoder)
    
    # Assert that the result is an instance of AnsibleVaultEncryptedUnicode
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result._ciphertext == "encrypted_value"
    assert result.vault == AnsibleJSONDecoder._vaults['default']

def test_ansible_vault_no_vaults(monkeypatch, json_decoder):
    # Ensure no vaults are set
    AnsibleJSONDecoder._vaults = {}
    
    # Create a JSON string that includes an Ansible vault encrypted value
    json_str = '{"__ansible_vault": "encrypted_value"}'
    
    # Mock the AnsibleVaultEncryptedUnicode to avoid actual encryption logic
    def mock_init(self, ciphertext):
        self.vault = None
        self._ciphertext = ciphertext
    
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, '__init__', mock_init)
    
    # Decode the JSON string
    result = json.loads(json_str, cls=AnsibleJSONDecoder)
    
    # Assert that the result is an instance of AnsibleVaultEncryptedUnicode
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result._ciphertext == "encrypted_value"
    assert result.vault is None

def test_ansible_unsafe(monkeypatch, json_decoder):
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    
    # Create a JSON string that includes an Ansible unsafe value
    json_str = '{"__ansible_unsafe": "unsafe_value"}'
    
    # Mock the AnsibleUnsafeText to avoid actual unsafe logic
    def mock_ansible_unsafe_text(value):
        return f"wrapped_{value}"
    
    monkeypatch.setattr('ansible.utils.unsafe_proxy.AnsibleUnsafeText', mock_ansible_unsafe_text)
    
    # Decode the JSON string
    result = json.loads(json_str, cls=AnsibleJSONDecoder)
    
    # Assert that the result is the wrapped value
    assert result == "wrapped_unsafe_value"
