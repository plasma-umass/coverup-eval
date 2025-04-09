# file lib/ansible/parsing/yaml/objects.py:277-278
# lines [277, 278]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    obj = AnsibleVaultEncryptedUnicode('encrypted_data')
    yield obj
    # Teardown
    # No specific teardown required for this test

def test_ansible_vault_encrypted_unicode_islower(vault_encrypted_unicode):
    # Test with lowercase data
    vault_encrypted_unicode._ciphertext = "lowercase"
    assert vault_encrypted_unicode.islower() is True

    # Test with uppercase data
    vault_encrypted_unicode._ciphertext = "UPPERCASE"
    assert vault_encrypted_unicode.islower() is False

    # Test with mixed case data
    vault_encrypted_unicode._ciphertext = "MixedCase"
    assert vault_encrypted_unicode.islower() is False

    # Test with non-alphabetic characters
    vault_encrypted_unicode._ciphertext = "12345!@#$%"
    assert vault_encrypted_unicode.islower() is False
