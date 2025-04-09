# file: lib/ansible/parsing/yaml/objects.py:262-263
# asked: {"lines": [262, 263], "branches": []}
# gained: {"lines": [262, 263], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode("encrypted_data")

def test_isalnum_true(monkeypatch, encrypted_unicode):
    # Mock the data property to return an alphanumeric string
    monkeypatch.setattr(encrypted_unicode.__class__, 'data', property(lambda self: "abc123"))
    assert encrypted_unicode.isalnum() is True

def test_isalnum_false(monkeypatch, encrypted_unicode):
    # Mock the data property to return a non-alphanumeric string
    monkeypatch.setattr(encrypted_unicode.__class__, 'data', property(lambda self: "abc 123"))
    assert encrypted_unicode.isalnum() is False
