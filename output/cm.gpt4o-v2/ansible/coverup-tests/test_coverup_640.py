# file: lib/ansible/plugins/loader.py:182-186
# asked: {"lines": [182, 183, 184, 185, 186], "branches": []}
# gained: {"lines": [182, 183, 184, 185, 186], "branches": []}

import pytest
from ansible.plugins.loader import PluginLoadContext

def test_plugin_load_context_redirect():
    context = PluginLoadContext()
    context.original_name = "original_plugin"
    
    result = context.redirect("new_plugin")
    
    assert context.pending_redirect == "new_plugin"
    assert context.exit_reason == "pending redirect resolution from original_plugin to new_plugin"
    assert context.resolved is False
    assert result is context
