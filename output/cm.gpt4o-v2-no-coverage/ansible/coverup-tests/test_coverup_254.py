# file: lib/ansible/playbook/base.py:753-772
# asked: {"lines": [753, 757, 758, 759, 760, 761, 762, 763, 765, 771, 772], "branches": [[757, 758], [757, 771], [758, 757], [758, 759], [760, 761], [760, 765]]}
# gained: {"lines": [753, 757, 758, 759, 760, 761, 762, 763, 765, 771, 772], "branches": [[757, 758], [757, 771], [758, 759], [760, 761], [760, 765]]}

import pytest
from unittest.mock import Mock

from ansible.playbook.base import FieldAttributeBase
from ansible.playbook.attribute import Attribute

class TestFieldAttributeBase:
    
    @pytest.fixture
    def mock_valid_attrs(self, monkeypatch):
        mock_attrs = {
            'attr1': Mock(isa='class', class_type=Mock(return_value=Mock(deserialize=Mock()))),
            'attr2': Mock(isa='other')
        }
        monkeypatch.setattr(FieldAttributeBase, '_valid_attrs', mock_attrs)
        return mock_attrs

    def test_from_attrs_with_class_type(self, mock_valid_attrs):
        instance = FieldAttributeBase()
        attrs = {
            'attr1': {'key': 'value'},
            'attr2': 'some_value'
        }
        
        instance.from_attrs(attrs)
        
        assert instance.attr1.deserialize.called
        assert instance.attr2 == 'some_value'
        assert instance._finalized
        assert instance._squashed

    def test_from_attrs_without_class_type(self, mock_valid_attrs):
        instance = FieldAttributeBase()
        attrs = {
            'attr2': 'some_value'
        }
        
        instance.from_attrs(attrs)
        
        assert instance.attr2 == 'some_value'
        assert instance._finalized
        assert instance._squashed
