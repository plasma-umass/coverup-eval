# file: lib/ansible/plugins/loader.py:116-132
# asked: {"lines": [116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132], "branches": []}
# gained: {"lines": [116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132], "branches": []}

import pytest

from ansible.plugins.loader import PluginLoadContext

@pytest.fixture
def plugin_load_context():
    return PluginLoadContext()

def test_initial_state(plugin_load_context):
    plc = plugin_load_context
    assert plc.original_name is None
    assert plc.redirect_list == []
    assert plc.error_list == []
    assert plc.import_error_list == []
    assert plc.load_attempts == []
    assert plc.pending_redirect is None
    assert plc.exit_reason is None
    assert plc.plugin_resolved_path is None
    assert plc.plugin_resolved_name is None
    assert plc.plugin_resolved_collection is None
    assert plc.deprecated is False
    assert plc.removal_date is None
    assert plc.removal_version is None
    assert plc.deprecation_warnings == []
    assert plc.resolved is False
    assert plc._resolved_fqcn is None

def test_modify_state(plugin_load_context):
    plc = plugin_load_context
    plc.original_name = "test_name"
    plc.redirect_list.append("redirect")
    plc.error_list.append("error")
    plc.import_error_list.append("import_error")
    plc.load_attempts.append("attempt")
    plc.pending_redirect = "pending"
    plc.exit_reason = "exit"
    plc.plugin_resolved_path = "resolved_path"
    plc.plugin_resolved_name = "resolved_name"
    plc.plugin_resolved_collection = "resolved_collection"
    plc.deprecated = True
    plc.removal_date = "2023-10-01"
    plc.removal_version = "2.0"
    plc.deprecation_warnings.append("warning")
    plc.resolved = True
    plc._resolved_fqcn = "fqcn"

    assert plc.original_name == "test_name"
    assert plc.redirect_list == ["redirect"]
    assert plc.error_list == ["error"]
    assert plc.import_error_list == ["import_error"]
    assert plc.load_attempts == ["attempt"]
    assert plc.pending_redirect == "pending"
    assert plc.exit_reason == "exit"
    assert plc.plugin_resolved_path == "resolved_path"
    assert plc.plugin_resolved_name == "resolved_name"
    assert plc.plugin_resolved_collection == "resolved_collection"
    assert plc.deprecated is True
    assert plc.removal_date == "2023-10-01"
    assert plc.removal_version == "2.0"
    assert plc.deprecation_warnings == ["warning"]
    assert plc.resolved is True
    assert plc._resolved_fqcn == "fqcn"
