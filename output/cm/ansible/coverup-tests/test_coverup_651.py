# file lib/ansible/plugins/loader.py:188-192
# lines [188, 189, 190, 191, 192]
# branches []

import pytest
from ansible.plugins.loader import PluginLoadContext

def test_plugin_load_context_nope():
    context = PluginLoadContext()
    exit_reason = "test_exit_reason"

    # Initialize attributes for the test
    context.pending_redirect = None
    context.exit_reason = None
    context.resolved = True

    result = context.nope(exit_reason)

    # After calling nope, ensure that the attributes are set correctly
    assert result.pending_redirect is None
    assert result.exit_reason == exit_reason
    assert result.resolved is False
