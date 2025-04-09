# file: lib/ansible/utils/collection_loader/_collection_finder.py:994-998
# asked: {"lines": [994, 995, 996, 998], "branches": [[995, 996], [995, 998]]}
# gained: {"lines": [994, 995, 996, 998], "branches": [[995, 996], [995, 998]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _get_import_redirect

def test_get_import_redirect_empty_dict():
    collection_meta_dict = {}
    fullname = 'some_module'
    result = _get_import_redirect(collection_meta_dict, fullname)
    assert result is None

def test_get_import_redirect_no_redirection():
    collection_meta_dict = {
        'import_redirection': {
            'some_module': {
                'no_redirect': 'value'
            }
        }
    }
    fullname = 'some_module'
    result = _get_import_redirect(collection_meta_dict, fullname)
    assert result is None

def test_get_import_redirect_with_redirection():
    collection_meta_dict = {
        'import_redirection': {
            'some_module': {
                'redirect': 'new_module'
            }
        }
    }
    fullname = 'some_module'
    result = _get_import_redirect(collection_meta_dict, fullname)
    assert result == 'new_module'
