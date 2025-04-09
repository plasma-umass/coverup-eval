# file: lib/ansible/parsing/yaml/constructor.py:101-115
# asked: {"lines": [101, 102, 103, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115], "branches": [[107, 108], [107, 112]]}
# gained: {"lines": [101, 102, 103, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115], "branches": [[107, 108], [107, 112]]}

import pytest
from yaml.constructor import ConstructorError
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from unittest.mock import Mock, patch

@pytest.fixture
def mock_vault():
    class MockVault:
        def __init__(self, secrets):
            self.secrets = secrets
    return MockVault

@pytest.fixture
def mock_node():
    class MockNode:
        def __init__(self, value, start_mark):
            self.value = value
            self.start_mark = start_mark
    return MockNode

@pytest.fixture
def mock_start_mark():
    class MockStartMark:
        def __init__(self, column, line, name):
            self.column = column
            self.line = line
            self.name = name
    return MockStartMark

def test_construct_vault_encrypted_unicode_success(mock_vault, mock_node, mock_start_mark):
    constructor = AnsibleConstructor()
    constructor.construct_scalar = Mock(return_value='encrypted_value')
    constructor._vaults = {'default': mock_vault(secrets='secret')}
    constructor._ansible_file_name = 'test_file'
    
    start_mark = mock_start_mark(column=0, line=0, name='test_file')
    node = mock_node('!vault encrypted_value', start_mark)
    
    result = constructor.construct_vault_encrypted_unicode(node)
    
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault == constructor._vaults['default']
    assert result.ansible_pos == ('test_file', 1, 1)

def test_construct_vault_encrypted_unicode_no_secrets(mock_vault, mock_node, mock_start_mark):
    constructor = AnsibleConstructor()
    constructor.construct_scalar = Mock(return_value='encrypted_value')
    constructor._vaults = {'default': mock_vault(secrets=None)}
    
    start_mark = mock_start_mark(column=0, line=0, name='test_file')
    node = mock_node('!vault encrypted_value', start_mark)
    
    with pytest.raises(ConstructorError, match="found !vault but no vault password provided"):
        constructor.construct_vault_encrypted_unicode(node)
