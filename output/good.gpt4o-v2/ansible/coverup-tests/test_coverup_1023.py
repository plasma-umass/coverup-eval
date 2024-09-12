# file: lib/ansible/parsing/yaml/objects.py:231-232
# asked: {"lines": [231, 232], "branches": []}
# gained: {"lines": [231, 232], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def encrypted_unicode():
    # Mocking the data property to return a known string
    class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
        @property
        def data(self):
            return "mocked data"
    
    return MockAnsibleVaultEncryptedUnicode("ciphertext")

def test_center(encrypted_unicode):
    centered_data = encrypted_unicode.center(20)
    assert centered_data == "    mocked data     "
