# file lib/ansible/parsing/yaml/constructor.py:36-41
# lines [36, 37, 38, 39, 40, 41]
# branches []

import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.vault import VaultLib

def test_ansible_constructor_initialization(mocker):
    # Mock the VaultLib to avoid side effects
    mock_vault_lib = mocker.patch('ansible.parsing.yaml.constructor.VaultLib')

    # Create an instance of AnsibleConstructor with a file name and vault secrets
    file_name = 'test_file.yml'
    vault_secrets = [('test_vault_id', 'test_secret')]
    ac = AnsibleConstructor(file_name=file_name, vault_secrets=vault_secrets)

    # Assertions to check if the AnsibleConstructor is initialized correctly
    assert ac._ansible_file_name == file_name
    assert ac.vault_secrets == vault_secrets
    mock_vault_lib.assert_called_once_with(secrets=vault_secrets)
    assert 'default' in ac._vaults
    assert isinstance(ac._vaults['default'], mock_vault_lib.return_value.__class__)

    # Test with no vault secrets provided
    ac_no_secrets = AnsibleConstructor(file_name=file_name)
    assert ac_no_secrets.vault_secrets == []
    mock_vault_lib.assert_called_with(secrets=[])

# Clean up is handled by pytest fixtures automatically, no additional code needed.
