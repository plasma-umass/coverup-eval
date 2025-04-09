# file lib/ansible/parsing/yaml/objects.py:253-254
# lines [253, 254]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockSequence:
    def __init__(self, data):
        self.data = data

class MockAnsibleBaseYAMLObject:
    pass

class TestAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode, MockSequence, MockAnsibleBaseYAMLObject):
    def __init__(self, data):
        MockSequence.__init__(self, data)
        MockAnsibleBaseYAMLObject.__init__(self)
        self.vault = None  # Mock attribute to avoid AttributeError

def test_format_map():
    # Arrange
    encrypted_unicode = TestAnsibleVaultEncryptedUnicode("Hello, {name}!")
    mapping = {"name": "World"}

    # Act
    result = encrypted_unicode.format_map(mapping)

    # Assert
    assert result == "Hello, World!"

    # Clean up
    del encrypted_unicode
