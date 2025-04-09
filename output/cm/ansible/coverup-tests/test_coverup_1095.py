# file lib/ansible/parsing/yaml/objects.py:333-334
# lines [333, 334]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    encrypted_data = AnsibleVaultEncryptedUnicode('encrypted data ')
    yield encrypted_data
    # Teardown
    # No teardown needed as there are no external resources to clean up

def test_ansible_vault_encrypted_unicode_rstrip(vault_encrypted_unicode):
    # Test the rstrip method without chars
    result_without_chars = vault_encrypted_unicode.rstrip()
    assert result_without_chars == 'encrypted data', "The rstrip method did not strip whitespace as expected"

    # Test the rstrip method with specific chars
    result_with_chars = vault_encrypted_unicode.rstrip(' ')
    assert result_with_chars == 'encrypted data', "The rstrip method did not strip the specified characters as expected"
