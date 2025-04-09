# file lib/ansible/plugins/lookup/config.py:107-115
# lines [107, 108, 109, 110, 111, 112, 113, 115]
# branches ['110->111', '110->115']

import pytest
from unittest.mock import patch
from ansible.plugins.lookup.config import _get_global_config
from ansible.errors import AnsibleLookupError
from ansible.module_utils.common.text.converters import to_native

class MissingSetting(Exception):
    def __init__(self, message, orig_exc=None):
        super().__init__(message)
        self.orig_exc = orig_exc

class MockC:
    VALID_SETTING = "valid_value"
    @staticmethod
    def INVALID_SETTING():
        pass

@pytest.fixture
def mock_ansible_constants(mocker):
    mocker.patch('ansible.plugins.lookup.config.C', new=MockC)

def test_get_global_config_valid_setting(mock_ansible_constants):
    result = _get_global_config('VALID_SETTING')
    assert result == "valid_value"

def test_get_global_config_invalid_setting_callable(mock_ansible_constants):
    with pytest.raises(AnsibleLookupError, match='Invalid setting "INVALID_SETTING" attempted'):
        _get_global_config('INVALID_SETTING')

def test_get_global_config_missing_setting(mock_ansible_constants, mocker):
    mocker.patch('ansible.plugins.lookup.config.MissingSetting', new=MissingSetting)
    with pytest.raises(MissingSetting) as excinfo:
        _get_global_config('MISSING_SETTING')
    assert to_native("type object 'MockC' has no attribute 'MISSING_SETTING'") in str(excinfo.value)
