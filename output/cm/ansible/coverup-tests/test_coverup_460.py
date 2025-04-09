# file lib/ansible/parsing/yaml/objects.py:312-317
# lines [312, 313, 314, 315, 316, 317]
# branches ['313->314', '313->315', '315->316', '315->317']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_str():
    # Initialize with a string that contains 'old_data' for replacement
    return AnsibleVaultEncryptedUnicode('encrypted_old_data')

def test_ansible_vault_encrypted_unicode_replace_with_vault_objects(vault_str):
    # Create another AnsibleVaultEncryptedUnicode object to use in replace
    old_vault_str = AnsibleVaultEncryptedUnicode('old_data')
    new_vault_str = AnsibleVaultEncryptedUnicode('new_data')

    # Replace 'old_data' with 'new_data' in the original vault_str
    result = vault_str.replace(old_vault_str, new_vault_str)

    # Check that the result is a string and 'old_data' has been replaced with 'new_data'
    assert isinstance(result, str)
    assert 'new_data' in result
    assert 'old_data' not in result

def test_ansible_vault_encrypted_unicode_replace_with_strings(vault_str):
    # Replace 'encrypted' with 'decrypted' in the original vault_str
    result = vault_str.replace('encrypted', 'decrypted')

    # Check that the result is a string and 'encrypted' has been replaced with 'decrypted'
    assert isinstance(result, str)
    assert 'decrypted_old_data' in result
    assert 'encrypted_old_data' not in result
