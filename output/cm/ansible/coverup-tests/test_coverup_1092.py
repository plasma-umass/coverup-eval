# file lib/ansible/parsing/yaml/objects.py:360-361
# lines [360, 361]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Assuming AnsibleVaultEncryptedUnicode can be instantiated with a string directly
    return AnsibleVaultEncryptedUnicode('secret')

def test_ansible_vault_encrypted_unicode_upper(vault_encrypted_unicode):
    uppercased = vault_encrypted_unicode.upper()
    assert uppercased == 'SECRET'
