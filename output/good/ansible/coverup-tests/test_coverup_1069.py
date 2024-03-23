# file lib/ansible/parsing/yaml/objects.py:193-194
# lines [193, 194]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    avu = AnsibleVaultEncryptedUnicode('vault_encrypted_data')
    yield avu
    # Teardown (nothing to do here as there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_getitem(vault_encrypted_unicode):
    # Test __getitem__
    assert vault_encrypted_unicode[0] == 'v'
    assert vault_encrypted_unicode[1] == 'a'
    assert vault_encrypted_unicode[-1] == 'a'
    assert vault_encrypted_unicode[2:5] == 'ult'
    with pytest.raises(IndexError):
        _ = vault_encrypted_unicode[100]  # Accessing beyond the length of the data
