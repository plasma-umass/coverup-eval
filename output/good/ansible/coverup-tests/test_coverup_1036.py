# file lib/ansible/module_utils/common/json.py:22-23
# lines [22, 23]
# branches []

import pytest
from ansible.module_utils.common.json import _is_vault

class MockVaultObject:
    __ENCRYPTED__ = True

@pytest.fixture
def mock_vault_object():
    return MockVaultObject()

def test_is_vault_with_vault_object(mock_vault_object):
    assert _is_vault(mock_vault_object) is True, "The _is_vault function should return True for vault objects"

def test_is_vault_with_non_vault_object():
    non_vault_object = object()
    assert _is_vault(non_vault_object) is False, "The _is_vault function should return False for non-vault objects"
