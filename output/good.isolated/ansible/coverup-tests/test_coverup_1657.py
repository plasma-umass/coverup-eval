# file lib/ansible/parsing/yaml/objects.py:208-211
# lines [209, 210, 211]
# branches ['209->210', '209->211']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

def test_ansible_vault_encrypted_unicode_radd_with_text_type(mocker):
    # Setup the AnsibleVaultEncryptedUnicode instance with some data
    vault_str = AnsibleVaultEncryptedUnicode('encrypted_data')

    # Mock the text_type to be str for the purpose of this test
    mocker.patch('ansible.parsing.yaml.objects.text_type', new=str)

    # Test __radd__ with a string (text_type)
    result = 'prefix_' + vault_str
    assert result == 'prefix_encrypted_data'

def test_ansible_vault_encrypted_unicode_radd_with_non_text_type(mocker):
    # Setup the AnsibleVaultEncryptedUnicode instance with some data
    vault_str = AnsibleVaultEncryptedUnicode('encrypted_data')

    # Mock the text_type to be str for the purpose of this test
    mocker.patch('ansible.parsing.yaml.objects.text_type', new=str)

    # Mock the to_text function to simply return the string representation of the object
    # Assuming the to_text function is supposed to return a native string type
    mocker.patch('ansible.parsing.yaml.objects.to_text', side_effect=lambda x: str(x) if not isinstance(x, bytes) else x.decode('utf-8'))

    # Test __radd__ with a non-text type (e.g., an integer)
    result = 123 + vault_str
    assert result == '123encrypted_data'
