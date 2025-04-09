# file lib/ansible/parsing/yaml/objects.py:280-281
# lines [281]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    obj = AnsibleVaultEncryptedUnicode(ciphertext="123")
    yield obj
    # Teardown
    # No specific teardown required for this test

def test_ansible_vault_encrypted_unicode_isnumeric(vault_encrypted_unicode):
    assert vault_encrypted_unicode.isnumeric() is True

    vault_encrypted_unicode.data = "abc"
    assert vault_encrypted_unicode.isnumeric() is False

    vault_encrypted_unicode.data = "123abc"
    assert vault_encrypted_unicode.isnumeric() is False

    vault_encrypted_unicode.data = ""
    assert vault_encrypted_unicode.isnumeric() is False
