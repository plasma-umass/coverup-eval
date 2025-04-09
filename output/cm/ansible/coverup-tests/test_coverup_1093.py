# file lib/ansible/parsing/yaml/objects.py:298-299
# lines [298, 299]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    encrypted_data = AnsibleVaultEncryptedUnicode('encrypted_data')
    yield encrypted_data
    # Teardown (nothing to do here since there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_ljust(vault_encrypted_unicode):
    width = 20
    fillchar = '*'
    result = vault_encrypted_unicode.ljust(width, fillchar)
    expected = 'encrypted_data'.ljust(width, fillchar)
    assert result == expected, "The ljust method did not return the expected left-justified string"
