# file: lib/ansible/parsing/yaml/constructor.py:36-41
# asked: {"lines": [36, 37, 38, 39, 40, 41], "branches": []}
# gained: {"lines": [36, 37, 38, 39, 40, 41], "branches": []}

import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.vault import VaultLib

def test_ansible_constructor_initialization():
    # Test with no parameters
    constructor = AnsibleConstructor()
    assert constructor._ansible_file_name is None
    assert constructor.vault_secrets == []
    assert isinstance(constructor._vaults['default'], VaultLib)
    assert constructor._vaults['default'].secrets == []

    # Test with file_name parameter
    constructor = AnsibleConstructor(file_name="test_file")
    assert constructor._ansible_file_name == "test_file"
    assert constructor.vault_secrets == []
    assert isinstance(constructor._vaults['default'], VaultLib)
    assert constructor._vaults['default'].secrets == []

    # Test with vault_secrets parameter
    secrets = ["secret1", "secret2"]
    constructor = AnsibleConstructor(vault_secrets=secrets)
    assert constructor._ansible_file_name is None
    assert constructor.vault_secrets == secrets
    assert isinstance(constructor._vaults['default'], VaultLib)
    assert constructor._vaults['default'].secrets == secrets

    # Test with both parameters
    constructor = AnsibleConstructor(file_name="test_file", vault_secrets=secrets)
    assert constructor._ansible_file_name == "test_file"
    assert constructor.vault_secrets == secrets
    assert isinstance(constructor._vaults['default'], VaultLib)
    assert constructor._vaults['default'].secrets == secrets
