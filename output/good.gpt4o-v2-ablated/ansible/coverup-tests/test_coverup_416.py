# file: lib/ansible/playbook/base.py:715-738
# asked: {"lines": [722, 723, 724, 725, 730, 731, 733, 734, 736, 738], "branches": [[722, 723], [722, 724], [724, 725], [724, 730], [733, 734], [733, 736]]}
# gained: {"lines": [722, 723, 724, 725, 730, 731, 733, 734, 736, 738], "branches": [[722, 723], [722, 724], [724, 725], [724, 730], [733, 734], [733, 736]]}

import pytest
from ansible.playbook.base import FieldAttributeBase, Sentinel
import itertools

class TestFieldAttributeBase:
    @pytest.fixture
    def field_attribute_base(self):
        return FieldAttributeBase()

    def test_extend_value_with_non_list_values(self, field_attribute_base):
        result = field_attribute_base._extend_value('a', 'b')
        assert result == ['a', 'b']

    def test_extend_value_with_list_values(self, field_attribute_base):
        result = field_attribute_base._extend_value(['a'], ['b'])
        assert result == ['a', 'b']

    def test_extend_value_with_duplicates(self, field_attribute_base):
        result = field_attribute_base._extend_value(['a', 'a'], ['b', 'b'])
        assert result == ['a', 'b']

    def test_extend_value_with_sentinel(self, field_attribute_base):
        result = field_attribute_base._extend_value(['a', Sentinel], ['b', Sentinel])
        assert result == ['a', 'b']

    def test_extend_value_with_prepend(self, field_attribute_base):
        result = field_attribute_base._extend_value(['a'], ['b'], prepend=True)
        assert result == ['b', 'a']

    def test_extend_value_with_none(self, field_attribute_base):
        result = field_attribute_base._extend_value(['a', None], ['b', None])
        assert result == ['a', 'b']
