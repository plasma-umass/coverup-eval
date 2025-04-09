# file lib/ansible/parsing/yaml/objects.py:295-296
# lines [295, 296]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def ansible_vault_encrypted_unicode():
    # Setup
    avu = AnsibleVaultEncryptedUnicode(ciphertext="encrypted")
    yield avu
    # Teardown (nothing to do here as there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_join(ansible_vault_encrypted_unicode):
    seq = ['a', 'b', 'c']
    result = ansible_vault_encrypted_unicode.join(seq)
    assert result == 'aencryptedbencryptedc'
