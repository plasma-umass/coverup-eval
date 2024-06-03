# file lib/ansible/utils/collection_loader/_collection_finder.py:359-378
# lines [359, 360, 361, 362, 363, 366, 368, 369, 370, 371, 373, 374, 375, 376, 378]
# branches ['366->368', '366->373', '369->370', '369->378', '375->376', '375->378']

import os
import pytest
from unittest import mock
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

@pytest.fixture
def mock_os_path_isdir(mocker):
    return mocker.patch('os.path.isdir')

@pytest.fixture
def mock_os_path_isfile(mocker):
    return mocker.patch('os.path.isfile')

@pytest.fixture
def mock_to_native(mocker):
    return mocker.patch('ansible.utils.collection_loader._collection_finder.to_native', side_effect=lambda x: x)

@pytest.fixture
def mock_to_bytes(mocker):
    return mocker.patch('ansible.utils.collection_loader._collection_finder.to_bytes', side_effect=lambda x: x.encode())

def test_module_file_from_path_package_with_init(mock_os_path_isdir, mock_os_path_isfile, mock_to_native, mock_to_bytes):
    mock_os_path_isdir.return_value = True
    mock_os_path_isfile.side_effect = lambda x: x.endswith(b'__init__.py')

    module_path, has_code, package_path = _AnsibleCollectionPkgLoaderBase._module_file_from_path('leaf', 'path')

    assert module_path == 'path/leaf/__init__.py'
    assert has_code is True
    assert package_path == 'path/leaf'

def test_module_file_from_path_package_without_init(mock_os_path_isdir, mock_os_path_isfile, mock_to_native, mock_to_bytes):
    mock_os_path_isdir.return_value = True
    mock_os_path_isfile.side_effect = lambda x: False

    module_path, has_code, package_path = _AnsibleCollectionPkgLoaderBase._module_file_from_path('leaf', 'path')

    assert module_path == 'path/leaf/__synthetic__'
    assert has_code is False
    assert package_path == 'path/leaf'

def test_module_file_from_path_not_a_package(mock_os_path_isdir, mock_os_path_isfile, mock_to_native, mock_to_bytes):
    mock_os_path_isdir.return_value = False
    mock_os_path_isfile.side_effect = lambda x: x.endswith(b'.py')

    module_path, has_code, package_path = _AnsibleCollectionPkgLoaderBase._module_file_from_path('leaf', 'path')

    assert module_path == 'path/leaf.py'
    assert has_code is True
    assert package_path is None

def test_module_file_from_path_not_found(mock_os_path_isdir, mock_os_path_isfile, mock_to_native, mock_to_bytes):
    mock_os_path_isdir.return_value = False
    mock_os_path_isfile.side_effect = lambda x: False

    with pytest.raises(ImportError, match='leaf not found at path'):
        _AnsibleCollectionPkgLoaderBase._module_file_from_path('leaf', 'path')
