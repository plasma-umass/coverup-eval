# file: lib/ansible/parsing/yaml/objects.py:221-222
# asked: {"lines": [221, 222], "branches": []}
# gained: {"lines": [221], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_text

def test_ansible_vault_encrypted_unicode_rmod():
    # Create an instance of AnsibleVaultEncryptedUnicode
    encrypted_unicode = AnsibleVaultEncryptedUnicode(b"encrypted_data")

    # Mock the data property to return a specific value
    encrypted_unicode.data = "decrypted_data"

    # Test the __rmod__ method
    template = "The secret is: %s"
    result = template % encrypted_unicode

    # Verify the result
    assert result == "The secret is: decrypted_data"
