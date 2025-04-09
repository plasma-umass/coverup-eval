# file: lib/ansible/playbook/base.py:715-738
# asked: {"lines": [715, 722, 723, 724, 725, 730, 731, 733, 734, 736, 738], "branches": [[722, 723], [722, 724], [724, 725], [724, 730], [733, 734], [733, 736]]}
# gained: {"lines": [715, 722, 723, 724, 725, 730, 731, 733, 734, 736, 738], "branches": [[722, 723], [722, 724], [724, 725], [724, 730], [733, 734], [733, 736]]}

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.utils.sentinel import Sentinel

class TestFieldAttributeBase:
    
    @pytest.mark.parametrize("value, new_value, prepend, expected", [
        (1, 2, False, [1, 2]),
        (1, 2, True, [2, 1]),
        ([1, 2], 3, False, [1, 2, 3]),
        (1, [2, 3], False, [1, 2, 3]),
        ([1, 2], [2, 3], False, [1, 2, 3]),
        ([1, Sentinel, 2], [2, Sentinel, 3], False, [1, 2, 3]),
        ([1, None, 2], [2, None, 3], False, [1, 2, 3]),
    ])
    def test_extend_value(self, value, new_value, prepend, expected):
        fab = FieldAttributeBase()
        result = fab._extend_value(value, new_value, prepend)
        assert result == expected
