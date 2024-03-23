# file lib/ansible/parsing/yaml/objects.py:225-226
# lines [225, 226]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    vault_str = AnsibleVaultEncryptedUnicode('secret')
    yield vault_str
    # Teardown (nothing to do here since there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_capitalize(vault_encrypted_unicode):
    capitalized = vault_encrypted_unicode.capitalize()
    assert capitalized == 'Secret', "The capitalize method should capitalize the first character"
