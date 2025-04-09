# file: lib/ansible/parsing/yaml/constructor.py:123-133
# asked: {"lines": [123, 124, 125, 126, 127, 128, 129, 131, 133], "branches": [[126, 127], [126, 131]]}
# gained: {"lines": [123, 124, 125, 126, 127, 128, 129, 131, 133], "branches": [[126, 127]]}

import pytest
from unittest.mock import Mock, patch
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.utils.unsafe_proxy import wrap_var
from yaml.nodes import Node

class TestAnsibleConstructor:

    @patch('ansible.parsing.yaml.constructor.AnsibleConstructor.construct_object')
    def test_construct_yaml_unsafe_with_id(self, mock_construct_object):
        constructor = AnsibleConstructor()
        node = Mock(spec=Node)
        node.id = 'object'
        
        mock_construct_object.return_value = 'constructed_value'
        
        result = constructor.construct_yaml_unsafe(node)
        
        mock_construct_object.assert_called_once_with(node)
        assert result == wrap_var('constructed_value')

    @patch('ansible.parsing.yaml.constructor.AnsibleConstructor.construct_object')
    def test_construct_yaml_unsafe_without_id(self, mock_construct_object):
        constructor = AnsibleConstructor()
        node = Mock(spec=Node)
        del node.id
        
        mock_construct_object.return_value = 'constructed_value'
        
        result = constructor.construct_yaml_unsafe(node)
        
        mock_construct_object.assert_called_once_with(node)
        assert result == wrap_var('constructed_value')

    @patch('ansible.parsing.yaml.constructor.AnsibleConstructor.construct_object')
    def test_construct_yaml_unsafe_with_invalid_id(self, mock_construct_object):
        constructor = AnsibleConstructor()
        node = Mock(spec=Node)
        node.id = 'invalid'
        
        mock_construct_object.return_value = 'constructed_value'
        
        result = constructor.construct_yaml_unsafe(node)
        
        mock_construct_object.assert_called_once_with(node)
        assert result == wrap_var('constructed_value')
