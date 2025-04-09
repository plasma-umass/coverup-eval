# file: lib/ansible/plugins/loader.py:134-147
# asked: {"lines": [136, 137, 139, 140, 141, 142, 143, 144, 145, 147], "branches": [[136, 137], [136, 139], [139, 140], [139, 147], [141, 142], [141, 143], [143, 144], [143, 145]]}
# gained: {"lines": [136, 137, 139, 140, 141, 142, 143, 144, 145, 147], "branches": [[136, 137], [136, 139], [139, 140], [139, 147], [141, 142], [141, 143], [143, 144], [143, 145]]}

import pytest
from ansible.plugins.loader import PluginLoadContext
from ansible.utils.collection_loader import AnsibleCollectionRef

@pytest.fixture
def plugin_load_context():
    return PluginLoadContext()

def test_resolved_fqcn_not_resolved(plugin_load_context):
    plugin_load_context.resolved = False
    assert plugin_load_context.resolved_fqcn is None

def test_resolved_fqcn_no_resolved_fqcn(plugin_load_context, mocker):
    plugin_load_context.resolved = True
    plugin_load_context._resolved_fqcn = None
    plugin_load_context.redirect_list = ['ansible.legacy.some_plugin']
    plugin_load_context.plugin_resolved_collection = 'test_collection'

    mocker.patch.object(AnsibleCollectionRef, 'is_valid_fqcr', return_value=True)

    assert plugin_load_context.resolved_fqcn == 'some_plugin'

def test_resolved_fqcn_with_resolved_fqcn(plugin_load_context):
    plugin_load_context.resolved = True
    plugin_load_context._resolved_fqcn = 'some_plugin'
    assert plugin_load_context.resolved_fqcn == 'some_plugin'

def test_resolved_fqcn_invalid_fqcr(plugin_load_context, mocker):
    plugin_load_context.resolved = True
    plugin_load_context._resolved_fqcn = None
    plugin_load_context.redirect_list = ['invalid_plugin']
    plugin_load_context.plugin_resolved_collection = 'test_collection'

    mocker.patch.object(AnsibleCollectionRef, 'is_valid_fqcr', return_value=False)

    assert plugin_load_context.resolved_fqcn == 'test_collection.invalid_plugin'
