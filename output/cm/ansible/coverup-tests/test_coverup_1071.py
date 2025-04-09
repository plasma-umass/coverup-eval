# file lib/ansible/parsing/yaml/objects.py:265-266
# lines [265, 266]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    vault_str = AnsibleVaultEncryptedUnicode('vault')
    yield vault_str
    # Teardown (nothing to do here since there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_isascii(vault_encrypted_unicode):
    # Test with ASCII characters
    vault_encrypted_unicode.data = 'ascii_text'
    assert vault_encrypted_unicode.isascii() is True

    # Test with non-ASCII characters
    vault_encrypted_unicode.data = 'non-ascii_text_é'
    assert vault_encrypted_unicode.isascii() is False
