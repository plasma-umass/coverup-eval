# file: lib/ansible/utils/collection_loader/_collection_finder.py:1024-1048
# asked: {"lines": [1026, 1027, 1029, 1032, 1033, 1034, 1035, 1036, 1037, 1040, 1041, 1044, 1047, 1048], "branches": [[1026, 1027], [1026, 1029], [1032, 0], [1032, 1033], [1033, 1034], [1033, 1035], [1035, 1032], [1035, 1036], [1037, 1040], [1037, 1047], [1040, 1041], [1040, 1044], [1047, 1035], [1047, 1048]]}
# gained: {"lines": [1026, 1027, 1029, 1032, 1033, 1035, 1036, 1037, 1040, 1041, 1044, 1047, 1048], "branches": [[1026, 1027], [1026, 1029], [1032, 0], [1032, 1033], [1033, 1035], [1035, 1032], [1035, 1036], [1037, 1040], [1037, 1047], [1040, 1041], [1040, 1044], [1047, 1048]]}

import os
import pytest
from ansible.utils.collection_loader._collection_finder import _iter_modules_impl
from ansible.module_utils.common.text.converters import to_native, to_bytes

@pytest.fixture
def setup_test_environment(tmp_path):
    # Setup a temporary directory structure
    base_dir = tmp_path / "test_dir"
    base_dir.mkdir()
    
    # Create subdirectories and files
    (base_dir / "subdir").mkdir()
    (base_dir / "subdir" / "__init__.py").write_text("")
    (base_dir / "module.py").write_text("")
    (base_dir / "__pycache__").mkdir()
    (base_dir / "__pycache__" / "cached.pyc").write_text("")
    (base_dir / "invalid.dir").mkdir()
    
    yield base_dir
    
    # Cleanup is handled by pytest's tmp_path fixture

def test_iter_modules_impl_no_prefix(setup_test_environment):
    base_dir = setup_test_environment
    paths = [str(base_dir)]
    
    result = sorted(list(_iter_modules_impl(paths)))
    
    expected = [
        ('module', False),
        ('subdir', True)
    ]
    
    assert result == expected

def test_iter_modules_impl_with_prefix(setup_test_environment):
    base_dir = setup_test_environment
    paths = [str(base_dir)]
    prefix = 'prefix_'
    
    result = sorted(list(_iter_modules_impl(paths, prefix)))
    
    expected = [
        ('prefix_module', False),
        ('prefix_subdir', True)
    ]
    
    assert result == expected
