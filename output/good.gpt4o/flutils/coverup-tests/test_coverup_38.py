# file flutils/setuputils/cfg.py:108-131
# lines [108, 110, 111, 112, 113, 115, 116, 117, 118, 120, 121, 122, 123, 124, 126, 127, 128, 129, 130]
# branches ['110->111', '110->115', '115->116', '115->120', '121->122', '121->126', '127->exit', '127->128']

import os
import pytest
from flutils.setuputils.cfg import _validate_setup_dir

def test_validate_setup_dir_file_not_found(mocker):
    mocker.patch('os.path.exists', return_value=False)
    with pytest.raises(FileNotFoundError, match="The given 'setup_dir' of 'nonexistent_dir' does NOT exist."):
        _validate_setup_dir('nonexistent_dir')

def test_validate_setup_dir_not_a_directory(mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isdir', return_value=False)
    with pytest.raises(NotADirectoryError, match="The given 'setup_dir' of 'not_a_dir' is NOT a directory."):
        _validate_setup_dir('not_a_dir')

def test_validate_setup_dir_missing_setup_py(mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isdir', return_value=True)
    mocker.patch('os.path.isfile', side_effect=lambda path: path.endswith('setup.cfg'))
    with pytest.raises(FileNotFoundError, match="The given 'setup_dir' of 'missing_setup_py' does NOT contain a setup.py file."):
        _validate_setup_dir('missing_setup_py')

def test_validate_setup_dir_missing_setup_cfg(mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isdir', return_value=True)
    mocker.patch('os.path.isfile', side_effect=lambda path: path.endswith('setup.py'))
    with pytest.raises(FileNotFoundError, match="The given 'setup_dir' of 'missing_setup_cfg' does NOT contain a setup.cfg file."):
        _validate_setup_dir('missing_setup_cfg')

def test_validate_setup_dir_valid(mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isdir', return_value=True)
    mocker.patch('os.path.isfile', return_value=True)
    # No exception should be raised for a valid setup_dir
    _validate_setup_dir('valid_setup_dir')
