# file: lib/ansible/playbook/base.py:129-192
# asked: {"lines": [], "branches": [[141, 148], [175, 174]]}
# gained: {"lines": [], "branches": [[141, 148]]}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.base import BaseMeta
from ansible.playbook.attribute import Attribute
from ansible.utils.sentinel import Sentinel

class TestBaseMeta:
    
    def test_create_attrs_with_private_attribute(self):
        src_dict = {
            '_private_attr': Attribute(default='default_value', alias=None, inherit=True)
        }
        dst_dict = {
            '_attributes': {},
            '_attr_defaults': {},
            '_valid_attrs': {},
            '_alias_attrs': {}
        }
        BaseMeta.__new__(BaseMeta, 'TestClass', (), src_dict)
        
        assert 'private_attr' in src_dict
        assert isinstance(src_dict['private_attr'], property)
        assert '_private_attr' not in src_dict['_valid_attrs']
        assert 'private_attr' in src_dict['_valid_attrs']
        assert src_dict['_valid_attrs']['private_attr'].default == 'default_value'
        assert src_dict['_attributes']['private_attr'] == Sentinel
        assert src_dict['_attr_defaults']['private_attr'] == 'default_value'

    def test_process_parents_with_dict(self):
        class Parent:
            parent_attr = Attribute(default='parent_default', alias=None, inherit=True)
        
        dst_dict = {
            '_attributes': {},
            '_attr_defaults': {},
            '_valid_attrs': {},
            '_alias_attrs': {}
        }
        BaseMeta.__new__(BaseMeta, 'TestClass', (Parent,), dst_dict)
        
        assert 'parent_attr' in dst_dict
        assert isinstance(dst_dict['parent_attr'], property)
        assert 'parent_attr' in dst_dict['_valid_attrs']
        assert dst_dict['_valid_attrs']['parent_attr'].default == 'parent_default'
        assert dst_dict['_attributes']['parent_attr'] == Sentinel
        assert dst_dict['_attr_defaults']['parent_attr'] == 'parent_default'
