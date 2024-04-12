# file lib/ansible/parsing/yaml/objects.py:271-272
# lines [271, 272]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    encrypted_data = AnsibleVaultEncryptedUnicode('!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          30313233343536373839616263646566\n          66656463626139616263646566616263\n          6162636465666768696a6b6c6d6e6f70\n          7172737475767778797a7a7a7a7a7a7a0a')
    yield encrypted_data
    # Teardown (nothing to do here since there's no external resource to free)

def test_ansible_vault_encrypted_unicode_isdigit(vault_encrypted_unicode):
    # Test with data that includes digits but is not purely digits
    assert not vault_encrypted_unicode.isdigit()

    # Test with data that is purely digits
    vault_encrypted_unicode.data = '1234567890'
    assert vault_encrypted_unicode.isdigit()

    # Test with data that contains no digits
    vault_encrypted_unicode.data = 'abcdefghij'
    assert not vault_encrypted_unicode.isdigit()
