# file: lib/ansible/plugins/loader.py:173-180
# asked: {"lines": [173, 174, 175, 176, 177, 178, 179, 180], "branches": []}
# gained: {"lines": [173, 174, 175, 176, 177, 178, 179, 180], "branches": []}

import pytest
from ansible.plugins.loader import PluginLoadContext

@pytest.fixture
def plugin_load_context():
    return PluginLoadContext()

def test_resolve(plugin_load_context):
    resolved_name = "test_name"
    resolved_path = "/test/path"
    resolved_collection = "test_collection"
    exit_reason = "test_exit"

    result = plugin_load_context.resolve(resolved_name, resolved_path, resolved_collection, exit_reason)

    assert result is plugin_load_context
    assert plugin_load_context.pending_redirect is None
    assert plugin_load_context.plugin_resolved_name == resolved_name
    assert plugin_load_context.plugin_resolved_path == resolved_path
    assert plugin_load_context.plugin_resolved_collection == resolved_collection
    assert plugin_load_context.exit_reason == exit_reason
    assert plugin_load_context.resolved is True
