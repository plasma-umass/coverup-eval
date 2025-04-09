# file: flutils/pathutils.py:574-621
# asked: {"lines": [613, 614, 615, 617], "branches": [[610, 608], [612, 613], [614, 615], [614, 617], [618, 0]]}
# gained: {"lines": [613, 614, 615, 617], "branches": [[612, 613], [614, 615], [614, 617]]}

import os
import pytest
import tempfile
from flutils.pathutils import path_absent

def test_path_absent_file():
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file_path = tmp_file.name

    assert os.path.exists(tmp_file_path)
    path_absent(tmp_file_path)
    assert not os.path.exists(tmp_file_path)

def test_path_absent_symlink():
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file_path = tmp_file.name

    symlink_path = tmp_file_path + "_symlink"
    os.symlink(tmp_file_path, symlink_path)

    assert os.path.islink(symlink_path)
    path_absent(symlink_path)
    assert not os.path.exists(symlink_path)
    os.unlink(tmp_file_path)  # Clean up the original file

def test_path_absent_directory_with_files_and_symlinks():
    with tempfile.TemporaryDirectory() as tmp_dir:
        file_path = os.path.join(tmp_dir, "file.txt")
        with open(file_path, "w") as f:
            f.write("test")

        sub_dir = os.path.join(tmp_dir, "subdir")
        os.mkdir(sub_dir)

        sub_file_path = os.path.join(sub_dir, "subfile.txt")
        with open(sub_file_path, "w") as f:
            f.write("test")

        symlink_path = os.path.join(sub_dir, "symlink")
        os.symlink(sub_file_path, symlink_path)

        assert os.path.exists(tmp_dir)
        assert os.path.exists(file_path)
        assert os.path.exists(sub_dir)
        assert os.path.exists(sub_file_path)
        assert os.path.islink(symlink_path)

        path_absent(tmp_dir)
        assert not os.path.exists(tmp_dir)

def test_path_absent_directory_with_symlink_to_dir():
    with tempfile.TemporaryDirectory() as tmp_dir:
        sub_dir = os.path.join(tmp_dir, "subdir")
        os.mkdir(sub_dir)

        symlink_path = os.path.join(tmp_dir, "symlink_to_subdir")
        os.symlink(sub_dir, symlink_path)

        assert os.path.exists(tmp_dir)
        assert os.path.exists(sub_dir)
        assert os.path.islink(symlink_path)

        path_absent(tmp_dir)
        assert not os.path.exists(tmp_dir)
