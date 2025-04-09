# file: lib/ansible/utils/collection_loader/_collection_finder.py:1001-1011
# asked: {"lines": [1003, 1004, 1005, 1006, 1007, 1009, 1010, 1011], "branches": [[1004, 1005], [1004, 1011], [1007, 1004], [1007, 1009]]}
# gained: {"lines": [1003, 1004, 1005, 1006, 1007, 1009, 1010, 1011], "branches": [[1004, 1005], [1004, 1011], [1007, 1004], [1007, 1009]]}

import pytest

from ansible.utils.collection_loader._collection_finder import _get_ancestor_redirect

def test_get_ancestor_redirect_no_redirect():
    redirected_package_map = {}
    fullname = "some.module.name"
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result is None

def test_get_ancestor_redirect_with_redirect():
    redirected_package_map = {
        "some": "redirected.some",
        "some.module": "redirected.some.module"
    }
    fullname = "some.module.name"
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result == "redirected.some.module.name"

def test_get_ancestor_redirect_partial_redirect():
    redirected_package_map = {
        "some": "redirected.some"
    }
    fullname = "some.module.name"
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result == "redirected.some.module.name"

def test_get_ancestor_redirect_no_ancestor():
    redirected_package_map = {
        "other": "redirected.other"
    }
    fullname = "some.module.name"
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result is None
