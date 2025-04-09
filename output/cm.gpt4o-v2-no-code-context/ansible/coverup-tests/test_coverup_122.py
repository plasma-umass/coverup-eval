# file: lib/ansible/utils/collection_loader/_collection_finder.py:359-378
# asked: {"lines": [359, 360, 361, 362, 363, 366, 368, 369, 370, 371, 373, 374, 375, 376, 378], "branches": [[366, 368], [366, 373], [369, 370], [369, 378], [375, 376], [375, 378]]}
# gained: {"lines": [359, 360, 361, 362, 363, 366, 368, 369, 370, 371, 373, 374, 375, 376, 378], "branches": [[366, 368], [366, 373], [369, 370], [369, 378], [375, 376], [375, 378]]}

import os
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

@pytest.fixture
def setup_and_teardown(tmp_path):
    # Setup: create temporary directories and files
    package_dir = tmp_path / "package"
    package_dir.mkdir()
    init_file = package_dir / "__init__.py"
    init_file.touch()
    synthetic_file = package_dir / "__synthetic__"
    module_file = tmp_path / "module.py"
    module_file.touch()
    
    yield tmp_path, package_dir, init_file, synthetic_file, module_file
    
    # Teardown: cleanup is handled by tmp_path fixture

def test_module_file_from_path_package_with_init(setup_and_teardown):
    tmp_path, package_dir, init_file, synthetic_file, module_file = setup_and_teardown
    leaf_name = "package"
    path = str(tmp_path)
    
    module_path, has_code, package_path = _AnsibleCollectionPkgLoaderBase._module_file_from_path(leaf_name, path)
    
    assert module_path == str(init_file)
    assert has_code is True
    assert package_path == str(package_dir)

def test_module_file_from_path_package_without_init(setup_and_teardown):
    tmp_path, package_dir, init_file, synthetic_file, module_file = setup_and_teardown
    leaf_name = "package"
    path = str(tmp_path)
    
    init_file.unlink()  # Remove the __init__.py file
    
    module_path, has_code, package_path = _AnsibleCollectionPkgLoaderBase._module_file_from_path(leaf_name, path)
    
    assert module_path == str(synthetic_file)
    assert has_code is False
    assert package_path == str(package_dir)

def test_module_file_from_path_module(setup_and_teardown):
    tmp_path, package_dir, init_file, synthetic_file, module_file = setup_and_teardown
    leaf_name = "module"
    path = str(tmp_path)
    
    module_path, has_code, package_path = _AnsibleCollectionPkgLoaderBase._module_file_from_path(leaf_name, path)
    
    assert module_path == str(module_file)
    assert has_code is True
    assert package_path is None

def test_module_file_from_path_module_not_found(setup_and_teardown):
    tmp_path, package_dir, init_file, synthetic_file, module_file = setup_and_teardown
    leaf_name = "nonexistent_module"
    path = str(tmp_path)
    
    with pytest.raises(ImportError, match=f'{leaf_name} not found at {path}'):
        _AnsibleCollectionPkgLoaderBase._module_file_from_path(leaf_name, path)
