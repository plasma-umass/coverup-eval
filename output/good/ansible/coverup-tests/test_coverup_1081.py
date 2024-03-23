# file lib/ansible/parsing/yaml/objects.py:158-159
# lines [158, 159]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # The AnsibleVaultEncryptedUnicode class does not accept 'data' as a keyword argument.
    # We need to pass the encrypted string directly to the constructor.
    encrypted_data = '!vault | $ANSIBLE_VAULT;1.1;AES256\n          30313233343536373839616263646566\n          66656463626139616263646566656463\n          6162636465666768696a6b6c6d6e6f70\n          7172737475767778797a7a7a7a7a7a7a\n'
    return AnsibleVaultEncryptedUnicode(encrypted_data)

def test_ansible_vault_encrypted_unicode_hash(vault_encrypted_unicode):
    # Verify that the __hash__ method is called and returns the correct hash
    assert isinstance(vault_encrypted_unicode, AnsibleVaultEncryptedUnicode)
    expected_hash = hash(str(vault_encrypted_unicode))
    actual_hash = hash(vault_encrypted_unicode)
    assert actual_hash == expected_hash, "The hash of the AnsibleVaultEncryptedUnicode object does not match the expected hash."
