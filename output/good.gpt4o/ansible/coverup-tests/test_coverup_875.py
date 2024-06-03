# file lib/ansible/plugins/loader.py:238-239
# lines [238, 239]
# branches []

import pytest
from unittest.mock import patch

# Assuming AnsibleCollectionRef and PluginLoader are imported from ansible.plugins.loader
from ansible.plugins.loader import AnsibleCollectionRef, PluginLoader

class TestPluginLoader:
    @patch('ansible.plugins.loader.AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type')
    def test_plugin_loader_repr(self, mock_legacy_plugin_dir_to_plugin_type):
        # Arrange
        mock_legacy_plugin_dir_to_plugin_type.return_value = 'test_type'
        loader = PluginLoader(class_name='test_class', package='test_package', config='test_config', subdir='test_subdir')
        
        # Act
        repr_result = repr(loader)
        
        # Assert
        assert repr_result == 'PluginLoader(type=test_type)'
        mock_legacy_plugin_dir_to_plugin_type.assert_called_once_with('test_subdir')
