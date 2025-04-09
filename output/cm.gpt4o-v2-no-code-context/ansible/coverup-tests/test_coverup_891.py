# file: lib/ansible/parsing/yaml/objects.py:324-325
# asked: {"lines": [324, 325], "branches": []}
# gained: {"lines": [324, 325], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class TestAnsibleVaultEncryptedUnicode:
    
    @pytest.fixture
    def encrypted_unicode(self):
        class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
            def __init__(self, data):
                self._data = data
                self.vault = True  # Mocking the vault attribute

            @property
            def data(self):
                return self._data
        
        return MockAnsibleVaultEncryptedUnicode("This is a test string for AnsibleVaultEncryptedUnicode")

    def test_rindex(self, encrypted_unicode):
        # Test rindex with default start and end
        assert encrypted_unicode.rindex("test") == 10
        
        # Test rindex with specific start and end
        assert encrypted_unicode.rindex("test", 0, 20) == 10
        
        # Test rindex with start and end that do not include the substring
        with pytest.raises(ValueError):
            encrypted_unicode.rindex("test", 0, 5)
        
        # Test rindex with substring not present
        with pytest.raises(ValueError):
            encrypted_unicode.rindex("not_present")
