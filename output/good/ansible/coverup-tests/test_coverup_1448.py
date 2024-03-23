# file lib/ansible/parsing/yaml/objects.py:149-150
# lines [150]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    obj = AnsibleVaultEncryptedUnicode('12345')
    yield obj
    # Teardown
    # (No teardown needed in this case)

def test_ansible_vault_encrypted_unicode_int(vault_encrypted_unicode):
    # Test the __int__ method with default base
    assert int(vault_encrypted_unicode) == 12345
    # Test the __int__ method with base 8
    vault_encrypted_unicode.data = '12345'
    assert vault_encrypted_unicode.__int__(base=8) == 5349
    # Test the __int__ method with base 16
    vault_encrypted_unicode.data = '1a'
    assert vault_encrypted_unicode.__int__(base=16) == 26
