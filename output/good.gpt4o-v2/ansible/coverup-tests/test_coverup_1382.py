# file: lib/ansible/utils/collection_loader/_collection_finder.py:254-286
# asked: {"lines": [261, 275, 278, 282, 286], "branches": [[259, 261], [270, 286], [281, 282]]}
# gained: {"lines": [261, 275, 278, 282, 286], "branches": [[259, 261], [270, 286], [281, 282]]}

import pytest
from unittest.mock import MagicMock, patch, create_autospec
from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder

@pytest.fixture
def finder():
    collection_finder = MagicMock()
    pathctx = 'some_path'
    finder = _AnsiblePathHookFinder(collection_finder, pathctx)
    return finder

def test_find_module_collection(finder):
    fullname = 'ansible_collections.some_module'
    finder._collection_finder.find_module.return_value = 'collection_module'
    
    result = finder.find_module(fullname)
    
    assert result == 'collection_module'
    finder._collection_finder.find_module.assert_called_once_with(fullname, path=[finder._pathctx])

@patch('ansible.utils.collection_loader._collection_finder.PY3', True)
def test_find_module_py3_no_file_finder(finder):
    fullname = 'some_module'
    with patch.object(_AnsiblePathHookFinder, '_filefinder_path_hook', side_effect=ImportError):
        result = finder.find_module(fullname)
        assert result is None

@patch('ansible.utils.collection_loader._collection_finder.PY3', True)
def test_find_module_py3_with_file_finder(finder):
    fullname = 'some_module'
    mock_spec = MagicMock()
    finder._file_finder = MagicMock()
    finder._file_finder.find_spec.return_value = mock_spec
    
    result = finder.find_module(fullname)
    
    assert result == mock_spec.loader
    finder._file_finder.find_spec.assert_called_once_with(fullname)

@patch('ansible.utils.collection_loader._collection_finder.PY3', True)
def test_find_module_py3_spec_none(finder):
    fullname = 'some_module'
    finder._file_finder = MagicMock()
    finder._file_finder.find_spec.return_value = None
    
    result = finder.find_module(fullname)
    
    assert result is None
    finder._file_finder.find_spec.assert_called_once_with(fullname)

@patch('ansible.utils.collection_loader._collection_finder.PY3', False)
def test_find_module_py2(finder):
    fullname = 'some_module'
    with patch('pkgutil.ImpImporter') as mock_importer:
        mock_instance = mock_importer.return_value
        mock_instance.find_module.return_value = 'py2_module'
        
        result = finder.find_module(fullname)
        
        assert result == 'py2_module'
        mock_importer.assert_called_once_with(finder._pathctx)
        mock_instance.find_module.assert_called_once_with(fullname)
