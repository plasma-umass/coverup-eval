# file: lib/ansible/playbook/play_context.py:156-165
# asked: {"lines": [156, 160, 161, 162, 163, 164, 165], "branches": [[161, 0], [161, 162], [162, 161], [162, 163], [164, 161], [164, 165]]}
# gained: {"lines": [156, 160, 161, 162, 163, 164, 165], "branches": [[161, 0], [161, 162], [162, 163], [164, 161], [164, 165]]}

import pytest
from unittest.mock import Mock, patch

# Assuming PlayContext and other necessary imports are available from ansible.playbook.play_context
from ansible.playbook.play_context import PlayContext

class TestPlayContext:
    
    @patch('ansible.playbook.play_context.C.config.get_configuration_definitions')
    @patch('ansible.playbook.play_context.get_plugin_class')
    def test_set_attributes_from_plugin(self, mock_get_plugin_class, mock_get_configuration_definitions):
        # Create a mock plugin
        mock_plugin = Mock()
        mock_plugin._load_name = 'mock_plugin'
        mock_plugin.get_option = Mock(side_effect=lambda x: f'value_for_{x}')
        
        # Mock the return value of get_plugin_class
        mock_get_plugin_class.return_value = 'mock_plugin_class'
        
        # Mock the return value of get_configuration_definitions
        mock_get_configuration_definitions.return_value = {
            'option1': {'name': 'attr1'},
            'option2': {'name': 'attr2'},
            'option3': {'name': None},  # This should be skipped
            'option4': {}  # This should also be skipped
        }
        
        # Create an instance of PlayContext
        play_context = PlayContext()
        
        # Call the method
        play_context.set_attributes_from_plugin(mock_plugin)
        
        # Assertions to verify that the attributes were set correctly
        assert getattr(play_context, 'attr1') == 'value_for_attr1'
        assert getattr(play_context, 'attr2') == 'value_for_attr2'
        assert not hasattr(play_context, 'option3')
        assert not hasattr(play_context, 'option4')
        
        # Verify that get_plugin_class and get_configuration_definitions were called correctly
        mock_get_plugin_class.assert_called_once_with(mock_plugin)
        mock_get_configuration_definitions.assert_called_once_with('mock_plugin_class', 'mock_plugin')
