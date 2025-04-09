# file lib/ansible/parsing/yaml/objects.py:180-183
# lines [180, 181, 182, 183]
# branches ['181->182', '181->183']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_string():
    return AnsibleVaultEncryptedUnicode('encrypted_data')

def test_ansible_vault_encrypted_unicode_ge_with_vault_string(vault_string):
    other_vault_string = AnsibleVaultEncryptedUnicode('encrypted_data')
    assert vault_string >= other_vault_string

def test_ansible_vault_encrypted_unicode_ge_with_plain_string(vault_string):
    plain_string = 'encrypted_data'
    assert vault_string >= plain_string

def test_ansible_vault_encrypted_unicode_ge_with_higher_plain_string(vault_string):
    higher_plain_string = 'higher_encrypted_data'
    assert not vault_string >= higher_plain_string

def test_ansible_vault_encrypted_unicode_ge_with_lower_plain_string(vault_string):
    lower_plain_string = 'data'
    assert vault_string >= lower_plain_string
