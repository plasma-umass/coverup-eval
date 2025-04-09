# file: lib/ansible/parsing/yaml/objects.py:82-90
# asked: {"lines": [82, 83, 84, 85, 87, 88, 89, 90], "branches": [[84, 85], [84, 87]]}
# gained: {"lines": [82, 83, 84, 85, 87, 88, 89, 90], "branches": [[84, 85], [84, 87]]}

import pytest
from unittest.mock import Mock, patch
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    class AnsibleVaultError(Exception):
        pass

    def encrypt(self, seq, secret):
        return f"encrypted({seq})"

def test_from_plaintext_with_valid_vault():
    seq = "my_secret"
    secret = "password"
    vault = MockVault()

    avu = AnsibleVaultEncryptedUnicode.from_plaintext(seq, vault, secret)

    assert avu._ciphertext == b"encrypted(my_secret)"
    assert avu.vault == vault

def test_from_plaintext_with_invalid_vault():
    seq = "my_secret"
    secret = "password"
    vault = None

    with pytest.raises(AttributeError):
        AnsibleVaultEncryptedUnicode.from_plaintext(seq, vault, secret)
