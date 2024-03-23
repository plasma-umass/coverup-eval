# file lib/ansible/parsing/yaml/objects.py:239-240
# lines [240]
# branches []

import sys
import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    encrypted_data = AnsibleVaultEncryptedUnicode('!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          663864396532363364626265666530633361646639663032313639346535613639\n          646566386664373466333261386433373737663564386430323862393261356237\n          0a363833')
    yield encrypted_data
    # Teardown (nothing to do here as there's no external resource to free)

def test_ansible_vault_encrypted_unicode_endswith(vault_encrypted_unicode):
    # Test the endswith method for coverage
    assert vault_encrypted_unicode.endswith('363833') == True
    assert vault_encrypted_unicode.endswith('invalid_suffix') == False
    assert vault_encrypted_unicode.endswith('363833', 0, 10) == False
    assert vault_encrypted_unicode.endswith('363833', 0, sys.maxsize) == True
