# file: lib/ansible/plugins/loader.py:182-186
# asked: {"lines": [182, 183, 184, 185, 186], "branches": []}
# gained: {"lines": [182, 183, 184, 185, 186], "branches": []}

import pytest
from ansible.plugins.loader import PluginLoadContext

@pytest.fixture
def plugin_load_context():
    return PluginLoadContext()

def test_redirect(plugin_load_context):
    context = plugin_load_context
    context.original_name = "original_plugin"
    redirect_name = "redirected_plugin"
    
    result = context.redirect(redirect_name)
    
    assert result is context
    assert context.pending_redirect == redirect_name
    assert context.exit_reason == f'pending redirect resolution from {context.original_name} to {redirect_name}'
    assert context.resolved is False
