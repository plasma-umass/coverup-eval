# file: flutils/objutils.py:88-112
# asked: {"lines": [88, 109, 110, 111, 112], "branches": [[109, 110], [109, 112], [110, 109], [110, 111]]}
# gained: {"lines": [88, 109, 110, 111, 112], "branches": [[109, 110], [109, 112], [110, 109], [110, 111]]}

import pytest
from flutils.objutils import has_attrs

class TestHasAttrs:
    def test_has_attrs_all_exist(self):
        obj = {'a': 1, 'b': 2}
        assert has_attrs(obj, 'keys', 'items', 'values') is True

    def test_has_attrs_some_missing(self):
        obj = {'a': 1, 'b': 2}
        assert has_attrs(obj, 'keys', 'items', 'nonexistent') is False

    def test_has_attrs_none_exist(self):
        obj = {'a': 1, 'b': 2}
        assert has_attrs(obj, 'nonexistent1', 'nonexistent2') is False

    def test_has_attrs_no_attrs(self):
        obj = {'a': 1, 'b': 2}
        assert has_attrs(obj) is True

    def test_has_attrs_empty_obj(self):
        obj = {}
        assert has_attrs(obj, 'keys', 'items', 'values') is True

    def test_has_attrs_with_non_dict_obj(self):
        class Dummy:
            def __init__(self):
                self.a = 1
                self.b = 2

        obj = Dummy()
        assert has_attrs(obj, 'a', 'b') is True
        assert has_attrs(obj, 'a', 'b', 'c') is False
