# file lib/ansible/parsing/yaml/objects.py:363-364
# lines [363, 364]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    avu = AnsibleVaultEncryptedUnicode('encrypted_data')
    yield avu
    # Teardown
    # No teardown needed as we are not modifying any external state

def test_ansible_vault_encrypted_unicode_zfill(vault_encrypted_unicode):
    # Test the zfill method
    width = 20
    result = vault_encrypted_unicode.zfill(width)
    assert result == 'encrypted_data'.zfill(width)
    assert len(result) == width
