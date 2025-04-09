# file: lib/ansible/plugins/loader.py:116-132
# asked: {"lines": [116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132], "branches": []}
# gained: {"lines": [116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132], "branches": []}

import pytest
from ansible.plugins.loader import PluginLoadContext

@pytest.fixture
def plugin_load_context():
    return PluginLoadContext()

def test_plugin_load_context_initialization(plugin_load_context):
    assert plugin_load_context.original_name is None
    assert plugin_load_context.redirect_list == []
    assert plugin_load_context.error_list == []
    assert plugin_load_context.import_error_list == []
    assert plugin_load_context.load_attempts == []
    assert plugin_load_context.pending_redirect is None
    assert plugin_load_context.exit_reason is None
    assert plugin_load_context.plugin_resolved_path is None
    assert plugin_load_context.plugin_resolved_name is None
    assert plugin_load_context.plugin_resolved_collection is None
    assert plugin_load_context.deprecated is False
    assert plugin_load_context.removal_date is None
    assert plugin_load_context.removal_version is None
    assert plugin_load_context.deprecation_warnings == []
    assert plugin_load_context.resolved is False
    assert plugin_load_context._resolved_fqcn is None
