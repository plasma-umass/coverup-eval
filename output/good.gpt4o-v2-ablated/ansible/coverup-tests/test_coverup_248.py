# file: lib/ansible/plugins/loader.py:182-186
# asked: {"lines": [182, 183, 184, 185, 186], "branches": []}
# gained: {"lines": [182, 183, 184, 185, 186], "branches": []}

import pytest

from ansible.plugins.loader import PluginLoadContext

@pytest.fixture
def plugin_load_context():
    context = PluginLoadContext()
    context.original_name = 'original_plugin'
    return context

def test_redirect(plugin_load_context):
    context = plugin_load_context.redirect('new_plugin')
    
    assert context.pending_redirect == 'new_plugin'
    assert context.exit_reason == 'pending redirect resolution from original_plugin to new_plugin'
    assert context.resolved is False

@pytest.fixture(autouse=True)
def cleanup_plugin_load_context(plugin_load_context):
    yield
    plugin_load_context.pending_redirect = None
    plugin_load_context.exit_reason = None
    plugin_load_context.resolved = None
