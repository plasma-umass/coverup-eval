# file lib/ansible/utils/collection_loader/_collection_finder.py:659-691
# lines [668, 674, 685, 686, 689, 690, 691]
# branches ['667->668', '673->674', '676->exit', '685->686', '685->689']

import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import _AnsibleInternalRedirectLoader
import sys

def test_ansible_internal_redirect_loader_import_error():
    with pytest.raises(ImportError, match='not interested'):
        _AnsibleInternalRedirectLoader('not_ansible.module', [])

def test_ansible_internal_redirect_loader_no_redirect(mocker):
    mock_get_collection_metadata = mocker.patch('ansible.utils.collection_loader._collection_finder._get_collection_metadata')
    mock_nested_dict_get = mocker.patch('ansible.utils.collection_loader._collection_finder._nested_dict_get')
    
    mock_get_collection_metadata.return_value = {}
    mock_nested_dict_get.return_value = None
    
    with pytest.raises(ImportError, match='not redirected, go ask path_hook'):
        _AnsibleInternalRedirectLoader('ansible.module', [])

def test_ansible_internal_redirect_loader_load_module_no_redirect(mocker):
    mock_get_collection_metadata = mocker.patch('ansible.utils.collection_loader._collection_finder._get_collection_metadata')
    mock_nested_dict_get = mocker.patch('ansible.utils.collection_loader._collection_finder._nested_dict_get')
    
    mock_get_collection_metadata.return_value = {}
    mock_nested_dict_get.return_value = None
    
    with patch.object(_AnsibleInternalRedirectLoader, '__init__', lambda self, fullname, path_list: None):
        loader = _AnsibleInternalRedirectLoader('ansible.module', [])
        loader._redirect = None
    
        with pytest.raises(ValueError, match='no redirect found for ansible.module'):
            loader.load_module('ansible.module')

def test_ansible_internal_redirect_loader_load_module_success(mocker):
    mock_get_collection_metadata = mocker.patch('ansible.utils.collection_loader._collection_finder._get_collection_metadata')
    mock_nested_dict_get = mocker.patch('ansible.utils.collection_loader._collection_finder._nested_dict_get')
    mock_import_module = mocker.patch('ansible.utils.collection_loader._collection_finder.import_module')
    
    mock_get_collection_metadata.return_value = {}
    mock_nested_dict_get.return_value = {'redirect': 'redirected.module'}
    mock_import_module.return_value = MagicMock()
    
    with patch.object(_AnsibleInternalRedirectLoader, '__init__', lambda self, fullname, path_list: None):
        loader = _AnsibleInternalRedirectLoader('ansible.module', [])
        loader._redirect = 'redirected.module'
        mod = loader.load_module('ansible.module')
    
        assert mod == mock_import_module.return_value
        assert sys.modules['ansible.module'] == mock_import_module.return_value
