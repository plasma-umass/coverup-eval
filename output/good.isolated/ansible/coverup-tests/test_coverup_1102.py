# file lib/ansible/parsing/yaml/objects.py:351-352
# lines [351, 352]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    encrypted_data = AnsibleVaultEncryptedUnicode('!vault |')
    yield encrypted_data
    # Teardown
    # No teardown needed as there is no external state change

def test_ansible_vault_encrypted_unicode_swapcase(vault_encrypted_unicode):
    # Precondition: The encrypted data should be lowercase
    assert vault_encrypted_unicode.data.islower()
    # Action: Use the swapcase method
    swapped_data = vault_encrypted_unicode.swapcase()
    # Postcondition: The swapped data should be uppercase
    assert swapped_data.isupper()
    # Verify that the swapcase method returns a new object
    assert swapped_data is not vault_encrypted_unicode
