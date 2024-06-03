# file flutils/pathutils.py:574-621
# lines [615]
# branches ['610->608', '614->615', '618->exit']

import os
import pytest
import tempfile
from flutils.pathutils import path_absent

@pytest.fixture
def temp_dir():
    dirpath = tempfile.mkdtemp()
    yield dirpath
    if os.path.exists(dirpath):
        for root, dirs, files in os.walk(dirpath, topdown=False):
            for name in files:
                os.unlink(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(dirpath)

def test_path_absent_file(temp_dir):
    file_path = os.path.join(temp_dir, 'test_file')
    with open(file_path, 'w') as f:
        f.write('test')
    assert os.path.isfile(file_path)
    path_absent(file_path)
    assert not os.path.exists(file_path)

def test_path_absent_symlink(temp_dir):
    target_path = os.path.join(temp_dir, 'target')
    symlink_path = os.path.join(temp_dir, 'symlink')
    with open(target_path, 'w') as f:
        f.write('test')
    os.symlink(target_path, symlink_path)
    assert os.path.islink(symlink_path)
    path_absent(symlink_path)
    assert not os.path.exists(symlink_path)
    assert os.path.exists(target_path)
    path_absent(target_path)
    assert not os.path.exists(target_path)

def test_path_absent_directory_with_symlink(temp_dir):
    dir_path = os.path.join(temp_dir, 'test_dir')
    os.mkdir(dir_path)
    file_path = os.path.join(dir_path, 'test_file')
    with open(file_path, 'w') as f:
        f.write('test')
    symlink_path = os.path.join(dir_path, 'symlink')
    os.symlink(file_path, symlink_path)
    assert os.path.isdir(dir_path)
    assert os.path.isfile(file_path)
    assert os.path.islink(symlink_path)
    path_absent(dir_path)
    assert not os.path.exists(dir_path)
    assert not os.path.exists(file_path)
    assert not os.path.exists(symlink_path)

def test_path_absent_directory_with_nested_symlink(temp_dir):
    dir_path = os.path.join(temp_dir, 'test_dir')
    os.mkdir(dir_path)
    nested_dir_path = os.path.join(dir_path, 'nested_dir')
    os.mkdir(nested_dir_path)
    file_path = os.path.join(nested_dir_path, 'test_file')
    with open(file_path, 'w') as f:
        f.write('test')
    symlink_path = os.path.join(nested_dir_path, 'symlink')
    os.symlink(file_path, symlink_path)
    assert os.path.isdir(dir_path)
    assert os.path.isdir(nested_dir_path)
    assert os.path.isfile(file_path)
    assert os.path.islink(symlink_path)
    path_absent(dir_path)
    assert not os.path.exists(dir_path)
    assert not os.path.exists(nested_dir_path)
    assert not os.path.exists(file_path)
    assert not os.path.exists(symlink_path)

def test_path_absent_directory_with_symlinked_dir(temp_dir):
    dir_path = os.path.join(temp_dir, 'test_dir')
    os.mkdir(dir_path)
    nested_dir_path = os.path.join(dir_path, 'nested_dir')
    os.mkdir(nested_dir_path)
    symlinked_dir_path = os.path.join(dir_path, 'symlinked_dir')
    os.symlink(nested_dir_path, symlinked_dir_path)
    assert os.path.isdir(dir_path)
    assert os.path.isdir(nested_dir_path)
    assert os.path.islink(symlinked_dir_path)
    path_absent(dir_path)
    assert not os.path.exists(dir_path)
    assert not os.path.exists(nested_dir_path)
    assert not os.path.exists(symlinked_dir_path)
