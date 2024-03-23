# file lib/ansible/utils/collection_loader/_collection_finder.py:1001-1011
# lines [1011]
# branches ['1004->1011']

import pytest
from ansible.utils.collection_loader._collection_finder import _get_ancestor_redirect

def test_get_ancestor_redirect_with_no_redirect(mocker):
    redirected_package_map = {
        'some.ancestor.package': 'redirected.package',
        'some.ancestor': 'redirected.ancestor'
    }
    fullname = 'some.ancestor.package.module'

    # Mock the redirected_package_map to not contain the exact fullname
    mocker.patch.dict(redirected_package_map, {}, clear=True)

    # Call the function with the mocked map
    result = _get_ancestor_redirect(redirected_package_map, fullname)

    # Assert that the result is None since there is no exact match in the map
    assert result is None

@pytest.fixture
def cleanup_redirects():
    # Setup fixture to provide a clean redirected_package_map
    redirected_package_map = {}
    yield redirected_package_map
    # No cleanup needed since we're not modifying any global state

def test_get_ancestor_redirect_with_redirect(cleanup_redirects):
    redirected_package_map = cleanup_redirects
    redirected_package_map.update({
        'some.ancestor': 'redirected.ancestor'
    })
    fullname = 'some.ancestor.package.module'

    # Call the function with the redirected_package_map containing a redirect
    result = _get_ancestor_redirect(redirected_package_map, fullname)

    # Assert that the result is the redirected fullname
    expected_redirect = 'redirected.ancestor.package.module'
    assert result == expected_redirect
