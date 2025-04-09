# file: flutils/objutils.py:36-58
# asked: {"lines": [36, 55, 56, 57, 58], "branches": [[55, 56], [55, 58], [56, 55], [56, 57]]}
# gained: {"lines": [36, 55, 56, 57, 58], "branches": [[55, 56], [55, 58], [56, 55], [56, 57]]}

import pytest
from flutils.objutils import has_any_attrs

class TestHasAnyAttrs:
    def test_has_any_attrs_true(self):
        obj = {'a': 1, 'b': 2}
        assert has_any_attrs(obj, 'keys', 'values') is True

    def test_has_any_attrs_false(self):
        obj = {'a': 1, 'b': 2}
        assert has_any_attrs(obj, 'nonexistent', 'another_nonexistent') is False

    def test_has_any_attrs_mixed(self):
        obj = {'a': 1, 'b': 2}
        assert has_any_attrs(obj, 'nonexistent', 'keys') is True

    def test_has_any_attrs_no_attrs(self):
        obj = {'a': 1, 'b': 2}
        assert has_any_attrs(obj) is False

    def test_has_any_attrs_empty_obj(self):
        obj = {}
        assert has_any_attrs(obj, 'nonexistent', 'another_nonexistent') is False
