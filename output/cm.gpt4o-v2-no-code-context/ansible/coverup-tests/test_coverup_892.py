# file: lib/ansible/parsing/yaml/objects.py:351-352
# asked: {"lines": [351, 352], "branches": []}
# gained: {"lines": [351, 352], "branches": []}

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

    return MockAnsibleVaultEncryptedUnicode

def test_swapcase(encrypted_unicode):
    instance = encrypted_unicode("sEcReT")
    result = instance.swapcase()
    assert result == "SeCrEt"
