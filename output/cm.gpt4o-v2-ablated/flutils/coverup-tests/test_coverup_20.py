# file: flutils/setuputils/cfg.py:108-131
# asked: {"lines": [108, 110, 111, 112, 113, 115, 116, 117, 118, 120, 121, 122, 123, 124, 126, 127, 128, 129, 130], "branches": [[110, 111], [110, 115], [115, 116], [115, 120], [121, 122], [121, 126], [127, 0], [127, 128]]}
# gained: {"lines": [108, 110, 111, 112, 113, 115, 116, 117, 118, 120, 121, 122, 123, 124, 126, 127, 128, 129, 130], "branches": [[110, 111], [110, 115], [115, 116], [115, 120], [121, 122], [121, 126], [127, 0], [127, 128]]}

import os
import pytest
from flutils.setuputils.cfg import _validate_setup_dir

def test_validate_setup_dir_not_exist(tmp_path):
    non_existent_dir = tmp_path / "non_existent"
    with pytest.raises(FileNotFoundError, match="does NOT exist"):
        _validate_setup_dir(str(non_existent_dir))

def test_validate_setup_dir_not_directory(tmp_path):
    file_path = tmp_path / "file.txt"
    file_path.write_text("This is a file, not a directory.")
    with pytest.raises(NotADirectoryError, match="is NOT a directory"):
        _validate_setup_dir(str(file_path))

def test_validate_setup_dir_no_setup_py(tmp_path):
    setup_dir = tmp_path / "setup_dir"
    setup_dir.mkdir()
    (setup_dir / "setup.cfg").write_text("[metadata]\nname = example")
    with pytest.raises(FileNotFoundError, match="does NOT contain a setup.py"):
        _validate_setup_dir(str(setup_dir))

def test_validate_setup_dir_no_setup_cfg(tmp_path):
    setup_dir = tmp_path / "setup_dir"
    setup_dir.mkdir()
    (setup_dir / "setup.py").write_text("from setuptools import setup\nsetup()")
    with pytest.raises(FileNotFoundError, match="does NOT contain a setup.cfg"):
        _validate_setup_dir(str(setup_dir))

def test_validate_setup_dir_valid(tmp_path):
    setup_dir = tmp_path / "setup_dir"
    setup_dir.mkdir()
    (setup_dir / "setup.py").write_text("from setuptools import setup\nsetup()")
    (setup_dir / "setup.cfg").write_text("[metadata]\nname = example")
    _validate_setup_dir(str(setup_dir))
