# file typesystem/unique.py:28-59
# lines [28, 34, 35, 38, 40, 41, 43, 44, 46, 47, 49, 50, 51, 52, 53, 54, 59]
# branches ['38->40', '38->41', '41->43', '41->44', '44->46', '44->47', '47->49', '47->59']

import pytest
from typesystem.unique import Uniqueness

class TestUniqueness:
    @pytest.fixture
    def uniqueness(self):
        return Uniqueness()

    def test_make_hashable_true(self, uniqueness):
        assert uniqueness.make_hashable(True) == uniqueness.TRUE

    def test_make_hashable_false(self, uniqueness):
        assert uniqueness.make_hashable(False) == uniqueness.FALSE

    def test_make_hashable_list(self, uniqueness):
        assert uniqueness.make_hashable([1, 2, 3]) == ("list", (1, 2, 3))

    def test_make_hashable_dict(self, uniqueness):
        assert uniqueness.make_hashable({'a': 1, 'b': 2}) == ("dict", (('a', 1), ('b', 2)))

    def test_make_hashable_nested(self, uniqueness):
        assert uniqueness.make_hashable([{'a': True}, False]) == ("list", (("dict", (('a', uniqueness.TRUE),)), uniqueness.FALSE))
