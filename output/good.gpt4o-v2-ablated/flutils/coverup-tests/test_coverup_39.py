# file: flutils/setuputils/cfg.py:134-154
# asked: {"lines": [], "branches": [[148, 145]]}
# gained: {"lines": [], "branches": [[148, 145]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from flutils.setuputils.cfg import _prep_setup_dir

def _validate_setup_dir(setup_dir):
    # Mock implementation of _validate_setup_dir for testing purposes
    if not os.path.isdir(setup_dir):
        raise ValueError(f"Invalid setup directory: {setup_dir}")

@pytest.fixture
def mock_validate_setup_dir(monkeypatch):
    monkeypatch.setattr('flutils.setuputils.cfg._validate_setup_dir', _validate_setup_dir)

def test_prep_setup_dir_with_valid_setup_dir(mock_validate_setup_dir, tmp_path):
    setup_dir = tmp_path / "valid_setup_dir"
    setup_dir.mkdir()
    result = _prep_setup_dir(setup_dir)
    assert result == os.path.realpath(str(setup_dir))

def test_prep_setup_dir_with_invalid_setup_dir(mock_validate_setup_dir, tmp_path):
    setup_dir = tmp_path / "invalid_setup_dir"
    with pytest.raises(ValueError):
        _prep_setup_dir(setup_dir)

@patch('flutils.setuputils.cfg.extract_stack')
def test_prep_setup_dir_finds_setup_py(mock_extract_stack, mock_validate_setup_dir, tmp_path):
    setup_dir = tmp_path / "project"
    setup_dir.mkdir()
    setup_py = setup_dir / "setup.py"
    setup_py.touch()

    frame_summary = MagicMock()
    frame_summary.filename = str(setup_py)
    mock_extract_stack.return_value = [frame_summary]

    result = _prep_setup_dir()
    assert result == os.path.realpath(str(setup_dir))

@patch('flutils.setuputils.cfg.extract_stack')
def test_prep_setup_dir_raises_file_not_found(mock_extract_stack, mock_validate_setup_dir):
    frame_summary = MagicMock()
    frame_summary.filename = "not_setup.py"
    mock_extract_stack.return_value = [frame_summary]

    with pytest.raises(FileNotFoundError):
        _prep_setup_dir()
