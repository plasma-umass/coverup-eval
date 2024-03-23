# file lib/ansible/parsing/yaml/objects.py:286-287
# lines [287]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    ciphertext = "encrypted_data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    yield obj
    # Teardown
    # No specific teardown required for this test

def test_ansible_vault_encrypted_unicode_isspace(vault_encrypted_unicode):
    # Test with whitespace string
    vault_encrypted_unicode._ciphertext = "   "
    assert vault_encrypted_unicode.isspace() is True

    # Test with non-whitespace string
    vault_encrypted_unicode._ciphertext = "encrypted_data"
    assert vault_encrypted_unicode.isspace() is False
