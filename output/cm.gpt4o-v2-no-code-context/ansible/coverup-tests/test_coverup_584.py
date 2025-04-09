# file: lib/ansible/parsing/yaml/loader.py:29-33
# asked: {"lines": [29, 30, 31, 32, 33], "branches": []}
# gained: {"lines": [29, 30, 31, 32, 33], "branches": []}

import pytest
from ansible.parsing.yaml.loader import AnsibleLoader
from yaml.parser import Parser
from yaml.constructor import Constructor
from yaml.resolver import Resolver

class MockParser(Parser):
    def __init__(self, stream):
        self.stream = stream

class MockAnsibleConstructor(Constructor):
    def __init__(self, file_name=None, vault_secrets=None):
        self.file_name = file_name
        self.vault_secrets = vault_secrets

class MockResolver(Resolver):
    def __init__(self):
        pass

@pytest.fixture
def mock_classes(monkeypatch):
    monkeypatch.setattr('ansible.parsing.yaml.loader.Parser', MockParser)
    monkeypatch.setattr('ansible.parsing.yaml.loader.AnsibleConstructor', MockAnsibleConstructor)
    monkeypatch.setattr('ansible.parsing.yaml.loader.Resolver', MockResolver)

def test_ansible_loader_init(mock_classes):
    stream = "test_stream"
    file_name = "test_file"
    vault_secrets = "test_secrets"
    
    loader = AnsibleLoader(stream, file_name=file_name, vault_secrets=vault_secrets)
    
    assert loader.stream == stream
    assert loader.file_name == file_name
    assert loader.vault_secrets == vault_secrets
