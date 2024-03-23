# file lib/ansible/parsing/yaml/objects.py:137-138
# lines [137, 138]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_text

def test_ansible_vault_encrypted_unicode():
    # Create an instance of AnsibleVaultEncryptedUnicode with some dummy data
    vault_encrypted_data = AnsibleVaultEncryptedUnicode('encrypted_data')

    # Call the __unicode__ method to trigger the execution of the missing lines
    result = vault_encrypted_data.__unicode__()

    # Assert that the result is a text type and the content is correctly decoded
    assert isinstance(result, str)
    assert result == to_text(vault_encrypted_data.data, errors='surrogate_or_strict')
