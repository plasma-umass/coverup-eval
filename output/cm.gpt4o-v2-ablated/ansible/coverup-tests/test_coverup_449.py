# file: lib/ansible/utils/collection_loader/_collection_finder.py:994-998
# asked: {"lines": [995, 996, 998], "branches": [[995, 996], [995, 998]]}
# gained: {"lines": [995, 996, 998], "branches": [[995, 996], [995, 998]]}

import pytest

from ansible.utils.collection_loader._collection_finder import _get_import_redirect

def test_get_import_redirect_no_meta_dict():
    assert _get_import_redirect(None, 'some.fullname') is None

def test_get_import_redirect_empty_meta_dict():
    assert _get_import_redirect({}, 'some.fullname') is None

def test_get_import_redirect_no_import_redirection(monkeypatch):
    def mock_nested_dict_get(d, keys):
        return None

    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._nested_dict_get', mock_nested_dict_get)
    collection_meta_dict = {'some_key': 'some_value'}
    assert _get_import_redirect(collection_meta_dict, 'some.fullname') is None

def test_get_import_redirect_with_import_redirection(monkeypatch):
    def mock_nested_dict_get(d, keys):
        if keys == ['import_redirection', 'some.fullname', 'redirect']:
            return 'redirect_value'
        return None

    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._nested_dict_get', mock_nested_dict_get)
    collection_meta_dict = {'import_redirection': {'some.fullname': {'redirect': 'redirect_value'}}}
    assert _get_import_redirect(collection_meta_dict, 'some.fullname') == 'redirect_value'
