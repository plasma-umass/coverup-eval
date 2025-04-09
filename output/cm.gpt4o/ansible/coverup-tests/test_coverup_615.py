# file lib/ansible/plugins/loader.py:182-186
# lines [182, 183, 184, 185, 186]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the PluginLoadContext class is imported from ansible.plugins.loader
from ansible.plugins.loader import PluginLoadContext

@pytest.fixture
def plugin_load_context():
    context = PluginLoadContext()
    context.original_name = "original_plugin"
    return context

def test_redirect(plugin_load_context):
    redirect_name = "redirected_plugin"
    context = plugin_load_context.redirect(redirect_name)
    
    assert context.pending_redirect == redirect_name
    assert context.exit_reason == 'pending redirect resolution from original_plugin to redirected_plugin'
    assert context.resolved is False
    assert context is plugin_load_context
