# file: lib/ansible/plugins/lookup/config.py:107-115
# asked: {"lines": [108, 109, 110, 111, 112, 113, 115], "branches": [[110, 111], [110, 115]]}
# gained: {"lines": [108, 109, 110, 111, 112, 113, 115], "branches": [[110, 111], [110, 115]]}

import pytest
from ansible.plugins.lookup.config import _get_global_config, AnsibleLookupError, MissingSetting
from ansible import constants as C

def test_get_global_config_valid(monkeypatch):
    monkeypatch.setattr(C, 'VALID_CONFIG', 'some_value', raising=False)
    assert _get_global_config('VALID_CONFIG') == 'some_value'

def test_get_global_config_callable(monkeypatch):
    def mock_callable():
        return 'callable_value'
    monkeypatch.setattr(C, 'CALLABLE_CONFIG', mock_callable, raising=False)
    with pytest.raises(AnsibleLookupError, match='Invalid setting "CALLABLE_CONFIG" attempted'):
        _get_global_config('CALLABLE_CONFIG')

def test_get_global_config_missing(monkeypatch):
    monkeypatch.delattr(C, 'MISSING_CONFIG', raising=False)
    with pytest.raises(MissingSetting):
        _get_global_config('MISSING_CONFIG')
