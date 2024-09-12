# file: lib/ansible/parsing/yaml/dumper.py:45-46
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

import pytest
from ansible.parsing.yaml.dumper import AnsibleDumper, represent_vault_encrypted_unicode
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
import yaml
from io import StringIO

class MockAnsibleVaultEncryptedUnicode:
    def __init__(self, ciphertext):
        self._ciphertext = ciphertext

def test_represent_vault_encrypted_unicode():
    stream = StringIO()
    dumper = AnsibleDumper(stream)
    data = MockAnsibleVaultEncryptedUnicode(b"encrypted_data")
    
    # Manually call the function since it's not bound to the class
    result = represent_vault_encrypted_unicode(dumper, data)
    
    assert result.tag == u'!vault'
    assert result.value == "encrypted_data"
    assert result.style == '|'
