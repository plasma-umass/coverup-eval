# file: lib/ansible/plugins/lookup/ini.py:92-119
# asked: {"lines": [92, 96, 97, 100, 101, 102, 105, 106, 107, 108, 111, 112, 113, 116, 119], "branches": [[102, 105], [102, 119], [105, 106], [105, 111], [106, 107], [106, 111], [107, 106], [107, 108], [111, 112], [111, 116]]}
# gained: {"lines": [92, 96, 97, 100, 101, 102, 105, 106, 107, 108, 111, 112, 113, 116, 119], "branches": [[102, 105], [102, 119], [105, 106], [105, 111], [106, 107], [106, 111], [107, 106], [107, 108], [111, 112], [111, 116]]}

import pytest
from collections import defaultdict
from ansible.plugins.lookup.ini import _parse_params

def test_parse_params_single_key():
    term = "key1=value1"
    paramvals = {"key1": "", "key2": ""}
    result = _parse_params(term, paramvals)
    assert result == ["key1=value1"]

def test_parse_params_multiple_keys():
    term = "key1=value1 key2=value2"
    paramvals = {"key1": "", "key2": ""}
    result = _parse_params(term, paramvals)
    assert result == ["key1=value1", "key2=value2"]

def test_parse_params_key_with_spaces():
    term = "key1=value1 some other value"
    paramvals = {"key1": "", "key2": ""}
    result = _parse_params(term, paramvals)
    assert result == ["key1=value1 some other value"]

def test_parse_params_update_key():
    term = "key1=value1 key1=updated"
    paramvals = {"key1": "", "key2": ""}
    result = _parse_params(term, paramvals)
    assert result == ["key1=value1 key1=updated"]

def test_parse_params_no_keys():
    term = "value1 value2"
    paramvals = {"key1": "", "key2": ""}
    result = _parse_params(term, paramvals)
    assert result == ["value1 value2"]

def test_parse_params_empty_term():
    term = ""
    paramvals = {"key1": "", "key2": ""}
    result = _parse_params(term, paramvals)
    assert result == []

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: monkeypatch any state or environment if needed
    yield
    # Teardown: clean up any state or environment if needed
