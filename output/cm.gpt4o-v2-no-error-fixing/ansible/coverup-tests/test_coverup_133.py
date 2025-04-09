# file: lib/ansible/playbook/base.py:715-738
# asked: {"lines": [715, 722, 723, 724, 725, 730, 731, 733, 734, 736, 738], "branches": [[722, 723], [722, 724], [724, 725], [724, 730], [733, 734], [733, 736]]}
# gained: {"lines": [715, 722, 723, 724, 725, 730, 731, 733, 734, 736, 738], "branches": [[722, 723], [722, 724], [724, 725], [724, 730], [733, 734], [733, 736]]}

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.utils.sentinel import Sentinel

class TestFieldAttributeBase:

    @pytest.fixture
    def field_attribute_base(self):
        return FieldAttributeBase()

    def test_extend_value_with_non_list_values(self, field_attribute_base):
        result = field_attribute_base._extend_value(1, 2)
        assert result == [1, 2]

    def test_extend_value_with_list_values(self, field_attribute_base):
        result = field_attribute_base._extend_value([1, 2], [3, 4])
        assert result == [1, 2, 3, 4]

    def test_extend_value_with_sentinel(self, field_attribute_base):
        result = field_attribute_base._extend_value([1, Sentinel], [Sentinel, 2])
        assert result == [1, 2]

    def test_extend_value_with_prepend(self, field_attribute_base):
        result = field_attribute_base._extend_value([1, 2], [3, 4], prepend=True)
        assert result == [3, 4, 1, 2]

    def test_extend_value_with_duplicates(self, field_attribute_base):
        result = field_attribute_base._extend_value([1, 2, 2], [2, 3, 3])
        assert result == [1, 2, 3]
