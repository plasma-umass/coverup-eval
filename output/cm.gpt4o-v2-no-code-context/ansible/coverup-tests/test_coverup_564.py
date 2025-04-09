# file: lib/ansible/plugins/loader.py:182-186
# asked: {"lines": [182, 183, 184, 185, 186], "branches": []}
# gained: {"lines": [182, 183, 184, 185, 186], "branches": []}

import pytest
from unittest.mock import MagicMock

# Assuming the PluginLoadContext class is part of a module named loader
from ansible.plugins.loader import PluginLoadContext

@pytest.fixture
def plugin_load_context():
    context = PluginLoadContext()
    context.original_name = "original_plugin"
    context.pending_redirect = None
    context.exit_reason = None
    context.resolved = True
    return context

def test_redirect(plugin_load_context):
    redirect_name = "new_plugin"
    result = plugin_load_context.redirect(redirect_name)
    
    assert plugin_load_context.pending_redirect == redirect_name
    assert plugin_load_context.exit_reason == 'pending redirect resolution from original_plugin to new_plugin'
    assert plugin_load_context.resolved is False
    assert result is plugin_load_context
