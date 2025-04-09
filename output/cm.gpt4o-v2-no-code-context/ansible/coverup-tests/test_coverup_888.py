# file: lib/ansible/parsing/yaml/objects.py:327-328
# asked: {"lines": [327, 328], "branches": []}
# gained: {"lines": [327, 328], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def encrypted_unicode():
    class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
        def __init__(self, data):
            self._data = data
            self.vault = True

        @property
        def data(self):
            return self._data

    return MockAnsibleVaultEncryptedUnicode("secret_data")

def test_rjust(encrypted_unicode):
    result = encrypted_unicode.rjust(20, '*')
    assert result == "*********secret_data"
