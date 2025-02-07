# file: lib/ansible/plugins/loader.py:134-147
# asked: {"lines": [134, 135, 136, 137, 139, 140, 141, 142, 143, 144, 145, 147], "branches": [[136, 137], [136, 139], [139, 140], [139, 147], [141, 142], [141, 143], [143, 144], [143, 145]]}
# gained: {"lines": [134, 135, 136, 137, 139, 140, 141, 142, 143, 144, 145, 147], "branches": [[136, 137], [136, 139], [139, 140], [141, 142], [141, 143], [143, 144], [143, 145]]}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.loader import PluginLoadContext
from ansible.utils.collection_loader import AnsibleCollectionRef

@pytest.fixture
def plugin_load_context():
    context = PluginLoadContext()
    context.resolved = False
    context._resolved_fqcn = None
    context.redirect_list = []
    context.plugin_resolved_collection = None
    return context

def test_resolved_fqcn_not_resolved(plugin_load_context):
    plugin_load_context.resolved = False
    assert plugin_load_context.resolved_fqcn is None

def test_resolved_fqcn_no_redirect_list(plugin_load_context):
    plugin_load_context.resolved = True
    plugin_load_context._resolved_fqcn = None
    plugin_load_context.redirect_list = []
    with pytest.raises(IndexError):
        plugin_load_context.resolved_fqcn

def test_resolved_fqcn_with_redirect_list(plugin_load_context, monkeypatch):
    plugin_load_context.resolved = True
    plugin_load_context._resolved_fqcn = None
    plugin_load_context.redirect_list = ['ansible.legacy.some_plugin']
    plugin_load_context.plugin_resolved_collection = None

    def mock_is_valid_fqcr(ref, ref_type=None):
        return ref == 'ansible.legacy.some_plugin'

    monkeypatch.setattr(AnsibleCollectionRef, 'is_valid_fqcr', mock_is_valid_fqcr)

    assert plugin_load_context.resolved_fqcn == 'some_plugin'

def test_resolved_fqcn_with_invalid_fqcr(plugin_load_context, monkeypatch):
    plugin_load_context.resolved = True
    plugin_load_context._resolved_fqcn = None
    plugin_load_context.redirect_list = ['some_plugin']
    plugin_load_context.plugin_resolved_collection = 'some_collection'

    def mock_is_valid_fqcr(ref, ref_type=None):
        return False

    monkeypatch.setattr(AnsibleCollectionRef, 'is_valid_fqcr', mock_is_valid_fqcr)

    assert plugin_load_context.resolved_fqcn == 'some_collection.some_plugin'
