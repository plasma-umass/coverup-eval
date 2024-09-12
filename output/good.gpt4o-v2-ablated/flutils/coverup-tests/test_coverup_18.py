# file: flutils/setuputils/cfg.py:134-154
# asked: {"lines": [134, 135, 140, 141, 142, 143, 145, 146, 147, 148, 149, 150, 151, 152, 153], "branches": [[140, 141], [140, 145], [145, 146], [145, 152], [148, 145], [148, 149]]}
# gained: {"lines": [134, 135, 140, 141, 142, 143, 145, 146, 147, 148, 149, 150, 151, 152, 153], "branches": [[140, 141], [140, 145], [145, 146], [145, 152], [148, 149]]}

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
    with pytest.raises(ValueError, match="Invalid setup directory"):
        _prep_setup_dir(setup_dir)

def test_prep_setup_dir_finds_setup_py(mock_validate_setup_dir, tmp_path, monkeypatch):
    setup_dir = tmp_path / "project"
    setup_dir.mkdir()
    setup_py = setup_dir / "setup.py"
    setup_py.touch()

    frame_summary_mock = MagicMock()
    frame_summary_mock.filename = str(setup_py)

    extract_stack_mock = MagicMock(return_value=[frame_summary_mock])
    monkeypatch.setattr('flutils.setuputils.cfg.extract_stack', extract_stack_mock)

    result = _prep_setup_dir()
    assert result == os.path.realpath(str(setup_dir))

def test_prep_setup_dir_raises_file_not_found_error(mock_validate_setup_dir, monkeypatch):
    extract_stack_mock = MagicMock(return_value=[])
    monkeypatch.setattr('flutils.setuputils.cfg.extract_stack', extract_stack_mock)

    with pytest.raises(FileNotFoundError, match="Unable to find the directory that contains the 'setup.py' file."):
        _prep_setup_dir()
