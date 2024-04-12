# file lib/ansible/parsing/yaml/objects.py:327-328
# lines [327, 328]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    vault_str = AnsibleVaultEncryptedUnicode('encrypted_data')
    yield vault_str
    # Teardown
    # No teardown needed as we are not modifying any external state

def test_ansible_vault_encrypted_unicode_rjust(vault_encrypted_unicode):
    # Test the rjust method
    result = vault_encrypted_unicode.rjust(20, '*')
    assert result == "******encrypted_data", "The rjust method did not return the expected string"
