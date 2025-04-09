# file lib/ansible/utils/collection_loader/_collection_finder.py:359-378
# lines [359, 360, 361, 362, 363, 366, 368, 369, 370, 371, 373, 374, 375, 376, 378]
# branches ['366->368', '366->373', '369->370', '369->378', '375->376', '375->378']

import os
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

@pytest.fixture
def create_module_files(tmp_path):
    module_name = "test_module"
    module_dir = tmp_path / module_name
    module_dir.mkdir()
    init_file = module_dir / "__init__.py"
    init_file.touch()
    synthetic_file = module_dir / "__synthetic__"
    synthetic_file.touch()
    return str(tmp_path), module_name

@pytest.fixture
def create_nonexistent_module_files(tmp_path):
    module_name = "nonexistent_module"
    module_path = tmp_path / (module_name + ".py")
    return str(tmp_path), module_name

def test_module_file_from_path_with_package(create_module_files):
    path, leaf_name = create_module_files
    module_path, has_code, package_path = _AnsibleCollectionPkgLoaderBase._module_file_from_path(leaf_name, path)
    assert os.path.isfile(module_path)
    assert has_code is True
    assert package_path is not None

def test_module_file_from_path_with_synthetic(create_module_files):
    path, leaf_name = create_module_files
    os.remove(os.path.join(path, leaf_name, "__init__.py"))
    module_path, has_code, package_path = _AnsibleCollectionPkgLoaderBase._module_file_from_path(leaf_name, path)
    assert os.path.isfile(module_path)
    assert has_code is False
    assert package_path is not None

def test_module_file_from_path_without_package(create_nonexistent_module_files):
    path, leaf_name = create_nonexistent_module_files
    with pytest.raises(ImportError) as excinfo:
        _AnsibleCollectionPkgLoaderBase._module_file_from_path(leaf_name, path)
    assert '{0} not found at {1}'.format(leaf_name, path) in str(excinfo.value)
