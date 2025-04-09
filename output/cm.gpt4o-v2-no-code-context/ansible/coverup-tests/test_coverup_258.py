# file: lib/ansible/parsing/yaml/constructor.py:101-115
# asked: {"lines": [101, 102, 103, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115], "branches": [[107, 108], [107, 112]]}
# gained: {"lines": [101, 102, 103, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115], "branches": [[107, 108], [107, 112]]}

import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.parsing.vault import VaultLib
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.utils.unsafe_proxy import to_bytes
import yaml
from yaml.constructor import ConstructorError
from yaml.reader import Reader
from yaml.scanner import Scanner
from yaml.parser import Parser
from yaml.composer import Composer
from yaml.resolver import Resolver

class MockVault:
    def __init__(self, secrets):
        self.secrets = secrets

@pytest.fixture
def constructor():
    constructor = AnsibleConstructor()
    constructor._vaults = {'default': MockVault(secrets=None)}
    return constructor

def test_construct_vault_encrypted_unicode_no_secrets(constructor):
    node = yaml.ScalarNode(tag='!vault', value='some_encrypted_value', start_mark=yaml.Mark('document', 0, 0, 0, 'buffer', 0))
    with pytest.raises(ConstructorError) as excinfo:
        constructor.construct_vault_encrypted_unicode(node)
    assert "found !vault but no vault password provided" in str(excinfo.value)

def test_construct_vault_encrypted_unicode_with_secrets(monkeypatch):
    def mock_to_bytes(value):
        return b'some_encrypted_value'

    monkeypatch.setattr('ansible.utils.unsafe_proxy.to_bytes', mock_to_bytes)

    constructor = AnsibleConstructor()
    constructor._vaults = {'default': MockVault(secrets='dummy_secret')}
    node = yaml.ScalarNode(tag='!vault', value='some_encrypted_value', start_mark=yaml.Mark('document', 0, 0, 0, 'buffer', 0))

    result = constructor.construct_vault_encrypted_unicode(node)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault == constructor._vaults['default']
    assert result.ansible_pos == constructor._node_position_info(node)
