# file lib/ansible/parsing/yaml/objects.py:304-305
# lines [304, 305]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    encrypted_data = AnsibleVaultEncryptedUnicode('  encrypted data ')
    yield encrypted_data
    # Teardown (nothing to do here since there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_lstrip(vault_encrypted_unicode):
    # Test lstrip with default chars (whitespace)
    stripped_data_default = vault_encrypted_unicode.lstrip()
    assert stripped_data_default == 'encrypted data '

    # Test lstrip with specific chars
    stripped_data_specific = vault_encrypted_unicode.lstrip(' e')
    assert stripped_data_specific == 'ncrypted data '
