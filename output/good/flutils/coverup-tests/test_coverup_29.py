# file flutils/setuputils/cfg.py:134-154
# lines [134, 135, 140, 141, 142, 143, 145, 146, 147, 148, 149, 150, 151, 152, 153]
# branches ['140->141', '140->145', '145->146', '145->152', '148->145', '148->149']

import os
import pytest
from flutils.setuputils.cfg import _prep_setup_dir
from unittest.mock import patch, MagicMock

# Test function to cover the case where setup_dir is provided
def test_prep_setup_dir_with_setup_dir(tmp_path):
    setup_dir = tmp_path / "project"
    setup_dir.mkdir()
    setup_py = setup_dir / "setup.py"
    setup_py.touch()

    with patch('flutils.setuputils.cfg._validate_setup_dir') as mock_validate:
        result = _prep_setup_dir(setup_dir)
        mock_validate.assert_called_once_with(str(setup_dir))
        assert result == str(setup_dir.resolve())

# Test function to cover the case where setup_dir is not provided
def test_prep_setup_dir_without_setup_dir(tmp_path):
    setup_dir = tmp_path / "project"
    setup_dir.mkdir()
    setup_py = setup_dir / "setup.py"
    setup_py.touch()

    with patch('flutils.setuputils.cfg.extract_stack') as mock_extract_stack:
        mock_frame = MagicMock()
        mock_frame.filename = str(setup_py)
        mock_extract_stack.return_value = [mock_frame]

        with patch('flutils.setuputils.cfg._validate_setup_dir') as mock_validate:
            result = _prep_setup_dir()
            mock_validate.assert_called_once_with(str(setup_dir))
            assert result == str(setup_dir.resolve())

# Test function to cover the case where 'setup.py' is not found
def test_prep_setup_dir_file_not_found():
    with patch('flutils.setuputils.cfg.extract_stack', return_value=[]):
        with pytest.raises(FileNotFoundError) as exc_info:
            _prep_setup_dir()
        assert "Unable to find the directory that contains the 'setup.py' file." in str(exc_info.value)
