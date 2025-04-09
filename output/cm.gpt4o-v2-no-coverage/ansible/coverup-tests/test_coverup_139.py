# file: lib/ansible/parsing/ajson.py:18-42
# asked: {"lines": [18, 20, 22, 23, 24, 26, 27, 28, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 42], "branches": [[31, 32], [31, 42], [34, 35], [34, 39], [36, 37], [36, 38], [39, 31], [39, 40]]}
# gained: {"lines": [18, 20, 22, 23, 24, 26, 27, 28, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 42], "branches": [[31, 32], [31, 42], [34, 35], [34, 39], [36, 37], [39, 31], [39, 40]]}

import pytest
import json
from ansible.parsing.ajson import AnsibleJSONDecoder
from ansible.parsing.vault import VaultLib
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.utils.unsafe_proxy import wrap_var

def test_ansible_json_decoder_init(monkeypatch):
    def mock_object_hook(pairs):
        return pairs

    monkeypatch.setattr(AnsibleJSONDecoder, 'object_hook', mock_object_hook)
    decoder = AnsibleJSONDecoder()
    assert decoder.object_hook.__func__ == mock_object_hook

def test_ansible_json_decoder_set_secrets():
    secrets = 'mysecret'
    AnsibleJSONDecoder.set_secrets(secrets)
    assert 'default' in AnsibleJSONDecoder._vaults
    assert isinstance(AnsibleJSONDecoder._vaults['default'], VaultLib)

def test_ansible_json_decoder_object_hook_vault(monkeypatch):
    secrets = 'mysecret'
    AnsibleJSONDecoder.set_secrets(secrets)
    
    pairs = {'__ansible_vault': 'encrypted_value'}
    decoder = AnsibleJSONDecoder()
    result = decoder.object_hook(pairs)
    
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault == AnsibleJSONDecoder._vaults['default']

def test_ansible_json_decoder_object_hook_unsafe():
    pairs = {'__ansible_unsafe': 'unsafe_value'}
    decoder = AnsibleJSONDecoder()
    result = decoder.object_hook(pairs)
    
    assert result == wrap_var('unsafe_value')

def test_ansible_json_decoder_object_hook_normal():
    pairs = {'normal_key': 'normal_value'}
    decoder = AnsibleJSONDecoder()
    result = decoder.object_hook(pairs)
    
    assert result == pairs
