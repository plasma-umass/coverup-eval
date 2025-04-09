# file lib/ansible/utils/collection_loader/_collection_finder.py:187-225
# lines [187, 190, 191, 192, 193, 195, 197, 200, 201, 202, 205, 207, 208, 211, 212, 214, 215, 216, 217, 218, 219, 220, 222, 223, 225]
# branches ['195->197', '195->200', '200->201', '200->207', '201->202', '201->205', '207->208', '207->211', '212->214', '212->215', '215->216', '215->217', '217->218', '217->219', '219->220', '219->222']

import pytest
from unittest import mock

# Assuming the classes _AnsibleInternalRedirectLoader, _AnsibleCollectionRootPkgLoader,
# _AnsibleCollectionNSPkgLoader, _AnsibleCollectionPkgLoader, and _AnsibleCollectionLoader
# are defined somewhere in the module ansible.utils.collection_loader._collection_finder

from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder

@pytest.fixture
def collection_finder():
    finder = _AnsibleCollectionFinder()
    # Mocking the default collection paths using a property mock
    with mock.patch.object(_AnsibleCollectionFinder, '_n_collection_paths', new_callable=mock.PropertyMock) as mock_paths:
        mock_paths.return_value = ['default_path']
        yield finder

def test_find_module_toplevel_pkg_not_ansible(collection_finder):
    assert collection_finder.find_module('not_ansible') is None

def test_find_module_toplevel_pkg_ansible_with_path(collection_finder):
    with pytest.raises(ValueError, match='path should not be specified for top-level packages'):
        collection_finder.find_module('ansible', path=['some_path'])

def test_find_module_subpackage_without_path(collection_finder):
    with pytest.raises(ValueError, match='path must be specified for subpackages'):
        collection_finder.find_module('ansible.subpackage')

def test_find_module_ansible_internal_redirect_loader(collection_finder):
    with mock.patch('ansible.utils.collection_loader._collection_finder._AnsibleInternalRedirectLoader') as mock_loader:
        mock_loader.return_value = 'mock_loader_instance'
        result = collection_finder.find_module('ansible.some_module', path=['some_path'])
        assert result == 'mock_loader_instance'
        mock_loader.assert_called_once_with(fullname='ansible.some_module', path_list=['some_path'])

def test_find_module_ansible_collection_root_pkg_loader(collection_finder):
    with mock.patch('ansible.utils.collection_loader._collection_finder._AnsibleCollectionRootPkgLoader') as mock_loader:
        mock_loader.return_value = 'mock_loader_instance'
        result = collection_finder.find_module('ansible_collections')
        assert result == 'mock_loader_instance'
        mock_loader.assert_called_once_with(fullname='ansible_collections', path_list=['default_path'])

def test_find_module_ansible_collection_ns_pkg_loader(collection_finder):
    with mock.patch('ansible.utils.collection_loader._collection_finder._AnsibleCollectionNSPkgLoader') as mock_loader:
        mock_loader.return_value = 'mock_loader_instance'
        result = collection_finder.find_module('ansible_collections.somens', path=['some_path'])
        assert result == 'mock_loader_instance'
        mock_loader.assert_called_once_with(fullname='ansible_collections.somens', path_list=['some_path'])

def test_find_module_ansible_collection_pkg_loader(collection_finder):
    with mock.patch('ansible.utils.collection_loader._collection_finder._AnsibleCollectionPkgLoader') as mock_loader:
        mock_loader.return_value = 'mock_loader_instance'
        result = collection_finder.find_module('ansible_collections.somens.somecoll', path=['some_path'])
        assert result == 'mock_loader_instance'
        mock_loader.assert_called_once_with(fullname='ansible_collections.somens.somecoll', path_list=['some_path'])

def test_find_module_ansible_collection_loader(collection_finder):
    with mock.patch('ansible.utils.collection_loader._collection_finder._AnsibleCollectionLoader') as mock_loader:
        mock_loader.return_value = 'mock_loader_instance'
        result = collection_finder.find_module('ansible_collections.somens.somecoll.some_module', path=['some_path'])
        assert result == 'mock_loader_instance'
        mock_loader.assert_called_once_with(fullname='ansible_collections.somens.somecoll.some_module', path_list=['some_path'])

def test_find_module_import_error(collection_finder):
    with mock.patch('ansible.utils.collection_loader._collection_finder._AnsibleCollectionLoader', side_effect=ImportError):
        result = collection_finder.find_module('ansible_collections.somens.somecoll.some_module', path=['some_path'])
        assert result is None
