# file: lib/ansible/plugins/loader.py:134-147
# asked: {"lines": [], "branches": [[139, 147]]}
# gained: {"lines": [], "branches": [[139, 147]]}

import pytest
from ansible.plugins.loader import PluginLoadContext
from ansible.utils.collection_loader import AnsibleCollectionRef

@pytest.fixture
def plugin_load_context():
    return PluginLoadContext()

def test_resolved_fqcn_with_redirect_list(plugin_load_context, mocker):
    mocker.patch.object(AnsibleCollectionRef, 'is_valid_fqcr', return_value=True)
    plugin_load_context.redirect_list = ['ansible.legacy.some_plugin']
    plugin_load_context.plugin_resolved_collection = 'some_collection'
    plugin_load_context._resolved_fqcn = None
    plugin_load_context.resolved = True

    result = plugin_load_context.resolved_fqcn

    assert result == 'some_plugin'
    assert plugin_load_context._resolved_fqcn == 'some_plugin'

def test_resolved_fqcn_with_invalid_fqcr(plugin_load_context, mocker):
    mocker.patch.object(AnsibleCollectionRef, 'is_valid_fqcr', return_value=False)
    plugin_load_context.redirect_list = ['some_plugin']
    plugin_load_context.plugin_resolved_collection = 'some_collection'
    plugin_load_context._resolved_fqcn = None
    plugin_load_context.resolved = True

    result = plugin_load_context.resolved_fqcn

    assert result == 'some_collection.some_plugin'
    assert plugin_load_context._resolved_fqcn == 'some_collection.some_plugin'

def test_resolved_fqcn_already_resolved(plugin_load_context):
    plugin_load_context._resolved_fqcn = 'already_resolved'
    plugin_load_context.resolved = True

    result = plugin_load_context.resolved_fqcn

    assert result == 'already_resolved'
