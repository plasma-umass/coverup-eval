# file: flutils/objutils.py:36-58
# asked: {"lines": [55, 56, 57, 58], "branches": [[55, 56], [55, 58], [56, 55], [56, 57]]}
# gained: {"lines": [55, 56, 57, 58], "branches": [[55, 56], [55, 58], [56, 55], [56, 57]]}

import pytest
from flutils.objutils import has_any_attrs

def test_has_any_attrs_with_existing_attrs():
    obj = {'key': 'value'}
    assert has_any_attrs(obj, 'keys', 'values') is True

def test_has_any_attrs_with_non_existing_attrs():
    obj = {'key': 'value'}
    assert has_any_attrs(obj, 'nonexistent', 'anothernonexistent') is False

def test_has_any_attrs_with_mixed_attrs():
    obj = {'key': 'value'}
    assert has_any_attrs(obj, 'keys', 'nonexistent') is True

def test_has_any_attrs_with_no_attrs():
    obj = {'key': 'value'}
    assert has_any_attrs(obj) is False
