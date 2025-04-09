# file lib/ansible/utils/collection_loader/_collection_finder.py:254-286
# lines [254, 256, 257, 259, 261, 270, 272, 273, 274, 275, 278, 280, 281, 282, 283, 286]
# branches ['259->261', '259->270', '270->272', '270->286', '272->273', '272->280', '281->282', '281->283']

import pytest
import sys
from unittest.mock import MagicMock, patch

# Assuming the module is named _collection_finder and the class is _AnsiblePathHookFinder
from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder

@pytest.fixture
def mock_pathctx(tmp_path):
    return str(tmp_path)

@pytest.fixture
def mock_collection_finder():
    return MagicMock()

@pytest.fixture
def ansible_path_hook_finder(mock_pathctx, mock_collection_finder):
    finder = _AnsiblePathHookFinder(mock_collection_finder, mock_pathctx)
    finder._file_finder = None
    return finder

def test_find_module_ansible_collections(ansible_path_hook_finder):
    fullname = 'ansible_collections.some_collection'
    ansible_path_hook_finder.find_module(fullname)
    ansible_path_hook_finder._collection_finder.find_module.assert_called_once_with(fullname, path=[ansible_path_hook_finder._pathctx])

def test_find_module_non_ansible_collections_py3(ansible_path_hook_finder, mocker):
    fullname = 'some_other_module'
    mocker.patch('ansible.utils.collection_loader._collection_finder.PY3', True)
    mock_file_finder = MagicMock()
    ansible_path_hook_finder._file_finder = mock_file_finder
    mock_spec = MagicMock()
    mock_file_finder.find_spec.return_value = mock_spec

    loader = ansible_path_hook_finder.find_module(fullname)
    mock_file_finder.find_spec.assert_called_once_with(fullname)
    assert loader == mock_spec.loader

def test_find_module_non_ansible_collections_py3_no_spec(ansible_path_hook_finder, mocker):
    fullname = 'some_other_module'
    mocker.patch('ansible.utils.collection_loader._collection_finder.PY3', True)
    mock_file_finder = MagicMock()
    ansible_path_hook_finder._file_finder = mock_file_finder
    mock_file_finder.find_spec.return_value = None

    loader = ansible_path_hook_finder.find_module(fullname)
    mock_file_finder.find_spec.assert_called_once_with(fullname)
    assert loader is None

def test_find_module_non_ansible_collections_py3_no_file_finder(ansible_path_hook_finder, mocker):
    fullname = 'some_other_module'
    mocker.patch('ansible.utils.collection_loader._collection_finder.PY3', True)
    mocker.patch('ansible.utils.collection_loader._collection_finder._AnsiblePathHookFinder._filefinder_path_hook', side_effect=ImportError)

    loader = ansible_path_hook_finder.find_module(fullname)
    assert loader is None

def test_find_module_non_ansible_collections_py2(ansible_path_hook_finder, mocker):
    fullname = 'some_other_module'
    mocker.patch('ansible.utils.collection_loader._collection_finder.PY3', False)
    mock_pkgutil = mocker.patch('ansible.utils.collection_loader._collection_finder.pkgutil')

    loader = ansible_path_hook_finder.find_module(fullname)
    mock_pkgutil.ImpImporter.assert_called_once_with(ansible_path_hook_finder._pathctx)
    mock_pkgutil.ImpImporter().find_module.assert_called_once_with(fullname)
    assert loader == mock_pkgutil.ImpImporter().find_module()
