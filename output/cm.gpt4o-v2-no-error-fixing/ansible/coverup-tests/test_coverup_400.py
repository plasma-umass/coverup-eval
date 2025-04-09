# file: lib/ansible/utils/collection_loader/_collection_finder.py:994-998
# asked: {"lines": [994, 995, 996, 998], "branches": [[995, 996], [995, 998]]}
# gained: {"lines": [994, 995, 996, 998], "branches": [[995, 996], [995, 998]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _get_import_redirect

def test_get_import_redirect_no_meta():
    result = _get_import_redirect({}, 'some.fullname')
    assert result is None

def test_get_import_redirect_no_redirect():
    collection_meta_dict = {
        'import_redirection': {
            'some.othername': {
                'redirect': 'some.redirect'
            }
        }
    }
    result = _get_import_redirect(collection_meta_dict, 'some.fullname')
    assert result is None

def test_get_import_redirect_with_redirect():
    collection_meta_dict = {
        'import_redirection': {
            'some.fullname': {
                'redirect': 'some.redirect'
            }
        }
    }
    result = _get_import_redirect(collection_meta_dict, 'some.fullname')
    assert result == 'some.redirect'
