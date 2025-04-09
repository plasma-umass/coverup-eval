# file: flutils/setuputils/cfg.py:108-131
# asked: {"lines": [108, 110, 111, 112, 113, 115, 116, 117, 118, 120, 121, 122, 123, 124, 126, 127, 128, 129, 130], "branches": [[110, 111], [110, 115], [115, 116], [115, 120], [121, 122], [121, 126], [127, 0], [127, 128]]}
# gained: {"lines": [108, 110, 111, 112, 113, 115, 116, 117, 118, 120, 121, 122, 123, 124, 126, 127, 128, 129, 130], "branches": [[110, 111], [110, 115], [115, 116], [115, 120], [121, 122], [121, 126], [127, 0], [127, 128]]}

import os
import pytest
from flutils.setuputils.cfg import _validate_setup_dir

def test_validate_setup_dir_not_exist(tmp_path):
    non_existent_dir = tmp_path / "non_existent"
    with pytest.raises(FileNotFoundError, match="The given 'setup_dir' of .* does NOT exist."):
        _validate_setup_dir(str(non_existent_dir))

def test_validate_setup_dir_not_a_directory(tmp_path):
    not_a_directory = tmp_path / "not_a_directory"
    not_a_directory.touch()  # Create a file instead of a directory
    with pytest.raises(NotADirectoryError, match="The given 'setup_dir' of .* is NOT a directory."):
        _validate_setup_dir(str(not_a_directory))

def test_validate_setup_dir_no_setup_py(tmp_path):
    valid_dir = tmp_path / "valid_dir"
    valid_dir.mkdir()
    (valid_dir / "setup.cfg").touch()  # Only create setup.cfg
    with pytest.raises(FileNotFoundError, match="The given 'setup_dir' of .* does NOT contain a setup.py file."):
        _validate_setup_dir(str(valid_dir))

def test_validate_setup_dir_no_setup_cfg(tmp_path):
    valid_dir = tmp_path / "valid_dir"
    valid_dir.mkdir()
    (valid_dir / "setup.py").touch()  # Only create setup.py
    with pytest.raises(FileNotFoundError, match="The given 'setup_dir' of .* does NOT contain a setup.cfg file."):
        _validate_setup_dir(str(valid_dir))

def test_validate_setup_dir_valid(tmp_path):
    valid_dir = tmp_path / "valid_dir"
    valid_dir.mkdir()
    (valid_dir / "setup.py").touch()
    (valid_dir / "setup.cfg").touch()
    # Should not raise any exceptions
    _validate_setup_dir(str(valid_dir))
