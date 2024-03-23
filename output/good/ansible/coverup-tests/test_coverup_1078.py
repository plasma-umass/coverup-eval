# file lib/ansible/parsing/yaml/objects.py:268-269
# lines [268, 269]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Assuming AnsibleVaultEncryptedUnicode can be instantiated with a string directly
    return AnsibleVaultEncryptedUnicode('123')

def test_ansible_vault_encrypted_unicode_isdecimal(vault_encrypted_unicode):
    assert vault_encrypted_unicode.isdecimal() is True

    # Assuming AnsibleVaultEncryptedUnicode allows assignment to 'data' attribute
    vault_encrypted_unicode.data = 'abc'
    assert vault_encrypted_unicode.isdecimal() is False
