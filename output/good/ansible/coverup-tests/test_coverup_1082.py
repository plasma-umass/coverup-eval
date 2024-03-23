# file lib/ansible/parsing/yaml/objects.py:221-222
# lines [221, 222]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def ansible_vault_encrypted_unicode():
    # Setup
    obj = AnsibleVaultEncryptedUnicode('ciphertext')
    yield obj
    # Teardown (nothing to do here since there's no external resource to clean up)

def test_ansible_vault_encrypted_unicode_rmod(ansible_vault_encrypted_unicode, mocker):
    # Mock the to_text function to return a simple string representation of the input
    mocker.patch('ansible.parsing.yaml.objects.to_text', return_value='decrypted_value_%s')
    
    # Create a template string to use the __rmod__ operation
    template = 'This is a %s'
    
    # Perform the __rmod__ operation
    result = template % ansible_vault_encrypted_unicode
    
    # Assert that the result is as expected
    assert result == 'This is a decrypted_value_%s'
