# file flutils/setuputils/cfg.py:108-131
# lines [108, 110, 111, 112, 113, 115, 116, 117, 118, 120, 121, 122, 123, 124, 126, 127, 128, 129, 130]
# branches ['110->111', '110->115', '115->116', '115->120', '121->122', '121->126', '127->exit', '127->128']

import os
import pytest
from flutils.setuputils.cfg import _validate_setup_dir

def test_validate_setup_dir(tmp_path, mocker):
    # Test setup_dir does not exist
    non_existing_dir = tmp_path / "non_existing"
    with pytest.raises(FileNotFoundError) as excinfo:
        _validate_setup_dir(str(non_existing_dir))
    assert "does NOT exist" in str(excinfo.value)

    # Test setup_dir is not a directory
    not_a_dir = tmp_path / "not_a_dir.txt"
    not_a_dir.touch()
    with pytest.raises(NotADirectoryError) as excinfo:
        _validate_setup_dir(str(not_a_dir))
    assert "is NOT a directory" in str(excinfo.value)

    # Test setup_dir does not contain setup.py
    dir_without_setup_py = tmp_path / "dir_without_setup_py"
    dir_without_setup_py.mkdir()
    with pytest.raises(FileNotFoundError) as excinfo:
        _validate_setup_dir(str(dir_without_setup_py))
    assert "does NOT contain a setup.py" in str(excinfo.value)

    # Test setup_dir does not contain setup.cfg
    dir_without_setup_cfg = tmp_path / "dir_without_setup_cfg"
    dir_without_setup_cfg.mkdir()
    setup_py = dir_without_setup_cfg / "setup.py"
    setup_py.touch()
    with pytest.raises(FileNotFoundError) as excinfo:
        _validate_setup_dir(str(dir_without_setup_cfg))
    assert "does NOT contain a setup.cfg" in str(excinfo.value)

    # Test setup_dir is valid
    valid_dir = tmp_path / "valid_dir"
    valid_dir.mkdir()
    valid_setup_py = valid_dir / "setup.py"
    valid_setup_py.touch()
    valid_setup_cfg = valid_dir / "setup.cfg"
    valid_setup_cfg.touch()
    # No exception should be raised for a valid directory
    _validate_setup_dir(str(valid_dir))
