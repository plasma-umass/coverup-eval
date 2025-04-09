# file lib/ansible/utils/collection_loader/_collection_finder.py:1024-1048
# lines [1024, 1026, 1027, 1029, 1032, 1033, 1034, 1035, 1036, 1037, 1040, 1041, 1044, 1047, 1048]
# branches ['1026->1027', '1026->1029', '1032->exit', '1032->1033', '1033->1034', '1033->1035', '1035->1032', '1035->1036', '1037->1040', '1037->1047', '1040->1041', '1040->1044', '1047->1035', '1047->1048']

import os
import pytest
from ansible.utils.collection_loader._collection_finder import _iter_modules_impl
from ansible.module_utils._text import to_bytes, to_native

@pytest.fixture
def create_test_directory(tmp_path):
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    (test_dir / "__pycache__").mkdir()
    (test_dir / "test_package").mkdir()
    (test_dir / "test_package" / "__init__.py").write_text("# test package")
    (test_dir / "test_module.py").write_text("# test module")
    (test_dir / "not_a_python_file.txt").write_text("Not a python file")
    return test_dir

def test__iter_modules_impl(create_test_directory):
    test_dir = create_test_directory
    paths = [str(test_dir)]
    modules = list(_iter_modules_impl(paths))
    assert ('test_package', True) in modules, "Expected to find the test_package as a package"
    assert ('test_module', False) in modules, "Expected to find the test_module as a module"
    assert ('__pycache__', True) not in modules, "Expected not to find __pycache__"
    assert ('not_a_python_file', False) not in modules, "Expected not to find not_a_python_file"
