# file lib/ansible/plugins/loader.py:182-186
# lines [182, 183, 184, 185, 186]
# branches []

import pytest
from ansible.plugins.loader import PluginLoadContext

def test_plugin_load_context_redirect():
    context = PluginLoadContext()
    context.original_name = "original_plugin"
    redirect_name = "redirected_plugin"
    
    # Perform the redirect
    result = context.redirect(redirect_name)
    
    # Assertions to verify postconditions
    assert result == context
    assert context.pending_redirect == redirect_name
    assert context.exit_reason == f"pending redirect resolution from {context.original_name} to {redirect_name}"
    assert context.resolved is False

    # Cleanup is not necessary here as the context is a local object and will be discarded after the test
