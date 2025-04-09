# file: lib/ansible/utils/collection_loader/_collection_finder.py:1024-1048
# asked: {"lines": [1026, 1027, 1029, 1032, 1033, 1034, 1035, 1036, 1037, 1040, 1041, 1044, 1047, 1048], "branches": [[1026, 1027], [1026, 1029], [1032, 0], [1032, 1033], [1033, 1034], [1033, 1035], [1035, 1032], [1035, 1036], [1037, 1040], [1037, 1047], [1040, 1041], [1040, 1044], [1047, 1035], [1047, 1048]]}
# gained: {"lines": [1026, 1027, 1029, 1032, 1033, 1035, 1036, 1037, 1040, 1041, 1044, 1047, 1048], "branches": [[1026, 1027], [1026, 1029], [1032, 0], [1032, 1033], [1033, 1035], [1035, 1032], [1035, 1036], [1037, 1040], [1037, 1047], [1040, 1041], [1040, 1044], [1047, 1035], [1047, 1048]]}

import os
import pytest
from ansible.utils.collection_loader._collection_finder import _iter_modules_impl
from ansible.module_utils.common.text.converters import to_native, to_bytes

def test_iter_modules_impl_no_prefix(tmp_path):
    # Create a temporary directory with some files and directories
    d = tmp_path / "testdir"
    d.mkdir()
    subdir = d / "subdir"
    subdir.mkdir()
    pyfile = d / "test.py"
    pyfile.write_text("print('hello world')")
    initfile = d / "__init__.py"
    initfile.write_text("")

    # Call the function
    result = list(_iter_modules_impl([str(d)]))

    # Check the results
    assert (to_native(subdir.name), True) in result
    assert (to_native(pyfile.stem), False) in result
    assert (to_native(initfile.stem), False) not in result

def test_iter_modules_impl_with_prefix(tmp_path):
    # Create a temporary directory with some files and directories
    d = tmp_path / "testdir"
    d.mkdir()
    subdir = d / "subdir"
    subdir.mkdir()
    pyfile = d / "test.py"
    pyfile.write_text("print('hello world')")
    initfile = d / "__init__.py"
    initfile.write_text("")

    # Call the function
    result = list(_iter_modules_impl([str(d)], prefix='prefix_'))

    # Check the results
    assert ('prefix_' + to_native(subdir.name), True) in result
    assert ('prefix_' + to_native(pyfile.stem), False) in result
    assert ('prefix_' + to_native(initfile.stem), False) not in result

def test_iter_modules_impl_ignore_non_dirs(tmp_path):
    # Create a temporary directory with some files and directories
    d = tmp_path / "testdir"
    d.mkdir()
    not_a_dir = d / "not_a_dir.txt"
    not_a_dir.write_text("I am not a directory")

    # Call the function
    result = list(_iter_modules_impl([str(d)]))

    # Check the results
    assert len(result) == 0

def test_iter_modules_impl_ignore_non_py_files(tmp_path):
    # Create a temporary directory with some files and directories
    d = tmp_path / "testdir"
    d.mkdir()
    txtfile = d / "test.txt"
    txtfile.write_text("I am a text file")

    # Call the function
    result = list(_iter_modules_impl([str(d)]))

    # Check the results
    assert len(result) == 0

def test_iter_modules_impl_ignore_pycache(tmp_path):
    # Create a temporary directory with some files and directories
    d = tmp_path / "testdir"
    d.mkdir()
    pycache = d / "__pycache__"
    pycache.mkdir()

    # Call the function
    result = list(_iter_modules_impl([str(d)]))

    # Check the results
    assert len(result) == 0
