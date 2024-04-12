# file lib/ansible/plugins/loader.py:173-180
# lines [173, 174, 175, 176, 177, 178, 179, 180]
# branches []

import pytest
from ansible.plugins.loader import PluginLoadContext

def test_plugin_load_context_resolve():
    context = PluginLoadContext()
    resolved_name = "test_plugin"
    resolved_path = "/path/to/test_plugin"
    resolved_collection = "test_collection"
    exit_reason = "test_reason"

    # Call the resolve method which should be covered by the test
    result = context.resolve(resolved_name, resolved_path, resolved_collection, exit_reason)

    # Assertions to check if the resolve method works correctly
    assert result == context
    assert context.pending_redirect is None
    assert context.plugin_resolved_name == resolved_name
    assert context.plugin_resolved_path == resolved_path
    assert context.plugin_resolved_collection == resolved_collection
    assert context.exit_reason == exit_reason
    assert context.resolved is True
