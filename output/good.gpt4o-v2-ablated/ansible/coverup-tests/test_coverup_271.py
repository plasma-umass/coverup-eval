# file: lib/ansible/plugins/loader.py:109-112
# asked: {"lines": [109, 110, 111, 112], "branches": []}
# gained: {"lines": [109, 110, 111, 112], "branches": []}

import pytest

from ansible.plugins.loader import PluginPathContext

@pytest.fixture
def plugin_path_context():
    return PluginPathContext('/some/path', True)

def test_plugin_path_context_initialization(plugin_path_context):
    assert plugin_path_context.path == '/some/path'
    assert plugin_path_context.internal is True

def test_plugin_path_context_internal_false(monkeypatch):
    context = PluginPathContext('/another/path', False)
    assert context.path == '/another/path'
    assert context.internal is False
