# file lib/ansible/parsing/yaml/objects.py:336-337
# lines [336, 337]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    encrypted_data = AnsibleVaultEncryptedUnicode('encrypted_value')
    yield encrypted_data
    # Teardown (nothing to do here since there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_split(vault_encrypted_unicode):
    # Test the split method without sep and maxsplit
    result = vault_encrypted_unicode.split()
    assert result == ['encrypted_value'], "The split method did not return the expected list"

    # Test the split method with sep
    vault_encrypted_unicode.data = 'encrypted value with spaces'
    result = vault_encrypted_unicode.split(sep=' ')
    assert result == ['encrypted', 'value', 'with', 'spaces'], "The split method did not split on spaces correctly"

    # Test the split method with maxsplit
    result = vault_encrypted_unicode.split(sep=' ', maxsplit=2)
    assert result == ['encrypted', 'value', 'with spaces'], "The split method did not honor the maxsplit argument"
