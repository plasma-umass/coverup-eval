# file: flutils/setuputils/cfg.py:134-154
# asked: {"lines": [134, 135, 140, 141, 142, 143, 145, 146, 147, 148, 149, 150, 151, 152, 153], "branches": [[140, 141], [140, 145], [145, 146], [145, 152], [148, 145], [148, 149]]}
# gained: {"lines": [134, 135, 140, 141, 142, 143, 145, 146, 147, 148, 149, 150, 151, 152, 153], "branches": [[140, 141], [140, 145], [145, 146], [145, 152], [148, 145], [148, 149]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from flutils.setuputils.cfg import _prep_setup_dir

def _validate_setup_dir(setup_dir):
    # Mock implementation of _validate_setup_dir for testing purposes
    if not os.path.isdir(setup_dir):
        raise ValueError(f"Invalid setup directory: {setup_dir}")

@pytest.fixture(autouse=True)
def mock_validate_setup_dir(monkeypatch):
    monkeypatch.setattr('flutils.setuputils.cfg._validate_setup_dir', _validate_setup_dir)

def test_prep_setup_dir_with_valid_setup_dir(monkeypatch, tmp_path):
    setup_dir = tmp_path / "valid_setup_dir"
    setup_dir.mkdir()
    monkeypatch.setattr('os.path.isdir', lambda x: True)
    
    result = _prep_setup_dir(setup_dir)
    assert result == os.path.realpath(str(setup_dir))

def test_prep_setup_dir_with_invalid_setup_dir(monkeypatch, tmp_path):
    setup_dir = tmp_path / "invalid_setup_dir"
    
    with pytest.raises(ValueError):
        _prep_setup_dir(setup_dir)

def test_prep_setup_dir_finds_setup_py_in_stack(monkeypatch):
    fake_stack = [
        MagicMock(filename='/some/other/file.py'),
        MagicMock(filename='/path/to/setup.py')
    ]
    monkeypatch.setattr('flutils.setuputils.cfg.extract_stack', lambda: fake_stack)
    monkeypatch.setattr('os.path.isdir', lambda x: True)
    
    result = _prep_setup_dir()
    assert result == os.path.realpath('/path/to')

def test_prep_setup_dir_raises_file_not_found(monkeypatch):
    fake_stack = [
        MagicMock(filename='/some/other/file.py'),
        MagicMock(filename='/another/file.py')
    ]
    monkeypatch.setattr('flutils.setuputils.cfg.extract_stack', lambda: fake_stack)
    
    with pytest.raises(FileNotFoundError):
        _prep_setup_dir()
