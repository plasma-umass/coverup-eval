# file: lib/ansible/context.py:38-56
# asked: {"lines": [51, 52, 53, 54, 55], "branches": [[49, 51], [51, 52], [51, 53], [53, 54], [53, 55]]}
# gained: {"lines": [51, 52, 53, 54, 55], "branches": [[49, 51], [51, 52], [51, 53], [53, 54], [53, 55]]}

import pytest
from unittest.mock import patch
from collections.abc import Mapping, Set

# Assuming CLIARGS is a global dictionary in the ansible.context module
CLIARGS = {}

def test_cliargs_deferred_get_no_shallowcopy(monkeypatch):
    from ansible.context import cliargs_deferred_get

    key = 'test_key'
    default_value = 'default'
    test_value = 'value'

    def mock_get(key, default=None):
        return test_value if key == 'test_key' else default

    monkeypatch.setattr('ansible.context.CLIARGS.get', mock_get)

    get_value = cliargs_deferred_get(key, default=default_value, shallowcopy=False)
    assert get_value() == test_value

def test_cliargs_deferred_get_default_no_shallowcopy(monkeypatch):
    from ansible.context import cliargs_deferred_get

    key = 'non_existent_key'
    default_value = 'default'

    def mock_get(key, default=None):
        return default

    monkeypatch.setattr('ansible.context.CLIARGS.get', mock_get)

    get_value = cliargs_deferred_get(key, default=default_value, shallowcopy=False)
    assert get_value() == default_value

def test_cliargs_deferred_get_shallowcopy_sequence(monkeypatch):
    from ansible.context import cliargs_deferred_get

    key = 'test_key'
    test_value = [1, 2, 3]

    def mock_get(key, default=None):
        return test_value if key == 'test_key' else default

    monkeypatch.setattr('ansible.context.CLIARGS.get', mock_get)

    get_value = cliargs_deferred_get(key, shallowcopy=True)
    result = get_value()
    assert result == test_value
    assert result is not test_value

def test_cliargs_deferred_get_shallowcopy_mapping(monkeypatch):
    from ansible.context import cliargs_deferred_get

    key = 'test_key'
    test_value = {'a': 1, 'b': 2}

    def mock_get(key, default=None):
        return test_value if key == 'test_key' else default

    monkeypatch.setattr('ansible.context.CLIARGS.get', mock_get)

    get_value = cliargs_deferred_get(key, shallowcopy=True)
    result = get_value()
    assert result == test_value
    assert result is not test_value

def test_cliargs_deferred_get_shallowcopy_set(monkeypatch):
    from ansible.context import cliargs_deferred_get

    key = 'test_key'
    test_value = {1, 2, 3}

    def mock_get(key, default=None):
        return test_value if key == 'test_key' else default

    monkeypatch.setattr('ansible.context.CLIARGS.get', mock_get)

    get_value = cliargs_deferred_get(key, shallowcopy=True)
    result = get_value()
    assert result == test_value
    assert result is not test_value

def test_cliargs_deferred_get_shallowcopy_other(monkeypatch):
    from ansible.context import cliargs_deferred_get

    key = 'test_key'
    test_value = 42

    def mock_get(key, default=None):
        return test_value if key == 'test_key' else default

    monkeypatch.setattr('ansible.context.CLIARGS.get', mock_get)

    get_value = cliargs_deferred_get(key, shallowcopy=True)
    assert get_value() == test_value

@pytest.fixture(autouse=True)
def cleanup():
    global CLIARGS
    CLIARGS.clear()
    yield
    CLIARGS.clear()
