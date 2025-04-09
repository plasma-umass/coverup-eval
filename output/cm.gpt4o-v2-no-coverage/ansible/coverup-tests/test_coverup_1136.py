# file: lib/ansible/utils/collection_loader/_collection_finder.py:659-691
# asked: {"lines": [668, 674, 685, 686, 689, 690, 691], "branches": [[667, 668], [673, 674], [676, 0], [685, 686], [685, 689]]}
# gained: {"lines": [668, 674, 685, 686, 689, 690, 691], "branches": [[667, 668], [673, 674], [676, 0], [685, 686], [685, 689]]}

import pytest
import sys
from unittest.mock import patch, MagicMock

from ansible.utils.collection_loader._collection_finder import _AnsibleInternalRedirectLoader

# Mock functions
def mock_get_collection_metadata(name):
    if name == 'ansible.builtin':
        return {
            'import_redirection': {
                'ansible.test': {
                    'redirect': 'ansible.builtin.test'
                }
            }
        }
    return {}

def mock_nested_dict_get(d, keys):
    for key in keys:
        d = d.get(key, {})
    return d

@pytest.fixture(autouse=True)
def mock_dependencies(monkeypatch):
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._get_collection_metadata', mock_get_collection_metadata)
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._nested_dict_get', mock_nested_dict_get)

def test_init_not_interested():
    with pytest.raises(ImportError, match='not interested'):
        _AnsibleInternalRedirectLoader('not_ansible.test', [])

def test_init_not_redirected():
    with pytest.raises(ImportError, match='not redirected, go ask path_hook'):
        _AnsibleInternalRedirectLoader('ansible.not_redirected', [])

def test_init_success():
    loader = _AnsibleInternalRedirectLoader('ansible.test', [])
    assert loader._redirect == 'ansible.builtin.test'

@patch('ansible.utils.collection_loader._collection_finder.import_module')
def test_load_module_success(mock_import_module):
    mock_module = MagicMock()
    mock_import_module.return_value = mock_module

    loader = _AnsibleInternalRedirectLoader('ansible.test', [])
    mod = loader.load_module('ansible.test')

    mock_import_module.assert_called_once_with('ansible.builtin.test')
    assert sys.modules['ansible.test'] == mock_module
    assert mod == mock_module

def test_load_module_no_redirect():
    loader = _AnsibleInternalRedirectLoader('ansible.test', [])
    loader._redirect = None
    with pytest.raises(ValueError, match='no redirect found for ansible.test'):
        loader.load_module('ansible.test')
