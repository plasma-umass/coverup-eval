# file lib/ansible/parsing/yaml/objects.py:231-232
# lines [231, 232]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    encrypted_data = AnsibleVaultEncryptedUnicode('encrypted')
    yield encrypted_data
    # Teardown (nothing to do here since there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_center(vault_encrypted_unicode):
    # Test the center method
    centered_data = vault_encrypted_unicode.center(20, '-')
    assert centered_data == '-----encrypted------'
