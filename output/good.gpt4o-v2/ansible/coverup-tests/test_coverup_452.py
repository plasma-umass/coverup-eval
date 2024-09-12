# file: lib/ansible/parsing/yaml/objects.py:312-317
# asked: {"lines": [312, 313, 314, 315, 316, 317], "branches": [[313, 314], [313, 315], [315, 316], [315, 317]]}
# gained: {"lines": [312, 313, 314, 315, 316, 317], "branches": [[313, 314], [313, 315], [315, 316], [315, 317]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return ciphertext.decode('utf-8')

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode(b"secret data")
    obj.vault = MockVault()
    return obj

def test_replace_with_plain_strings(encrypted_unicode):
    encrypted_unicode._ciphertext = b"secret data"
    result = encrypted_unicode.replace("secret", "public")
    assert result == "public data"

def test_replace_with_encrypted_unicode(encrypted_unicode):
    encrypted_unicode._ciphertext = b"secret data"
    old = AnsibleVaultEncryptedUnicode(b"secret")
    old.vault = MockVault()
    new = AnsibleVaultEncryptedUnicode(b"public")
    new.vault = MockVault()
    result = encrypted_unicode.replace(old, new)
    assert result == "public data"

def test_replace_with_mixed_types(encrypted_unicode):
    encrypted_unicode._ciphertext = b"secret data"
    old = AnsibleVaultEncryptedUnicode(b"secret")
    old.vault = MockVault()
    result = encrypted_unicode.replace(old, "public")
    assert result == "public data"
    result = encrypted_unicode.replace("public", old)
    assert result == "secret data"
