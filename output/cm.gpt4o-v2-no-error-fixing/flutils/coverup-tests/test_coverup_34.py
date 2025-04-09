# file: flutils/setuputils/cfg.py:134-154
# asked: {"lines": [134, 135, 140, 141, 142, 143, 145, 146, 147, 148, 149, 150, 151, 152, 153], "branches": [[140, 141], [140, 145], [145, 146], [145, 152], [148, 145], [148, 149]]}
# gained: {"lines": [134, 135, 140, 141, 142, 143, 145, 146, 147, 148, 149, 150, 151, 152, 153], "branches": [[140, 141], [140, 145], [145, 146], [145, 152], [148, 145], [148, 149]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from flutils.setuputils.cfg import _prep_setup_dir, _validate_setup_dir

def test_prep_setup_dir_with_valid_setup_dir(monkeypatch):
    setup_dir = "/valid/setup/dir"
    
    def mock_validate_setup_dir(path):
        assert path == setup_dir
    
    monkeypatch.setattr('flutils.setuputils.cfg._validate_setup_dir', mock_validate_setup_dir)
    
    result = _prep_setup_dir(setup_dir)
    assert result == os.path.realpath(setup_dir)

def test_prep_setup_dir_with_invalid_setup_dir(monkeypatch):
    setup_dir = "/invalid/setup/dir"
    
    def mock_validate_setup_dir(path):
        raise FileNotFoundError("The given 'setup_dir' of %r does NOT exist." % path)
    
    monkeypatch.setattr('flutils.setuputils.cfg._validate_setup_dir', mock_validate_setup_dir)
    
    with pytest.raises(FileNotFoundError):
        _prep_setup_dir(setup_dir)

def test_prep_setup_dir_without_setup_dir_finds_setup_py(monkeypatch):
    fake_stack = [
        MagicMock(filename='/some/other/file.py'),
        MagicMock(filename='/valid/setup/dir/setup.py')
    ]
    
    def mock_extract_stack():
        return fake_stack
    
    def mock_validate_setup_dir(path):
        assert path == "/valid/setup/dir"
    
    monkeypatch.setattr('flutils.setuputils.cfg.extract_stack', mock_extract_stack)
    monkeypatch.setattr('flutils.setuputils.cfg._validate_setup_dir', mock_validate_setup_dir)
    
    result = _prep_setup_dir()
    assert result == os.path.realpath("/valid/setup/dir")

def test_prep_setup_dir_without_setup_dir_raises_file_not_found(monkeypatch):
    fake_stack = [
        MagicMock(filename='/some/other/file.py'),
        MagicMock(filename='/another/file.py')
    ]
    
    def mock_extract_stack():
        return fake_stack
    
    monkeypatch.setattr('flutils.setuputils.cfg.extract_stack', mock_extract_stack)
    
    with pytest.raises(FileNotFoundError):
        _prep_setup_dir()
