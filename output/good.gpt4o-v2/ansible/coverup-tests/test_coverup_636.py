# file: lib/ansible/plugins/loader.py:188-192
# asked: {"lines": [188, 189, 190, 191, 192], "branches": []}
# gained: {"lines": [188, 189, 190, 191, 192], "branches": []}

import pytest
from ansible.plugins.loader import PluginLoadContext

def test_nope_method():
    context = PluginLoadContext()
    exit_reason = "Test exit reason"
    
    result = context.nope(exit_reason)
    
    assert result is context
    assert context.pending_redirect is None
    assert context.exit_reason == exit_reason
    assert context.resolved is False
