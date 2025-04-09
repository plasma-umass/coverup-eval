# file lib/ansible/utils/collection_loader/_collection_finder.py:994-998
# lines [994, 995, 996, 998]
# branches ['995->996', '995->998']

import pytest
from ansible.utils.collection_loader._collection_finder import _get_import_redirect

def test_get_import_redirect_none():
    assert _get_import_redirect(None, 'test.fullname') is None

def test_get_import_redirect_empty_dict():
    assert _get_import_redirect({}, 'test.fullname') is None

def test_get_import_redirect_with_data(mocker):
    collection_meta_dict = {
        'import_redirection': {
            'test.fullname': {
                'redirect': 'test.redirected_fullname'
            }
        }
    }
    assert _get_import_redirect(collection_meta_dict, 'test.fullname') == 'test.redirected_fullname'

def test_get_import_redirect_missing_fullname(mocker):
    collection_meta_dict = {
        'import_redirection': {
            'other.fullname': {
                'redirect': 'other.redirected_fullname'
            }
        }
    }
    assert _get_import_redirect(collection_meta_dict, 'test.fullname') is None
