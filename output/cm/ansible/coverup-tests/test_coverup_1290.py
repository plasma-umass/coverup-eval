# file lib/ansible/parsing/yaml/objects.py:82-90
# lines [84, 85, 87, 88, 89, 90]
# branches ['84->85', '84->87']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

def test_ansible_vault_encrypted_unicode_from_plaintext_with_invalid_vault():
    invalid_vault = None
    secret = 'fake_secret'
    plaintext = 'fake_plaintext'

    with pytest.raises(AttributeError) as excinfo:
        AnsibleVaultEncryptedUnicode.from_plaintext(plaintext, invalid_vault, secret)
    
    assert "'NoneType' object has no attribute 'AnsibleVaultError'" in str(excinfo.value)
