# file lib/ansible/parsing/yaml/objects.py:170-173
# lines [171, 172, 173]
# branches ['171->172', '171->173']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_string():
    return AnsibleVaultEncryptedUnicode('encrypted_data')

def test_ansible_vault_encrypted_unicode_comparison_with_string(vault_string):
    assert vault_string <= 'encrypted_data'
    assert not (vault_string <= 'a_different_string')

def test_ansible_vault_encrypted_unicode_comparison_with_itself(vault_string):
    same_vault_string = AnsibleVaultEncryptedUnicode('encrypted_data')
    assert vault_string <= same_vault_string

def test_ansible_vault_encrypted_unicode_comparison_with_different_vault_string(vault_string):
    different_vault_string = AnsibleVaultEncryptedUnicode('different_encrypted_data')
    assert not (vault_string <= different_vault_string)
