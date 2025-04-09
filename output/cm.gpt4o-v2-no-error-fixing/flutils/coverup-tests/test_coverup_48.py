# file: flutils/setuputils/cfg.py:108-131
# asked: {"lines": [110, 111, 112, 113, 115, 116, 117, 118, 120, 121, 122, 123, 124, 126, 127, 128, 129, 130], "branches": [[110, 111], [110, 115], [115, 116], [115, 120], [121, 122], [121, 126], [127, 0], [127, 128]]}
# gained: {"lines": [110, 111, 112, 113, 115, 116, 117, 118, 120, 121, 122, 123, 124, 126, 127, 128, 129, 130], "branches": [[110, 111], [110, 115], [115, 116], [115, 120], [121, 122], [121, 126], [127, 0], [127, 128]]}

import os
import pytest
from flutils.setuputils.cfg import _validate_setup_dir

def test_validate_setup_dir_not_exists(tmp_path):
    with pytest.raises(FileNotFoundError, match="does NOT exist"):
        _validate_setup_dir(str(tmp_path / "non_existent_dir"))

def test_validate_setup_dir_not_directory(tmp_path):
    file_path = tmp_path / "file.txt"
    file_path.write_text("This is a file, not a directory.")
    with pytest.raises(NotADirectoryError, match="is NOT a directory"):
        _validate_setup_dir(str(file_path))

def test_validate_setup_dir_no_setup_py(tmp_path):
    os.makedirs(tmp_path / "valid_dir")
    with pytest.raises(FileNotFoundError, match="does NOT contain a setup.py file"):
        _validate_setup_dir(str(tmp_path / "valid_dir"))

def test_validate_setup_dir_no_setup_cfg(tmp_path):
    os.makedirs(tmp_path / "valid_dir")
    (tmp_path / "valid_dir" / "setup.py").write_text("print('setup.py')")
    with pytest.raises(FileNotFoundError, match="does NOT contain a setup.cfg file"):
        _validate_setup_dir(str(tmp_path / "valid_dir"))

def test_validate_setup_dir_valid(tmp_path):
    os.makedirs(tmp_path / "valid_dir")
    (tmp_path / "valid_dir" / "setup.py").write_text("print('setup.py')")
    (tmp_path / "valid_dir" / "setup.cfg").write_text("[metadata]")
    _validate_setup_dir(str(tmp_path / "valid_dir"))
