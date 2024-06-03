# file flutils/pathutils.py:574-621
# lines [609, 610, 611, 613, 614, 615, 617]
# branches ['608->609', '610->608', '610->611', '612->613', '614->615', '614->617', '618->exit']

import os
import pytest
import tempfile
from unittest.mock import patch
from flutils.pathutils import path_absent

def test_path_absent_file(mocker):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file_path = tmp_file.name

    assert os.path.exists(tmp_file_path)
    path_absent(tmp_file_path)
    assert not os.path.exists(tmp_file_path)

def test_path_absent_symlink(mocker):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file_path = tmp_file.name

    symlink_path = tmp_file_path + "_symlink"
    os.symlink(tmp_file_path, symlink_path)

    assert os.path.exists(symlink_path)
    path_absent(symlink_path)
    assert not os.path.exists(symlink_path)
    assert os.path.exists(tmp_file_path)

    os.unlink(tmp_file_path)

def test_path_absent_directory(mocker):
    with tempfile.TemporaryDirectory() as tmp_dir:
        sub_dir = os.path.join(tmp_dir, "sub_dir")
        os.mkdir(sub_dir)
        file_path = os.path.join(sub_dir, "file.txt")
        with open(file_path, "w") as f:
            f.write("test")

        symlink_path = os.path.join(sub_dir, "symlink")
        os.symlink(file_path, symlink_path)

        assert os.path.exists(tmp_dir)
        assert os.path.exists(sub_dir)
        assert os.path.exists(file_path)
        assert os.path.exists(symlink_path)

        path_absent(tmp_dir)

        assert not os.path.exists(tmp_dir)
        assert not os.path.exists(sub_dir)
        assert not os.path.exists(file_path)
        assert not os.path.exists(symlink_path)
