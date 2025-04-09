# file: lib/ansible/utils/collection_loader/_collection_finder.py:1024-1048
# asked: {"lines": [1024, 1026, 1027, 1029, 1032, 1033, 1034, 1035, 1036, 1037, 1040, 1041, 1044, 1047, 1048], "branches": [[1026, 1027], [1026, 1029], [1032, 0], [1032, 1033], [1033, 1034], [1033, 1035], [1035, 1032], [1035, 1036], [1037, 1040], [1037, 1047], [1040, 1041], [1040, 1044], [1047, 1035], [1047, 1048]]}
# gained: {"lines": [1024, 1026, 1027, 1029, 1032, 1033, 1034, 1035, 1036, 1037, 1047, 1048], "branches": [[1026, 1027], [1026, 1029], [1032, 0], [1032, 1033], [1033, 1034], [1033, 1035], [1035, 1032], [1035, 1036], [1037, 1047], [1047, 1035], [1047, 1048]]}

import os
import pytest
from ansible.module_utils.common.text.converters import to_native, to_bytes
from ansible.utils.collection_loader._collection_finder import _iter_modules_impl

@pytest.fixture
def create_test_files(tmp_path):
    # Create test directories and files
    dir1 = tmp_path / "dir1"
    dir1.mkdir()
    (dir1 / "__init__.py").write_text("")
    (dir1 / "module1.py").write_text("")
    (dir1 / "module2.py").write_text("")
    (dir1 / "not_a_module.txt").write_text("")

    dir2 = tmp_path / "dir2"
    dir2.mkdir()
    (dir2 / "__init__.py").write_text("")
    (dir2 / "module3.py").write_text("")
    (dir2 / "module4.py").write_text("")
    (dir2 / "not_a_module.txt").write_text("")

    yield [str(dir1), str(dir2)]

    # Cleanup is handled by tmp_path fixture

def test_iter_modules_impl(create_test_files):
    paths = create_test_files
    modules = list(_iter_modules_impl(paths))

    expected_modules = [
        ('module1', False),
        ('module2', False),
        ('module3', False),
        ('module4', False)
    ]

    assert modules == expected_modules

def test_iter_modules_impl_with_prefix(create_test_files):
    paths = create_test_files
    modules = list(_iter_modules_impl(paths, prefix='ansible_collections.'))

    expected_modules = [
        ('ansible_collections.module1', False),
        ('ansible_collections.module2', False),
        ('ansible_collections.module3', False),
        ('ansible_collections.module4', False)
    ]

    assert modules == expected_modules

def test_iter_modules_impl_nonexistent_path():
    paths = ["/nonexistent_path"]
    modules = list(_iter_modules_impl(paths))
    assert modules == []

def test_iter_modules_impl_empty_path():
    paths = []
    modules = list(_iter_modules_impl(paths))
    assert modules == []
