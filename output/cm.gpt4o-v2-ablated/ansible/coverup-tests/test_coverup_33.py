# file: lib/ansible/utils/collection_loader/_collection_finder.py:1024-1048
# asked: {"lines": [1024, 1026, 1027, 1029, 1032, 1033, 1034, 1035, 1036, 1037, 1040, 1041, 1044, 1047, 1048], "branches": [[1026, 1027], [1026, 1029], [1032, 0], [1032, 1033], [1033, 1034], [1033, 1035], [1035, 1032], [1035, 1036], [1037, 1040], [1037, 1047], [1040, 1041], [1040, 1044], [1047, 1035], [1047, 1048]]}
# gained: {"lines": [1024, 1026, 1027, 1029, 1032, 1033, 1035, 1036, 1037, 1040, 1041, 1044, 1047, 1048], "branches": [[1026, 1027], [1026, 1029], [1032, 0], [1032, 1033], [1033, 1035], [1035, 1032], [1035, 1036], [1037, 1040], [1037, 1047], [1040, 1041], [1040, 1044], [1047, 1035], [1047, 1048]]}

import os
import pytest
from ansible.utils.collection_loader._collection_finder import _iter_modules_impl
from ansible.module_utils._text import to_bytes, to_native

@pytest.fixture
def temp_dir(tmp_path):
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    yield dir_path
    # Cleanup is handled by tmp_path fixture

def test_iter_modules_impl_empty_dir(temp_dir):
    result = list(_iter_modules_impl([str(temp_dir)]))
    assert result == []

def test_iter_modules_impl_with_files(temp_dir):
    (temp_dir / "module1.py").write_text("")
    (temp_dir / "module2.py").write_text("")
    (temp_dir / "__init__.py").write_text("")
    result = list(_iter_modules_impl([str(temp_dir)]))
    assert result == [("module1", False), ("module2", False)]

def test_iter_modules_impl_with_dirs(temp_dir):
    (temp_dir / "pkg1").mkdir()
    (temp_dir / "pkg2").mkdir()
    (temp_dir / "pkg1" / "__init__.py").write_text("")
    (temp_dir / "pkg2" / "__init__.py").write_text("")
    result = list(_iter_modules_impl([str(temp_dir)]))
    assert result == [("pkg1", True), ("pkg2", True)]

def test_iter_modules_impl_with_mixed_content(temp_dir):
    (temp_dir / "module1.py").write_text("")
    (temp_dir / "pkg1").mkdir()
    (temp_dir / "pkg1" / "__init__.py").write_text("")
    (temp_dir / "__pycache__").mkdir()
    (temp_dir / "not_a_module.txt").write_text("")
    result = list(_iter_modules_impl([str(temp_dir)]))
    assert result == [("module1", False), ("pkg1", True)]

def test_iter_modules_impl_with_prefix(temp_dir):
    (temp_dir / "module1.py").write_text("")
    (temp_dir / "pkg1").mkdir()
    (temp_dir / "pkg1" / "__init__.py").write_text("")
    result = list(_iter_modules_impl([str(temp_dir)], prefix="prefix_"))
    assert result == [("prefix_module1", False), ("prefix_pkg1", True)]
