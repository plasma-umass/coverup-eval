# file flutils/setuputils/cfg.py:134-154
# lines []
# branches ['148->145']

import os
import pytest
from flutils.setuputils.cfg import _prep_setup_dir
from unittest.mock import MagicMock

def test_prep_setup_dir_with_setup_py_in_call_stack(tmp_path, mocker):
    # Create a dummy setup.py in the temporary directory
    setup_py = tmp_path / "setup.py"
    setup_py.touch()

    # Mock the extract_stack function to return a frame without the setup.py
    # followed by a frame with the setup.py
    mock_frame_without_setup = MagicMock()
    mock_frame_without_setup.filename = str(tmp_path / "dummy.py")
    mock_frame_with_setup = MagicMock()
    mock_frame_with_setup.filename = str(setup_py)
    mocker.patch('flutils.setuputils.cfg.extract_stack', return_value=[mock_frame_without_setup, mock_frame_with_setup])

    # Mock the _validate_setup_dir function to do nothing
    mocker.patch('flutils.setuputils.cfg._validate_setup_dir')

    # Run the function and assert it finds the setup.py
    setup_dir = _prep_setup_dir()
    assert setup_dir == str(tmp_path.resolve()), "The _prep_setup_dir function did not find the setup.py file"

def test_prep_setup_dir_raises_file_not_found_error(mocker):
    # Mock the extract_stack function to return an empty list
    mocker.patch('flutils.setuputils.cfg.extract_stack', return_value=[])

    # Mock the _validate_setup_dir function to do nothing
    mocker.patch('flutils.setuputils.cfg._validate_setup_dir')

    # Run the function and assert it raises a FileNotFoundError
    with pytest.raises(FileNotFoundError) as exc_info:
        _prep_setup_dir()
    assert "Unable to find the directory that contains the 'setup.py' file." in str(exc_info.value)
