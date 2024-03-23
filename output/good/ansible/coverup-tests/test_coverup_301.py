# file lib/ansible/parsing/yaml/constructor.py:101-115
# lines [101, 102, 103, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115]
# branches ['107->108', '107->112']

import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor, ConstructorError
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from yaml import ScalarNode

@pytest.fixture
def mock_vault(mocker):
    mock_vault = mocker.MagicMock()
    mock_vault.secrets = None
    return mock_vault

@pytest.fixture
def constructor(mock_vault):
    constructor = AnsibleConstructor()
    constructor._vaults = {'default': mock_vault}
    return constructor

def test_construct_vault_encrypted_unicode_without_secrets(constructor, mocker):
    node = ScalarNode(tag='!vault', value='encrypted_data')
    # Mock the start_mark attribute to prevent AttributeError
    node.start_mark = mocker.Mock(column=0, line=0)
    with pytest.raises(ConstructorError) as excinfo:
        constructor.construct_vault_encrypted_unicode(node)
    assert "found !vault but no vault password provided" in str(excinfo.value)

def test_construct_vault_encrypted_unicode_with_secrets(constructor, mock_vault, mocker):
    mock_vault.secrets = 'fake_secrets'
    node = ScalarNode(tag='!vault', value='encrypted_data')
    # Mock the start_mark attribute to prevent AttributeError
    node.start_mark = mocker.Mock(column=0, line=0)
    result = constructor.construct_vault_encrypted_unicode(node)
    assert isinstance(result, AnsibleVaultEncryptedUnicode)
    assert result.vault == mock_vault
    # Since _node_position_info is not the focus of the test, we don't assert its value
