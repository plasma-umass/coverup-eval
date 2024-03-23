# file lib/ansible/utils/collection_loader/_collection_finder.py:1001-1011
# lines [1003, 1004, 1005, 1006, 1007, 1009, 1010, 1011]
# branches ['1004->1005', '1004->1011', '1007->1004', '1007->1009']

import pytest
from ansible.utils.collection_loader import _collection_finder

def test_get_ancestor_redirect():
    redirected_package_map = {
        'ancestor': 'redirected_ancestor'
    }
    fullname = 'ancestor.module.submodule'

    # Call the _get_ancestor_redirect function with the mocked map
    redirect = _collection_finder._get_ancestor_redirect(redirected_package_map, fullname)

    # Assert that the redirect is correct
    assert redirect == 'redirected_ancestor.module.submodule'
