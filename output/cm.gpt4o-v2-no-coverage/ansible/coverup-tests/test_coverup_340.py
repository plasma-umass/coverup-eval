# file: lib/ansible/plugins/loader.py:307-314
# asked: {"lines": [307, 308, 309, 310, 311, 312, 313, 314], "branches": [[310, 311], [310, 314], [311, 310], [311, 312], [312, 310], [312, 313]]}
# gained: {"lines": [307, 308, 309, 310, 311, 312, 313, 314], "branches": [[310, 311], [310, 314], [311, 310], [311, 312], [312, 310], [312, 313]]}

import os
import pytest
from unittest.mock import patch
from ansible.plugins.loader import PluginLoader

class TestPluginLoader:
    
    @patch('os.walk')
    def test_all_directories(self, mock_walk):
        # Arrange
        loader = PluginLoader(class_name='test', package='test', config=None, subdir='test')
        test_dir = '/test'
        mock_walk.return_value = [
            ('/test', ['subdir1', 'subdir2'], ['__init__.py']),
            ('/test/subdir1', [], []),
            ('/test/subdir2', [], [])
        ]
        
        # Act
        result = loader._all_directories(test_dir)
        
        # Assert
        expected = [
            '/test',
            '/test/subdir1',
            '/test/subdir2'
        ]
        assert result == expected
        mock_walk.assert_called_once_with(test_dir, followlinks=True)
