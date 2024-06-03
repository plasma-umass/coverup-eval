# file lib/ansible/playbook/base.py:715-738
# lines []
# branches ['722->724']

import pytest
from ansible.playbook.base import FieldAttributeBase

class TestFieldAttributeBase:
    def test_extend_value_with_non_list_values(self):
        fab = FieldAttributeBase()
        
        # Test with non-list values
        value = 'a'
        new_value = 'b'
        result = fab._extend_value(value, new_value)
        
        assert result == ['a', 'b']
        
    def test_extend_value_with_non_list_new_value(self):
        fab = FieldAttributeBase()
        
        # Test with list value and non-list new_value
        value = ['a']
        new_value = 'b'
        result = fab._extend_value(value, new_value)
        
        assert result == ['a', 'b']
        
    def test_extend_value_with_non_list_value_and_new_value(self):
        fab = FieldAttributeBase()
        
        # Test with non-list value and non-list new_value
        value = 'a'
        new_value = 'b'
        result = fab._extend_value(value, new_value)
        
        assert result == ['a', 'b']
        
    def test_extend_value_with_list_values(self):
        fab = FieldAttributeBase()
        
        # Test with list values
        value = ['a']
        new_value = ['b']
        result = fab._extend_value(value, new_value)
        
        assert result == ['a', 'b']
        
    def test_extend_value_with_duplicates(self):
        fab = FieldAttributeBase()
        
        # Test with duplicate values
        value = ['a', 'b']
        new_value = ['b', 'c']
        result = fab._extend_value(value, new_value)
        
        assert result == ['a', 'b', 'c']
        
    def test_extend_value_with_sentinel(self, mocker):
        fab = FieldAttributeBase()
        
        # Mock Sentinel
        mock_sentinel = mocker.patch('ansible.playbook.base.Sentinel')
        
        # Test with Sentinel values
        value = ['a', mock_sentinel, 'b']
        new_value = [mock_sentinel, 'c']
        result = fab._extend_value(value, new_value)
        
        assert result == ['a', 'b', 'c']
        
    def test_extend_value_with_prepend(self):
        fab = FieldAttributeBase()
        
        # Test with prepend=True
        value = ['a']
        new_value = ['b']
        result = fab._extend_value(value, new_value, prepend=True)
        
        assert result == ['b', 'a']
