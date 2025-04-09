# file: lib/ansible/parsing/yaml/objects.py:193-194
# asked: {"lines": [193, 194], "branches": []}
# gained: {"lines": [193, 194], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class TestAnsibleVaultEncryptedUnicode:
    
    @pytest.fixture
    def encrypted_unicode(self):
        class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
            def __init__(self, data):
                self._data = data
                self.vault = True  # Mock the vault attribute

            @property
            def data(self):
                return self._data
        
        return MockAnsibleVaultEncryptedUnicode(data="encrypted_data")

    def test_getitem(self, encrypted_unicode):
        assert encrypted_unicode[0] == "e"
        assert encrypted_unicode[1] == "n"
        assert encrypted_unicode[-1] == "a"
        assert encrypted_unicode[:] == "encrypted_data"
