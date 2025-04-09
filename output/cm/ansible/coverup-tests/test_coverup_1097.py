# file lib/ansible/parsing/yaml/objects.py:301-302
# lines [301, 302]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def ansible_vault_encrypted_unicode():
    # Setup
    encrypted_data = AnsibleVaultEncryptedUnicode('!vault |')
    encrypted_data._ciphertext = "ENCRYPTED DATA"
    yield encrypted_data
    # Teardown
    # No teardown needed as we are not modifying any external state

def test_ansible_vault_encrypted_unicode_lower(ansible_vault_encrypted_unicode):
    # Test the lower method of AnsibleVaultEncryptedUnicode
    result = ansible_vault_encrypted_unicode.lower()
    assert result == "encrypted data", "The lower method should return the lowercase version of the data"
