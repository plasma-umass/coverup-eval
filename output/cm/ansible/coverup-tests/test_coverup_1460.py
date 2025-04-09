# file lib/ansible/parsing/yaml/objects.py:221-222
# lines [222]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

def test_ansible_vault_encrypted_unicode_rmod(mocker):
    # Create a mock AnsibleVaultEncryptedUnicode object with a dummy ciphertext
    vault_str = AnsibleVaultEncryptedUnicode('dummy_ciphertext')
    
    # Mock the to_text function to return a specific string
    mock_to_text = mocker.patch('ansible.parsing.yaml.objects.to_text', side_effect=lambda x: x)
    
    # Perform the reverse modulo operation
    template = 'encrypted %s'
    result = vault_str.__rmod__(template)
    
    # Check that to_text was called with the correct arguments
    mock_to_text.assert_called_with(b'dummy_ciphertext')
    
    # Check the result of the reverse modulo operation
    assert result == template % 'dummy_ciphertext'
