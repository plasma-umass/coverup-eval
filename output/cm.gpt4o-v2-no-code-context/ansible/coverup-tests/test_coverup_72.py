# file: lib/ansible/utils/collection_loader/_collection_finder.py:659-691
# asked: {"lines": [659, 660, 661, 663, 664, 665, 667, 668, 670, 672, 673, 674, 676, 677, 679, 685, 686, 689, 690, 691], "branches": [[667, 668], [667, 670], [673, 674], [673, 676], [676, 0], [676, 677], [685, 686], [685, 689]]}
# gained: {"lines": [659, 660, 661, 663, 664, 665, 667, 668, 670, 672, 673, 674, 676, 677, 679, 685, 686, 689, 690, 691], "branches": [[667, 668], [667, 670], [673, 674], [673, 676], [676, 0], [676, 677], [685, 686], [685, 689]]}

import pytest
import sys
from unittest.mock import patch, MagicMock
from importlib import import_module
from ansible.utils.collection_loader._collection_finder import _AnsibleInternalRedirectLoader

# Mocking the _get_collection_metadata and _nested_dict_get functions
def mock_get_collection_metadata(name):
    if name == 'ansible.builtin':
        return {
            'import_redirection': {
                'ansible.some_module': {
                    'redirect': 'ansible.builtin.some_module'
                }
            }
        }
    return {}

def mock_nested_dict_get(d, keys):
    for key in keys:
        d = d.get(key, {})
    return d

@pytest.fixture
def mock_imports(monkeypatch):
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._get_collection_metadata', mock_get_collection_metadata)
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._nested_dict_get', mock_nested_dict_get)

def test_ansible_internal_redirect_loader_init_success(mock_imports):
    loader = _AnsibleInternalRedirectLoader('ansible.some_module', [])
    assert loader._redirect == 'ansible.builtin.some_module'

def test_ansible_internal_redirect_loader_init_import_error(mock_imports):
    with pytest.raises(ImportError, match='not interested'):
        _AnsibleInternalRedirectLoader('not_ansible.some_module', [])

def test_ansible_internal_redirect_loader_init_no_redirect(mock_imports):
    with pytest.raises(ImportError, match='not redirected, go ask path_hook'):
        _AnsibleInternalRedirectLoader('ansible.non_existent_module', [])

@patch('ansible.utils.collection_loader._collection_finder.import_module')
def test_ansible_internal_redirect_loader_load_module(mock_import_module, mock_imports):
    mock_import_module.return_value = MagicMock()
    loader = _AnsibleInternalRedirectLoader('ansible.some_module', [])
    mod = loader.load_module('ansible.some_module')
    mock_import_module.assert_called_once_with('ansible.builtin.some_module')
    assert sys.modules['ansible.some_module'] == mod

def test_ansible_internal_redirect_loader_load_module_no_redirect(mock_imports):
    loader = _AnsibleInternalRedirectLoader('ansible.some_module', [])
    loader._redirect = None
    with pytest.raises(ValueError, match='no redirect found for ansible.some_module'):
        loader.load_module('ansible.some_module')
