# file: lib/ansible/utils/collection_loader/_collection_finder.py:1024-1048
# asked: {"lines": [1034], "branches": [[1033, 1034]]}
# gained: {"lines": [1034], "branches": [[1033, 1034]]}

import os
import pytest
from ansible.utils.collection_loader._collection_finder import _iter_modules_impl
from ansible.module_utils._text import to_bytes, to_native

@pytest.fixture
def temp_dir(tmp_path):
    d = tmp_path / "test_dir"
    d.mkdir()
    yield d
    # Cleanup is handled by tmp_path fixture

def test_iter_modules_impl_empty_dir(temp_dir):
    result = list(_iter_modules_impl([str(temp_dir)]))
    assert result == []

def test_iter_modules_impl_with_files(temp_dir):
    (temp_dir / "module1.py").write_text("")
    (temp_dir / "module2.py").write_text("")
    (temp_dir / "__init__.py").write_text("")
    (temp_dir / "not_a_module.txt").write_text("")
    
    result = list(_iter_modules_impl([str(temp_dir)]))
    assert result == [("module1", False), ("module2", False)]

def test_iter_modules_impl_with_subdirs(temp_dir):
    subdir = temp_dir / "subdir"
    subdir.mkdir()
    (subdir / "__init__.py").write_text("")
    (temp_dir / "module1.py").write_text("")
    (temp_dir / "__pycache__").mkdir()
    
    result = list(_iter_modules_impl([str(temp_dir)]))
    assert result == [("module1", False), ("subdir", True)]

def test_iter_modules_impl_with_prefix(temp_dir):
    (temp_dir / "module1.py").write_text("")
    (temp_dir / "module2.py").write_text("")
    
    result = list(_iter_modules_impl([str(temp_dir)], prefix="prefix_"))
    assert result == [("prefix_module1", False), ("prefix_module2", False)]

def test_iter_modules_impl_nonexistent_path():
    result = list(_iter_modules_impl(["/nonexistent_path"]))
    assert result == []

def test_iter_modules_impl_ignore_non_python_dirs(temp_dir):
    (temp_dir / "module1.py").write_text("")
    (temp_dir / "not_a_module.txt").write_text("")
    (temp_dir / "subdir.notpy").mkdir()
    
    result = list(_iter_modules_impl([str(temp_dir)]))
    assert result == [("module1", False)]
