# file: lib/ansible/utils/collection_loader/_collection_finder.py:994-998
# asked: {"lines": [994, 995, 996, 998], "branches": [[995, 996], [995, 998]]}
# gained: {"lines": [994, 995, 996, 998], "branches": [[995, 996], [995, 998]]}

import pytest

def test_get_import_redirect_no_meta():
    from ansible.utils.collection_loader._collection_finder import _get_import_redirect
    assert _get_import_redirect({}, 'some.fullname') is None

def test_get_import_redirect_no_redirect():
    from ansible.utils.collection_loader._collection_finder import _get_import_redirect
    collection_meta_dict = {
        'import_redirection': {
            'some.fullname': {}
        }
    }
    assert _get_import_redirect(collection_meta_dict, 'some.fullname') is None

def test_get_import_redirect_with_redirect():
    from ansible.utils.collection_loader._collection_finder import _get_import_redirect
    collection_meta_dict = {
        'import_redirection': {
            'some.fullname': {
                'redirect': 'redirect_value'
            }
        }
    }
    assert _get_import_redirect(collection_meta_dict, 'some.fullname') == 'redirect_value'
