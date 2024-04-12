# file lib/ansible/parsing/yaml/objects.py:348-349
# lines [348, 349]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    encrypted_data = AnsibleVaultEncryptedUnicode('  encrypted  ')
    yield encrypted_data
    # Teardown (nothing to do here since there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_strip(vault_encrypted_unicode):
    # Test without chars
    stripped_data = vault_encrypted_unicode.strip()
    assert stripped_data == 'encrypted'

    # Test with specific chars
    encrypted_data_with_chars = AnsibleVaultEncryptedUnicode('xxencryptedxx')
    stripped_data_with_chars = encrypted_data_with_chars.strip('x')
    assert stripped_data_with_chars == 'encrypted'
