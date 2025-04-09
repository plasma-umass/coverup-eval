# file lib/ansible/plugins/loader.py:116-132
# lines [116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]
# branches []

import pytest
from ansible.plugins.loader import PluginLoadContext

def test_plugin_load_context():
    context = PluginLoadContext()

    assert context.original_name is None
    assert context.redirect_list == []
    assert context.error_list == []
    assert context.import_error_list == []
    assert context.load_attempts == []
    assert context.pending_redirect is None
    assert context.exit_reason is None
    assert context.plugin_resolved_path is None
    assert context.plugin_resolved_name is None
    assert context.plugin_resolved_collection is None
    assert context.deprecated is False
    assert context.removal_date is None
    assert context.removal_version is None
    assert context.deprecation_warnings == []
    assert context.resolved is False
    assert context._resolved_fqcn is None
