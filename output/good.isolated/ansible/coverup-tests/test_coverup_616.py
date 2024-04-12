# file lib/ansible/parsing/yaml/objects.py:165-168
# lines [165, 166, 167, 168]
# branches ['166->167', '166->168']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_string():
    return AnsibleVaultEncryptedUnicode('encrypted_data')

def test_ansible_vault_encrypted_unicode_comparison_with_string(vault_string):
    assert vault_string < 'zzz'  # 'encrypted_data' is less than 'zzz'
    assert not (vault_string < 'aaa')  # 'encrypted_data' is not less than 'aaa'

def test_ansible_vault_encrypted_unicode_comparison_with_itself(vault_string):
    other_vault_string = AnsibleVaultEncryptedUnicode('encrypted_data')
    assert not (vault_string < other_vault_string)  # Both have the same 'data'

def test_ansible_vault_encrypted_unicode_comparison_with_other_vault_string(vault_string):
    other_vault_string = AnsibleVaultEncryptedUnicode('zzz')
    assert vault_string < other_vault_string  # 'encrypted_data' is less than 'zzz'
    other_vault_string = AnsibleVaultEncryptedUnicode('aaa')
    assert not (vault_string < other_vault_string)  # 'encrypted_data' is not less than 'aaa'
