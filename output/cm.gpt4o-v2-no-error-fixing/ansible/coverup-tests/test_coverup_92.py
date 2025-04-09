# file: lib/ansible/utils/collection_loader/_collection_finder.py:359-378
# asked: {"lines": [359, 360, 361, 362, 363, 366, 368, 369, 370, 371, 373, 374, 375, 376, 378], "branches": [[366, 368], [366, 373], [369, 370], [369, 378], [375, 376], [375, 378]]}
# gained: {"lines": [359, 360, 361, 362, 363, 366, 368, 369, 370, 371, 373, 374, 375, 376, 378], "branches": [[366, 368], [366, 373], [369, 370], [369, 378], [375, 376], [375, 378]]}

import os
import pytest
from ansible.module_utils.common.text.converters import to_native, to_bytes
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

def test_module_file_from_path_package_with_init(monkeypatch, tmp_path):
    leaf_name = 'test_package'
    path = tmp_path / leaf_name
    init_file = path / '__init__.py'
    os.makedirs(path)
    init_file.touch()

    module_path, has_code, package_path = _AnsibleCollectionPkgLoaderBase._module_file_from_path(leaf_name, tmp_path)

    assert module_path == str(init_file)
    assert has_code is True
    assert package_path == str(path)

def test_module_file_from_path_package_without_init(monkeypatch, tmp_path):
    leaf_name = 'test_package'
    path = tmp_path / leaf_name
    os.makedirs(path)

    module_path, has_code, package_path = _AnsibleCollectionPkgLoaderBase._module_file_from_path(leaf_name, tmp_path)

    assert module_path == str(path / '__synthetic__')
    assert has_code is False
    assert package_path == str(path)

def test_module_file_from_path_module(monkeypatch, tmp_path):
    leaf_name = 'test_module'
    path = tmp_path
    module_file = path / (leaf_name + '.py')
    module_file.touch()

    module_path, has_code, package_path = _AnsibleCollectionPkgLoaderBase._module_file_from_path(leaf_name, tmp_path)

    assert module_path == str(module_file)
    assert has_code is True
    assert package_path is None

def test_module_file_from_path_module_not_found(monkeypatch, tmp_path):
    leaf_name = 'test_module'
    path = tmp_path

    with pytest.raises(ImportError, match=f'{leaf_name} not found at {tmp_path}'):
        _AnsibleCollectionPkgLoaderBase._module_file_from_path(leaf_name, tmp_path)
