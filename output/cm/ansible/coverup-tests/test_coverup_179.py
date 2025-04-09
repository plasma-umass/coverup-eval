# file lib/ansible/plugins/loader.py:134-147
# lines [134, 135, 136, 137, 139, 140, 141, 142, 143, 144, 145, 147]
# branches ['136->137', '136->139', '139->140', '139->147', '141->142', '141->143', '143->144', '143->145']

import pytest
from ansible.plugins.loader import PluginLoadContext
from ansible.utils.collection_loader import AnsibleCollectionRef

@pytest.fixture
def plugin_load_context():
    context = PluginLoadContext()
    context.resolved = True
    context.redirect_list = []
    context.plugin_resolved_collection = None
    return context

def test_resolved_fqcn_with_legacy_prefix(plugin_load_context):
    plugin_load_context.redirect_list = ['ansible.legacy.sample_plugin']
    assert plugin_load_context.resolved_fqcn == 'sample_plugin'

def test_resolved_fqcn_with_collection(plugin_load_context):
    plugin_load_context.redirect_list = ['some.collection.sample_plugin']
    plugin_load_context.plugin_resolved_collection = 'some.collection'
    assert plugin_load_context.resolved_fqcn == 'some.collection.sample_plugin'

def test_resolved_fqcn_without_collection(plugin_load_context):
    plugin_load_context.redirect_list = ['sample_plugin']
    plugin_load_context.plugin_resolved_collection = 'some.collection'
    assert plugin_load_context.resolved_fqcn == 'some.collection.sample_plugin'

def test_resolved_fqcn_not_resolved(plugin_load_context):
    plugin_load_context.resolved = False
    assert plugin_load_context.resolved_fqcn is None

def test_resolved_fqcn_already_set(plugin_load_context):
    plugin_load_context._resolved_fqcn = 'already.set.fqcn'
    assert plugin_load_context.resolved_fqcn == 'already.set.fqcn'
