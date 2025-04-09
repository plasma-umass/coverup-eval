# file: lib/ansible/parsing/yaml/objects.py:271-272
# asked: {"lines": [271, 272], "branches": []}
# gained: {"lines": [271, 272], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode("12345")

def test_isdigit(encrypted_unicode):
    assert encrypted_unicode.isdigit() == True

def test_isdigit_with_non_digit(monkeypatch, encrypted_unicode):
    monkeypatch.setattr(encrypted_unicode, 'data', 'abcde')
    assert encrypted_unicode.isdigit() == False
