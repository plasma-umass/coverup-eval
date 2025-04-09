# file: lib/ansible/utils/collection_loader/_collection_finder.py:254-286
# asked: {"lines": [261, 275, 278, 282, 286], "branches": [[259, 261], [270, 286], [281, 282]]}
# gained: {"lines": [261, 275, 278], "branches": [[259, 261]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.six import PY3
from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder

@pytest.fixture
def collection_finder():
    return MagicMock()

@pytest.fixture
def pathctx():
    return "some_path"

@pytest.fixture
def finder(collection_finder, pathctx):
    return _AnsiblePathHookFinder(collection_finder, pathctx)

def test_find_module_ansible_collections(finder, collection_finder):
    fullname = "ansible_collections.some_module"
    result = finder.find_module(fullname)
    collection_finder.find_module.assert_called_once_with(fullname, path=[finder._pathctx])
    assert result == collection_finder.find_module.return_value

def test_find_module_py3_no_file_finder(finder):
    if not PY3:
        pytest.skip("This test is for Python 3 only")
    
    fullname = "some_module"
    with patch.object(_AnsiblePathHookFinder, '_filefinder_path_hook', return_value=MagicMock()) as mock_filefinder_path_hook:
        result = finder.find_module(fullname)
        mock_filefinder_path_hook.assert_called_once_with(finder._pathctx)
        assert result == mock_filefinder_path_hook.return_value.find_spec.return_value.loader

def test_find_module_py3_with_file_finder(finder):
    if not PY3:
        pytest.skip("This test is for Python 3 only")
    
    fullname = "some_module"
    finder._file_finder = MagicMock()
    result = finder.find_module(fullname)
    finder._file_finder.find_spec.assert_called_once_with(fullname)
    assert result == finder._file_finder.find_spec.return_value.loader

def test_find_module_py3_import_error(finder):
    if not PY3:
        pytest.skip("This test is for Python 3 only")
    
    fullname = "some_module"
    with patch.object(_AnsiblePathHookFinder, '_filefinder_path_hook', side_effect=ImportError):
        result = finder.find_module(fullname)
        assert result is None

def test_find_module_py2(finder, monkeypatch):
    if PY3:
        pytest.skip("This test is for Python 2 only")
    
    fullname = "some_module"
    mock_imp_importer = MagicMock()
    monkeypatch.setattr(pkgutil, 'ImpImporter', mock_imp_importer)
    result = finder.find_module(fullname)
    mock_imp_importer.assert_called_once_with(finder._pathctx)
    mock_imp_importer.return_value.find_module.assert_called_once_with(fullname)
    assert result == mock_imp_importer.return_value.find_module.return_value
