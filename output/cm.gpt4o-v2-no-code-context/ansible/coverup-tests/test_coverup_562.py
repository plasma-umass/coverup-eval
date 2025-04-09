# file: lib/ansible/plugins/loader.py:188-192
# asked: {"lines": [188, 189, 190, 191, 192], "branches": []}
# gained: {"lines": [188, 189, 190, 191, 192], "branches": []}

import pytest
from ansible.plugins.loader import PluginLoadContext

@pytest.fixture
def plugin_load_context():
    return PluginLoadContext()

def test_nope_method(plugin_load_context):
    context = plugin_load_context.nope("test_reason")
    assert context.exit_reason == "test_reason"
    assert context.pending_redirect is None
    assert context.resolved is False
    assert context is plugin_load_context
