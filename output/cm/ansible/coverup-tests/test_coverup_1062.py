# file lib/ansible/parsing/yaml/objects.py:218-219
# lines [218, 219]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Assuming AnsibleVaultEncryptedUnicode can be instantiated with a string directly
    return AnsibleVaultEncryptedUnicode("encrypted_value_%s")

def test_ansible_vault_encrypted_unicode_mod(vault_encrypted_unicode):
    args = ("replacement",)
    result = vault_encrypted_unicode % args
    assert result == "encrypted_value_replacement"
