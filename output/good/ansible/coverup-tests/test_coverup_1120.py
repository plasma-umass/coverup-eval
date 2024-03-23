# file lib/ansible/parsing/yaml/objects.py:253-254
# lines [253, 254]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def ansible_vault_encrypted_unicode():
    # Setup
    encrypted_data = AnsibleVaultEncryptedUnicode('!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          663864396532363364626265666530633361646639663032313639346535613639\n          6466396630323136393465356136396466396630323136393465356136390a6638\n          643965326333646262653665663030')
    yield encrypted_data
    # Teardown (if necessary)

def test_ansible_vault_encrypted_unicode_format_map(ansible_vault_encrypted_unicode):
    mapping = {'key': 'value'}
    result = ansible_vault_encrypted_unicode.format_map(mapping)
    assert result == ansible_vault_encrypted_unicode.data.format_map(mapping)
