# file lib/ansible/parsing/yaml/objects.py:175-178
# lines [175, 176, 177, 178]
# branches ['176->177', '176->178']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_string():
    return AnsibleVaultEncryptedUnicode('encrypted_data')

def test_ansible_vault_encrypted_unicode_comparison_with_string(vault_string):
    assert vault_string > 'abc'  # Assuming 'encrypted_data' > 'abc'
    assert not (vault_string > 'zzz')  # Assuming 'encrypted_data' < 'zzz'

def test_ansible_vault_encrypted_unicode_comparison_with_itself(vault_string):
    same_vault_string = AnsibleVaultEncryptedUnicode('encrypted_data')
    different_vault_string = AnsibleVaultEncryptedUnicode('different_encrypted_data')
    assert not (vault_string > same_vault_string)  # Should not be greater than itself
    assert vault_string > different_vault_string  # Assuming 'encrypted_data' > 'different_encrypted_data'
