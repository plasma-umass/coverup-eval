# file lib/ansible/playbook/base.py:715-738
# lines [715, 722, 723, 724, 725, 730, 731, 733, 734, 736, 738]
# branches ['722->723', '722->724', '724->725', '724->730', '733->734', '733->736']

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.utils.sentinel import Sentinel
import itertools

class TestFieldAttributeBase:

    @pytest.fixture
    def field_attribute_base(self):
        return FieldAttributeBase()

    def test_extend_value(self, field_attribute_base):
        # Test with non-list values
        result = field_attribute_base._extend_value('a', 'b')
        assert result == ['a', 'b'], "Non-list values should be converted to lists and combined"

        # Test with list values
        result = field_attribute_base._extend_value(['a'], ['b'])
        assert result == ['a', 'b'], "List values should be combined"

        # Test with duplicate values
        result = field_attribute_base._extend_value(['a', 'b'], ['b', 'c'])
        assert result == ['a', 'b', 'c'], "Duplicate values should be removed"

        # Test with Sentinel values
        result = field_attribute_base._extend_value([Sentinel, 'a'], [Sentinel, 'b'])
        assert result == ['a', 'b'], "Sentinel values should be stripped"

        # Test with None values
        result = field_attribute_base._extend_value([None, 'a'], [None, 'b'])
        assert result == ['a', 'b'], "None values should be removed"

        # Test with prepend=True
        result = field_attribute_base._extend_value(['a'], ['b'], prepend=True)
        assert result == ['b', 'a'], "Prepend should add new_value before value"

        # Test with prepend=False
        result = field_attribute_base._extend_value(['a'], ['b'], prepend=False)
        assert result == ['a', 'b'], "Prepend should add new_value after value"

