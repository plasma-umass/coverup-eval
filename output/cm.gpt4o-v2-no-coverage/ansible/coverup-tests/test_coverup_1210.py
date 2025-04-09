# file: lib/ansible/utils/collection_loader/_collection_finder.py:1024-1048
# asked: {"lines": [1041], "branches": [[1040, 1041]]}
# gained: {"lines": [1041], "branches": [[1040, 1041]]}

import os
import pytest
from ansible.module_utils.common.text.converters import to_native, to_bytes
from ansible.utils.collection_loader._collection_finder import _iter_modules_impl

@pytest.fixture
def create_test_files(tmp_path):
    # Create a temporary directory structure
    d = tmp_path / "test_dir"
    d.mkdir()
    sub_d = d / "sub_dir"
    sub_d.mkdir()
    py_file = d / "test_file.py"
    py_file.write_text("# test file")
    init_file = d / "__init__.py"
    init_file.write_text("# init file")
    pycache_dir = d / "__pycache__"
    pycache_dir.mkdir()
    yield d
    # Cleanup is handled by pytest

def test_iter_modules_impl_no_prefix(create_test_files):
    d = create_test_files
    result = list(_iter_modules_impl([str(d)]))
    assert result == [('sub_dir', True), ('test_file', False)]

def test_iter_modules_impl_with_prefix(create_test_files):
    d = create_test_files
    result = list(_iter_modules_impl([str(d)], prefix='prefix_'))
    assert result == [('prefix_sub_dir', True), ('prefix_test_file', False)]

def test_iter_modules_impl_nonexistent_dir(tmp_path):
    d = tmp_path / "nonexistent_dir"
    result = list(_iter_modules_impl([str(d)]))
    assert result == []

def test_iter_modules_impl_non_python_files(tmp_path):
    d = tmp_path / "test_dir"
    d.mkdir()
    non_py_file = d / "test_file.txt"
    non_py_file.write_text("test file")
    result = list(_iter_modules_impl([str(d)]))
    assert result == []

def test_iter_modules_impl_pycache(create_test_files):
    d = create_test_files
    result = list(_iter_modules_impl([str(d / "__pycache__")]))
    assert result == []
