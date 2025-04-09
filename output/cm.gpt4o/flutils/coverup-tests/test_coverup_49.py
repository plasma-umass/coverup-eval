# file flutils/setuputils/cfg.py:134-154
# lines [134, 135, 140, 141, 142, 143, 145, 146, 147, 148, 149, 150, 151, 152, 153]
# branches ['140->141', '140->145', '145->146', '145->152', '148->145', '148->149']

import os
import pytest
from unittest.mock import patch, MagicMock
from flutils.setuputils.cfg import _prep_setup_dir

def _validate_setup_dir(setup_dir):
    # Mock implementation of _validate_setup_dir for testing purposes
    if not os.path.exists(setup_dir):
        raise ValueError(f"Invalid setup directory: {setup_dir}")

@pytest.fixture
def mock_validate_setup_dir(monkeypatch):
    monkeypatch.setattr('flutils.setuputils.cfg._validate_setup_dir', _validate_setup_dir)

def test_prep_setup_dir_with_valid_setup_dir(mock_validate_setup_dir, tmp_path):
    setup_dir = tmp_path / "valid_setup_dir"
    setup_dir.mkdir()
    setup_file = setup_dir / "setup.py"
    setup_file.touch()

    result = _prep_setup_dir(setup_dir)
    assert result == os.path.realpath(setup_dir)

def test_prep_setup_dir_with_invalid_setup_dir(mock_validate_setup_dir, tmp_path):
    setup_dir = tmp_path / "invalid_setup_dir"

    with pytest.raises(ValueError, match="Invalid setup directory"):
        _prep_setup_dir(setup_dir)

def test_prep_setup_dir_finds_setup_py_in_stack(mock_validate_setup_dir, tmp_path):
    setup_dir = tmp_path / "valid_setup_dir"
    setup_dir.mkdir()
    setup_file = setup_dir / "setup.py"
    setup_file.touch()

    mock_stack = [
        MagicMock(filename='/some/other/file.py'),
        MagicMock(filename=str(setup_file))
    ]

    with patch('flutils.setuputils.cfg.extract_stack', return_value=mock_stack):
        result = _prep_setup_dir()
        assert result == os.path.realpath(setup_dir)

def test_prep_setup_dir_raises_file_not_found(mock_validate_setup_dir):
    mock_stack = [
        MagicMock(filename='/some/other/file.py'),
        MagicMock(filename='/another/file.py')
    ]

    with patch('flutils.setuputils.cfg.extract_stack', return_value=mock_stack):
        with pytest.raises(FileNotFoundError, match="Unable to find the directory that contains the 'setup.py' file."):
            _prep_setup_dir()
