# file: lib/ansible/utils/collection_loader/_collection_finder.py:359-378
# asked: {"lines": [359, 360, 361, 362, 363, 366, 368, 369, 370, 371, 373, 374, 375, 376, 378], "branches": [[366, 368], [366, 373], [369, 370], [369, 378], [375, 376], [375, 378]]}
# gained: {"lines": [359, 360, 361, 362, 363, 366, 368, 369, 370, 371, 373, 374, 375, 376, 378], "branches": [[366, 368], [366, 373], [369, 370], [369, 378], [375, 376], [375, 378]]}

import os
import pytest
from ansible.module_utils.common.text.converters import to_native, to_bytes
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

def test_module_file_from_path_package_with_init(monkeypatch):
    test_leaf_name = 'test_package'
    test_path = '/test/path'
    test_package_path = os.path.join(to_native(test_path), to_native(test_leaf_name))
    test_module_path = os.path.join(test_package_path, '__init__.py')

    def mock_isdir(path):
        return path == to_bytes(test_package_path)

    def mock_isfile(path):
        return path == to_bytes(test_module_path)

    monkeypatch.setattr(os.path, 'isdir', mock_isdir)
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)

    module_path, has_code, package_path = _AnsibleCollectionPkgLoaderBase._module_file_from_path(test_leaf_name, test_path)

    assert module_path == test_module_path
    assert has_code is True
    assert package_path == test_package_path

def test_module_file_from_path_package_without_init(monkeypatch):
    test_leaf_name = 'test_package'
    test_path = '/test/path'
    test_package_path = os.path.join(to_native(test_path), to_native(test_leaf_name))
    test_module_path = os.path.join(test_package_path, '__synthetic__')

    def mock_isdir(path):
        return path == to_bytes(test_package_path)

    def mock_isfile(path):
        return False

    monkeypatch.setattr(os.path, 'isdir', mock_isdir)
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)

    module_path, has_code, package_path = _AnsibleCollectionPkgLoaderBase._module_file_from_path(test_leaf_name, test_path)

    assert module_path == test_module_path
    assert has_code is False
    assert package_path == test_package_path

def test_module_file_from_path_module(monkeypatch):
    test_leaf_name = 'test_module'
    test_path = '/test/path'
    test_module_path = os.path.join(to_native(test_path), to_native(test_leaf_name) + '.py')

    def mock_isdir(path):
        return False

    def mock_isfile(path):
        return path == to_bytes(test_module_path)

    monkeypatch.setattr(os.path, 'isdir', mock_isdir)
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)

    module_path, has_code, package_path = _AnsibleCollectionPkgLoaderBase._module_file_from_path(test_leaf_name, test_path)

    assert module_path == test_module_path
    assert has_code is True
    assert package_path is None

def test_module_file_from_path_module_not_found(monkeypatch):
    test_leaf_name = 'test_module'
    test_path = '/test/path'
    test_module_path = os.path.join(to_native(test_path), to_native(test_leaf_name) + '.py')

    def mock_isdir(path):
        return False

    def mock_isfile(path):
        return False

    monkeypatch.setattr(os.path, 'isdir', mock_isdir)
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)

    with pytest.raises(ImportError, match=f'{test_leaf_name} not found at {test_path}'):
        _AnsibleCollectionPkgLoaderBase._module_file_from_path(test_leaf_name, test_path)
