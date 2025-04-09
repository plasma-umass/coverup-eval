# file: lib/ansible/plugins/loader.py:657-759
# asked: {"lines": [664, 693, 694, 703, 708, 709, 734, 736, 739, 740, 742, 743, 744, 746, 747, 748, 749, 750, 751, 752, 755, 756, 757, 759], "branches": [[663, 664], [685, 739], [702, 703], [714, 717], [717, 720], [720, 723], [723, 696], [739, 740], [739, 755], [742, 743], [742, 755], [744, 746], [744, 748], [756, 757], [756, 759]]}
# gained: {"lines": [664, 739, 740, 742, 755, 756, 757], "branches": [[663, 664], [685, 739], [739, 740], [742, 755], [756, 757]]}

import pytest
import os
from unittest.mock import MagicMock, patch
from ansible.plugins.loader import PluginLoader
from ansible.utils.collection_loader import AnsibleCollectionRef
from ansible.module_utils._text import to_bytes, to_text, to_native

class MockDisplay:
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def deprecated(self, msg):
        pass

@pytest.fixture
def plugin_loader():
    loader = PluginLoader(class_name='test', package='test_package', config=None, subdir='modules')
    loader._plugin_path_cache = {'': {}, '.py': {}}
    loader._searched_paths = set()
    loader._get_paths_with_context = MagicMock(return_value=[])
    loader.aliases = {}
    return loader

@pytest.fixture
def plugin_load_context():
    class PluginLoadContext:
        def __init__(self):
            self.resolved = False
            self.plugin_resolved_path = None
            self.plugin_resolved_name = None
            self.plugin_resolved_collection = None
            self.load_attempts = []

        def nope(self, msg):
            return self

    return PluginLoadContext()

def test_find_plugin_legacy_cache_hit(plugin_loader, plugin_load_context):
    plugin_loader._plugin_path_cache['.py']['test_plugin'] = MagicMock(path='test_path', internal=True)
    result = plugin_loader._find_plugin_legacy('test_plugin', plugin_load_context, suffix='.py')
    assert result.resolved
    assert result.plugin_resolved_path == 'test_path'
    assert result.plugin_resolved_name == 'test_plugin'
    assert result.plugin_resolved_collection == 'ansible.builtin'

def test_find_plugin_legacy_cache_miss(plugin_loader, plugin_load_context):
    with patch('os.path.isdir', return_value=True), \
         patch('os.listdir', return_value=[b'test_plugin.py']), \
         patch('os.path.isfile', return_value=True), \
         patch('ansible.plugins.loader.display', new_callable=MockDisplay):
        plugin_loader._get_paths_with_context = MagicMock(return_value=[MagicMock(path='test_path', internal=True)])
        result = plugin_loader._find_plugin_legacy('test_plugin', plugin_load_context, suffix='.py')
        assert result.resolved
        assert result.plugin_resolved_path == 'test_path/test_plugin.py'
        assert result.plugin_resolved_name == 'test_plugin'
        assert result.plugin_resolved_collection == 'ansible.builtin'

def test_find_plugin_legacy_alias(plugin_loader, plugin_load_context):
    plugin_loader._plugin_path_cache['.py']['_test_plugin'] = MagicMock(path='test_path', internal=True)
    plugin_loader.aliases = {'test_plugin': '_test_plugin'}
    result = plugin_loader._find_plugin_legacy('test_plugin', plugin_load_context, check_aliases=True, suffix='.py')
    assert result.resolved
    assert result.plugin_resolved_path == 'test_path'
    assert result.plugin_resolved_name == '_test_plugin'
    assert result.plugin_resolved_collection == 'ansible.builtin'

def test_find_plugin_legacy_builtin_redirect(plugin_loader, plugin_load_context):
    with patch.object(AnsibleCollectionRef, 'is_valid_fqcr', return_value=True), \
         patch.object(plugin_loader, '_find_fq_plugin', return_value=plugin_load_context):
        result = plugin_loader._find_plugin_legacy('test_plugin', plugin_load_context, suffix='.py')
        assert result == plugin_load_context

def test_find_plugin_legacy_no_resolution(plugin_loader, plugin_load_context):
    result = plugin_loader._find_plugin_legacy('test_plugin', plugin_load_context, suffix='.py')
    assert not result.resolved
