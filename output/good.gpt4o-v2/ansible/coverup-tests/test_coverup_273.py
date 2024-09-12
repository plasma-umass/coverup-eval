# file: lib/ansible/parsing/yaml/constructor.py:101-115
# asked: {"lines": [101, 102, 103, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115], "branches": [[107, 108], [107, 112]]}
# gained: {"lines": [101, 102, 103, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115], "branches": [[107, 108], [107, 112]]}

import pytest
from yaml.nodes import ScalarNode
from yaml.constructor import ConstructorError
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def __init__(self, secrets):
        self.secrets = secrets

class MockAnsibleConstructor(AnsibleConstructor):
    def __init__(self, vaults):
        self._vaults = vaults

    def construct_scalar(self, node):
        return node.value

    def _node_position_info(self, node):
        return ("mock_source", 1, 1)

@pytest.fixture
def mock_node():
    return ScalarNode(tag='!vault', value='mock_encrypted_value')

def test_construct_vault_encrypted_unicode_success(mock_node):
    vault = MockVault(secrets=True)
    constructor = MockAnsibleConstructor(vaults={'default': vault})
    
    result = constructor.construct_vault_encrypted_unicode(mock_node)
    
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault == vault
    assert result._data_source == "mock_source"
    assert result._line_number == 1
    assert result._column_number == 1

def test_construct_vault_encrypted_unicode_no_secrets(mock_node):
    vault = MockVault(secrets=None)
    constructor = MockAnsibleConstructor(vaults={'default': vault})
    
    with pytest.raises(ConstructorError) as excinfo:
        constructor.construct_vault_encrypted_unicode(mock_node)
    
    assert "found !vault but no vault password provided" in str(excinfo.value)
