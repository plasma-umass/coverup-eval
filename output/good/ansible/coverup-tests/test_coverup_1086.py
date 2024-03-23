# file lib/ansible/parsing/yaml/objects.py:228-229
# lines [228, 229]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    encrypted_data = AnsibleVaultEncryptedUnicode('ENCRYPTED STRING')
    encrypted_data._decrypt_if_vault_encrypted = lambda: encrypted_data.data
    yield encrypted_data
    # Teardown (nothing to do here since there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_casefold(vault_encrypted_unicode):
    # Precondition: The encrypted data is a string that responds to casefold
    assert hasattr(vault_encrypted_unicode, 'casefold')

    # Action: Call the casefold method
    result = vault_encrypted_unicode.casefold()

    # Postcondition: The result should be the casefolded version of the decrypted string
    assert result == 'ENCRYPTED STRING'.casefold()
