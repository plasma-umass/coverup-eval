# file: lib/ansible/plugins/lookup/config.py:107-115
# asked: {"lines": [107, 108, 109, 110, 111, 112, 113, 115], "branches": [[110, 111], [110, 115]]}
# gained: {"lines": [107, 108, 109, 110, 111, 112, 113, 115], "branches": [[110, 111], [110, 115]]}

import pytest
from ansible.errors import AnsibleLookupError
from ansible.module_utils._text import to_native
from ansible.plugins.lookup.config import _get_global_config, MissingSetting

class MockConstants:
    VALID_CONFIG = "valid_value"
    INVALID_CONFIG = lambda: "invalid_value"

def test_get_global_config_valid(monkeypatch):
    monkeypatch.setattr("ansible.plugins.lookup.config.C", MockConstants)
    assert _get_global_config("VALID_CONFIG") == "valid_value"

def test_get_global_config_invalid_callable(monkeypatch):
    monkeypatch.setattr("ansible.plugins.lookup.config.C", MockConstants)
    with pytest.raises(AnsibleLookupError, match='Invalid setting "INVALID_CONFIG" attempted'):
        _get_global_config("INVALID_CONFIG")

def test_get_global_config_missing(monkeypatch):
    monkeypatch.setattr("ansible.plugins.lookup.config.C", MockConstants)
    with pytest.raises(MissingSetting):
        _get_global_config("MISSING_CONFIG")
