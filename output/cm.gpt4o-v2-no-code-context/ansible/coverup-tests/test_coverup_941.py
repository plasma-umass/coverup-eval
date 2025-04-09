# file: lib/ansible/utils/collection_loader/_collection_finder.py:1024-1048
# asked: {"lines": [1026, 1027, 1029, 1032, 1033, 1034, 1035, 1036, 1037, 1040, 1041, 1044, 1047, 1048], "branches": [[1026, 1027], [1026, 1029], [1032, 0], [1032, 1033], [1033, 1034], [1033, 1035], [1035, 1032], [1035, 1036], [1037, 1040], [1037, 1047], [1040, 1041], [1040, 1044], [1047, 1035], [1047, 1048]]}
# gained: {"lines": [1026, 1027, 1029, 1032, 1033, 1035, 1036, 1037, 1040, 1041, 1044, 1047, 1048], "branches": [[1026, 1027], [1026, 1029], [1032, 0], [1032, 1033], [1033, 1035], [1035, 1032], [1035, 1036], [1037, 1040], [1037, 1047], [1040, 1041], [1040, 1044], [1047, 1035], [1047, 1048]]}

import os
import pytest
from ansible.utils.collection_loader._collection_finder import _iter_modules_impl

@pytest.fixture
def setup_test_environment(tmp_path):
    # Create a temporary directory structure for testing
    base_dir = tmp_path / "test_dir"
    base_dir.mkdir()
    
    # Create subdirectories and files
    (base_dir / "subdir").mkdir()
    (base_dir / "subdir" / "__init__.py").touch()
    (base_dir / "module.py").touch()
    (base_dir / "not_a_module.txt").touch()
    (base_dir / "__pycache__").mkdir()
    
    yield base_dir
    
    # Cleanup is handled by pytest's tmp_path fixture

def test_iter_modules_no_prefix(setup_test_environment):
    base_dir = setup_test_environment
    paths = [str(base_dir)]
    
    result = list(_iter_modules_impl(paths))
    
    expected = [
        ('module', False),
        ('subdir', True)
    ]
    
    assert result == expected

def test_iter_modules_with_prefix(setup_test_environment):
    base_dir = setup_test_environment
    paths = [str(base_dir)]
    
    result = list(_iter_modules_impl(paths, prefix='myprefix.'))
    
    expected = [
        ('myprefix.module', False),
        ('myprefix.subdir', True)
    ]
    
    assert result == expected

def test_iter_modules_ignore_non_python_files(setup_test_environment):
    base_dir = setup_test_environment
    paths = [str(base_dir)]
    
    result = list(_iter_modules_impl(paths))
    
    assert ('not_a_module', False) not in result
    assert ('__pycache__', True) not in result
