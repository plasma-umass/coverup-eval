# file: flutils/pathutils.py:574-621
# asked: {"lines": [574, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 617, 618, 619, 621], "branches": [[603, 0], [603, 604], [604, 605], [604, 606], [606, 607], [606, 621], [607, 608], [607, 618], [608, 609], [608, 612], [610, 608], [610, 611], [612, 607], [612, 613], [614, 615], [614, 617], [618, 0], [618, 619]]}
# gained: {"lines": [574, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 618, 619, 621], "branches": [[603, 0], [603, 604], [604, 605], [604, 606], [606, 607], [606, 621], [607, 608], [607, 618], [608, 609], [608, 612], [610, 611], [612, 607], [618, 619]]}

import os
import pytest
import tempfile
from pathlib import Path
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

    assert os.path.exists(symlink_path)
    path_absent(symlink_path)
    assert not os.path.exists(symlink_path)
    os.unlink(tmp_file_path)  # Clean up the original file

def test_path_absent_empty_directory():
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_dir_path = tmp_dir

    assert not os.path.exists(tmp_dir_path)
    path_absent(tmp_dir_path)
    assert not os.path.exists(tmp_dir_path)

def test_path_absent_directory_with_files():
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_dir_path = tmp_dir
        file_path = os.path.join(tmp_dir_path, "test_file")
        with open(file_path, "w") as f:
            f.write("test")

        assert os.path.exists(file_path)
        path_absent(tmp_dir_path)
        assert not os.path.exists(tmp_dir_path)

def test_path_absent_directory_with_symlinks():
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_dir_path = tmp_dir
        file_path = os.path.join(tmp_dir_path, "test_file")
        with open(file_path, "w") as f:
            f.write("test")

        symlink_path = os.path.join(tmp_dir_path, "test_symlink")
        os.symlink(file_path, symlink_path)

        assert os.path.exists(symlink_path)
        path_absent(tmp_dir_path)
        assert not os.path.exists(tmp_dir_path)
