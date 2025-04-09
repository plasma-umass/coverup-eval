# file: lib/ansible/utils/collection_loader/_collection_finder.py:1001-1011
# asked: {"lines": [1001, 1003, 1004, 1005, 1006, 1007, 1009, 1010, 1011], "branches": [[1004, 1005], [1004, 1011], [1007, 1004], [1007, 1009]]}
# gained: {"lines": [1001, 1003, 1004, 1005, 1006, 1007, 1009, 1010, 1011], "branches": [[1004, 1005], [1004, 1011], [1007, 1004], [1007, 1009]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _get_ancestor_redirect

def test_get_ancestor_redirect_no_redirect():
    redirected_package_map = {}
    fullname = "ansible.module_utils.basic"
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result is None

def test_get_ancestor_redirect_with_redirect():
    redirected_package_map = {
        "ansible": "redirected_ansible",
        "ansible.module_utils": "redirected_module_utils"
    }
    fullname = "ansible.module_utils.basic"
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result == "redirected_module_utils.basic"

def test_get_ancestor_redirect_partial_redirect():
    redirected_package_map = {
        "ansible": "redirected_ansible"
    }
    fullname = "ansible.module_utils.basic"
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result == "redirected_ansible.module_utils.basic"

def test_get_ancestor_redirect_no_match():
    redirected_package_map = {
        "other": "redirected_other"
    }
    fullname = "ansible.module_utils.basic"
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result is None
