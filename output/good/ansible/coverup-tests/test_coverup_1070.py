# file lib/ansible/parsing/yaml/objects.py:146-147
# lines [146, 147]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def ansible_vault_encrypted_unicode():
    return AnsibleVaultEncryptedUnicode(ciphertext='fake_ciphertext')

def test_ansible_vault_encrypted_unicode_repr(ansible_vault_encrypted_unicode):
    # Set the data attribute to control the output of __repr__
    ansible_vault_encrypted_unicode.data = 'fake_ciphertext'

    # Call __repr__ and assert it returns the expected representation
    result = repr(ansible_vault_encrypted_unicode)
    assert result == repr('fake_ciphertext')
