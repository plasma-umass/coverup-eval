# file: lib/ansible/parsing/yaml/constructor.py:36-41
# asked: {"lines": [36, 37, 38, 39, 40, 41], "branches": []}
# gained: {"lines": [36, 37, 38, 39, 40, 41], "branches": []}

import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.vault import VaultLib

@pytest.fixture
def mock_vault_lib(mocker):
    return mocker.patch('ansible.parsing.yaml.constructor.VaultLib')

def test_ansible_constructor_initialization_with_defaults(mock_vault_lib):
    constructor = AnsibleConstructor()
    assert constructor._ansible_file_name is None
    assert constructor.vault_secrets == []
    assert 'default' in constructor._vaults
    mock_vault_lib.assert_called_once_with(secrets=[])

def test_ansible_constructor_initialization_with_file_name(mock_vault_lib):
    file_name = 'test_file.yml'
    constructor = AnsibleConstructor(file_name=file_name)
    assert constructor._ansible_file_name == file_name
    assert constructor.vault_secrets == []
    assert 'default' in constructor._vaults
    mock_vault_lib.assert_called_once_with(secrets=[])

def test_ansible_constructor_initialization_with_vault_secrets(mock_vault_lib):
    vault_secrets = ['secret1', 'secret2']
    constructor = AnsibleConstructor(vault_secrets=vault_secrets)
    assert constructor._ansible_file_name is None
    assert constructor.vault_secrets == vault_secrets
    assert 'default' in constructor._vaults
    mock_vault_lib.assert_called_once_with(secrets=vault_secrets)

def test_ansible_constructor_initialization_with_all_params(mock_vault_lib):
    file_name = 'test_file.yml'
    vault_secrets = ['secret1', 'secret2']
    constructor = AnsibleConstructor(file_name=file_name, vault_secrets=vault_secrets)
    assert constructor._ansible_file_name == file_name
    assert constructor.vault_secrets == vault_secrets
    assert 'default' in constructor._vaults
    mock_vault_lib.assert_called_once_with(secrets=vault_secrets)
