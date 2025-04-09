# file: lib/ansible/parsing/utils/yaml.py:59-84
# asked: {"lines": [59, 64, 66, 68, 72, 73, 75, 76, 79, 80, 81, 82, 84], "branches": [[75, 76], [75, 79]]}
# gained: {"lines": [59, 64, 66, 68, 72, 73, 75, 76, 79, 80, 81, 82, 84], "branches": [[75, 76], [75, 79]]}

import pytest
from ansible.parsing.utils.yaml import from_yaml
from ansible.errors import AnsibleParserError
from ansible.parsing.yaml.objects import AnsibleUnicode
import json
import yaml

def test_from_yaml_json_success(monkeypatch):
    data = '{"key": "value"}'
    
    result = from_yaml(data)
    
    assert result == {"key": "value"}

def test_from_yaml_json_failure_yaml_success(monkeypatch):
    data = 'key: value'
    
    result = from_yaml(data)
    
    assert result == {"key": "value"}

def test_from_yaml_json_failure_yaml_failure(monkeypatch):
    data = 'key: value: another_value'
    
    with pytest.raises(AnsibleParserError):
        from_yaml(data)

def test_from_yaml_json_only_failure(monkeypatch):
    data = 'key: value'
    
    with pytest.raises(AnsibleParserError):
        from_yaml(data, json_only=True)

def test_from_yaml_with_vault_secrets(monkeypatch):
    data = '{"key": "value"}'
    vault_secrets = "dummy_secret"
    
    class MockAnsibleJSONDecoder:
        @staticmethod
        def set_secrets(secrets):
            assert secrets == vault_secrets
    
    monkeypatch.setattr('ansible.parsing.utils.yaml.AnsibleJSONDecoder', MockAnsibleJSONDecoder)
    
    result = from_yaml(data, vault_secrets=vault_secrets)
    
    assert result == {"key": "value"}

def test_from_yaml_with_file_name(monkeypatch):
    data = '{"key": "value"}'
    file_name = 'test_file'
    
    result = from_yaml(data, file_name=file_name)
    
    assert result == {"key": "value"}

def test_from_yaml_with_show_content(monkeypatch):
    data = 'key: value: another_value'
    
    with pytest.raises(AnsibleParserError):
        from_yaml(data, show_content=True)
