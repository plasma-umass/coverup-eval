# file lib/ansible/parsing/yaml/objects.py:250-251
# lines [250, 251]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

def test_ansible_vault_encrypted_unicode_format(mocker):
    class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
        def __init__(self, data):
            self._data = data
            self.vault = mocker.Mock()

        @property
        def data(self):
            return self._data

    encrypted_unicode = MockAnsibleVaultEncryptedUnicode("Hello, {}!")
    formatted_string = encrypted_unicode.format("World")
    
    assert formatted_string == "Hello, World!"
