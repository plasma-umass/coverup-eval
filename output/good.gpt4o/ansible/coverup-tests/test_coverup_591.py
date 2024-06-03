# file lib/ansible/parsing/yaml/constructor.py:36-41
# lines [36, 37, 38, 39, 40, 41]
# branches []

import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.vault import VaultLib

def test_ansible_constructor_initialization(mocker):
    mock_vault_lib = mocker.patch('ansible.parsing.yaml.constructor.VaultLib', autospec=True)
    
    file_name = 'test_file.yml'
    vault_secrets = ['secret1', 'secret2']
    
    constructor = AnsibleConstructor(file_name=file_name, vault_secrets=vault_secrets)
    
    assert constructor._ansible_file_name == file_name
    assert constructor.vault_secrets == vault_secrets
    assert 'default' in constructor._vaults
    mock_vault_lib.assert_called_once_with(secrets=vault_secrets)
    
    # Clean up
    del constructor
