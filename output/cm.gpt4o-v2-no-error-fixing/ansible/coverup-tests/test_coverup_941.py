# file: lib/ansible/parsing/yaml/objects.py:265-266
# asked: {"lines": [266], "branches": []}
# gained: {"lines": [266], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

def test_isascii():
    # Create an instance of AnsibleVaultEncryptedUnicode with ASCII data
    encrypted_unicode = AnsibleVaultEncryptedUnicode("ascii text")
    
    # Mock the data property to return an ASCII string
    encrypted_unicode.data = "ascii text"
    
    # Assert that isascii returns True for ASCII data
    assert encrypted_unicode.isascii() == True

    # Mock the data property to return a non-ASCII string
    encrypted_unicode.data = "non-ascii text ñ"
    
    # Assert that isascii returns False for non-ASCII data
    assert encrypted_unicode.isascii() == False
