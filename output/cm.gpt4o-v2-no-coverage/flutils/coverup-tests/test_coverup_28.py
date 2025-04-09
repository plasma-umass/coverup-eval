# file: flutils/setuputils/cfg.py:108-131
# asked: {"lines": [108, 110, 111, 112, 113, 115, 116, 117, 118, 120, 121, 122, 123, 124, 126, 127, 128, 129, 130], "branches": [[110, 111], [110, 115], [115, 116], [115, 120], [121, 122], [121, 126], [127, 0], [127, 128]]}
# gained: {"lines": [108, 110, 111, 112, 113, 115, 116, 117, 118, 120, 121, 122, 123, 124, 126, 127, 128, 129, 130], "branches": [[110, 111], [110, 115], [115, 116], [115, 120], [121, 122], [121, 126], [127, 0], [127, 128]]}

import os
import pytest
from flutils.setuputils.cfg import _validate_setup_dir

def test_validate_setup_dir_exists_not_directory(tmp_path):
    # Create a file instead of a directory
    setup_dir = tmp_path / "not_a_directory"
    setup_dir.write_text("This is a file, not a directory.")
    
    with pytest.raises(NotADirectoryError):
        _validate_setup_dir(str(setup_dir))

def test_validate_setup_dir_no_setup_py(tmp_path):
    # Create a valid directory without setup.py
    setup_dir = tmp_path / "valid_directory"
    setup_dir.mkdir()
    
    with pytest.raises(FileNotFoundError):
        _validate_setup_dir(str(setup_dir))

def test_validate_setup_dir_no_setup_cfg(tmp_path):
    # Create a valid directory with setup.py but without setup.cfg
    setup_dir = tmp_path / "valid_directory"
    setup_dir.mkdir()
    (setup_dir / "setup.py").write_text("print('setup.py')")
    
    with pytest.raises(FileNotFoundError):
        _validate_setup_dir(str(setup_dir))

def test_validate_setup_dir_valid(tmp_path):
    # Create a valid directory with both setup.py and setup.cfg
    setup_dir = tmp_path / "valid_directory"
    setup_dir.mkdir()
    (setup_dir / "setup.py").write_text("print('setup.py')")
    (setup_dir / "setup.cfg").write_text("[metadata]\nname = example")
    
    # Should not raise any exceptions
    _validate_setup_dir(str(setup_dir))

def test_validate_setup_dir_not_exists():
    # Test with a directory that does not exist
    with pytest.raises(FileNotFoundError):
        _validate_setup_dir("non_existent_directory")
