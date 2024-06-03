# file lib/ansible/plugins/loader.py:188-192
# lines [188, 189, 190, 191, 192]
# branches []

import pytest
from ansible.plugins.loader import PluginLoadContext

@pytest.fixture
def plugin_load_context():
    return PluginLoadContext()

def test_plugin_load_context_nope(plugin_load_context):
    context = plugin_load_context.nope("test_exit_reason")
    assert context.pending_redirect is None
    assert context.exit_reason == "test_exit_reason"
    assert context.resolved is False
