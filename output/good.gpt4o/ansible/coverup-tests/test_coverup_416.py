# file lib/ansible/parsing/yaml/constructor.py:123-133
# lines [123, 124, 125, 126, 127, 128, 129, 131, 133]
# branches ['126->127', '126->131']

import pytest
from unittest.mock import Mock, patch
from ansible.parsing.yaml.constructor import AnsibleConstructor
from yaml.nodes import Node

class TestAnsibleConstructor:
    @patch('ansible.parsing.yaml.constructor.wrap_var')
    def test_construct_yaml_unsafe(self, mock_wrap_var):
        mock_node = Mock(spec=Node)
        mock_node.id = 'test'
        
        constructor = AnsibleConstructor()
        
        # Mock the method that should be called based on node.id
        mock_construct_method = Mock(return_value='constructed_value')
        setattr(constructor, 'construct_test', mock_construct_method)
        
        # Call the method under test
        result = constructor.construct_yaml_unsafe(mock_node)
        
        # Assertions
        mock_construct_method.assert_called_once_with(mock_node)
        mock_wrap_var.assert_called_once_with('constructed_value')
        assert result == mock_wrap_var.return_value

    @patch('ansible.parsing.yaml.constructor.wrap_var')
    def test_construct_yaml_unsafe_no_id(self, mock_wrap_var):
        mock_node = Mock(spec=Node)
        del mock_node.id  # Ensure the node has no 'id' attribute
        
        constructor = AnsibleConstructor()
        
        # Mock the default construct_object method
        mock_construct_object = Mock(return_value='default_constructed_value')
        constructor.construct_object = mock_construct_object
        
        # Call the method under test
        result = constructor.construct_yaml_unsafe(mock_node)
        
        # Assertions
        mock_construct_object.assert_called_once_with(mock_node)
        mock_wrap_var.assert_called_once_with('default_constructed_value')
        assert result == mock_wrap_var.return_value
