# file: lib/ansible/plugins/loader.py:188-192
# asked: {"lines": [188, 189, 190, 191, 192], "branches": []}
# gained: {"lines": [188, 189, 190, 191, 192], "branches": []}

import pytest
from ansible.plugins.loader import PluginLoadContext

def test_nope_method():
    context = PluginLoadContext()
    
    # Call the nope method with a sample exit reason
    result = context.nope("Sample exit reason")
    
    # Assertions to verify the state changes
    assert context.pending_redirect is None
    assert context.exit_reason == "Sample exit reason"
    assert context.resolved is False
    assert result is context
