# file: lib/ansible/inventory/host.py:161-162
# asked: {"lines": [161, 162], "branches": []}
# gained: {"lines": [161, 162], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.inventory.host import Host

@pytest.fixture
def host():
    host = Host()
    host.vars = {'var1': 'value1'}
    return host

def test_get_vars_merge_behavior(host, monkeypatch):
    def mock_combine_vars(a, b, merge=None):
        return {**a, **b}

    def mock_get_magic_vars():
        return {'magic_var1': 'magic_value1'}

    monkeypatch.setattr('ansible.utils.vars.combine_vars', mock_combine_vars)
    monkeypatch.setattr(host, 'get_magic_vars', mock_get_magic_vars)

    result = host.get_vars()
    assert result == {'var1': 'value1', 'magic_var1': 'magic_value1'}

def test_get_vars_no_merge_behavior(host, monkeypatch):
    def mock_combine_vars(a, b, merge=None):
        return {**a, **b}

    def mock_get_magic_vars():
        return {'magic_var1': 'magic_value1'}

    monkeypatch.setattr('ansible.utils.vars.combine_vars', mock_combine_vars)
    monkeypatch.setattr(host, 'get_magic_vars', mock_get_magic_vars)

    result = host.get_vars()
    assert result == {'var1': 'value1', 'magic_var1': 'magic_value1'}
