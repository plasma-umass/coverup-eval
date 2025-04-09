# file: flutils/setuputils/cfg.py:134-154
# asked: {"lines": [134, 135, 140, 141, 142, 143, 145, 146, 147, 148, 149, 150, 151, 152, 153], "branches": [[140, 141], [140, 145], [145, 146], [145, 152], [148, 145], [148, 149]]}
# gained: {"lines": [134, 135, 140, 141, 142, 143, 145, 146, 147, 148, 149, 150, 151, 152, 153], "branches": [[140, 141], [140, 145], [145, 146], [145, 152], [148, 145], [148, 149]]}

import os
import pytest
from unittest import mock
from flutils.setuputils.cfg import _prep_setup_dir, _validate_setup_dir

def test_prep_setup_dir_with_valid_setup_dir(monkeypatch):
    valid_dir = "/valid/setup/dir"
    monkeypatch.setattr(os.path, "exists", lambda x: x == valid_dir)
    monkeypatch.setattr(os.path, "isdir", lambda x: x == valid_dir)
    monkeypatch.setattr(os.path, "isfile", lambda x: x in [os.path.join(valid_dir, 'setup.py'), os.path.join(valid_dir, 'setup.cfg')])
    result = _prep_setup_dir(valid_dir)
    assert result == os.path.realpath(valid_dir)

def test_prep_setup_dir_with_invalid_setup_dir(monkeypatch):
    invalid_dir = "/invalid/setup/dir"
    monkeypatch.setattr(os.path, "exists", lambda x: x != invalid_dir)
    with pytest.raises(FileNotFoundError):
        _prep_setup_dir(invalid_dir)

def test_prep_setup_dir_finds_setup_py_in_stack(monkeypatch):
    valid_dir = "/valid/setup/dir"
    frame_summary = mock.Mock()
    frame_summary.filename = os.path.join(valid_dir, 'setup.py')
    monkeypatch.setattr('flutils.setuputils.cfg.extract_stack', lambda: [frame_summary])
    monkeypatch.setattr(os.path, "exists", lambda x: x == valid_dir)
    monkeypatch.setattr(os.path, "isdir", lambda x: x == valid_dir)
    monkeypatch.setattr(os.path, "isfile", lambda x: x in [os.path.join(valid_dir, 'setup.py'), os.path.join(valid_dir, 'setup.cfg')])
    result = _prep_setup_dir()
    assert result == os.path.realpath(valid_dir)

def test_prep_setup_dir_raises_file_not_found_error(monkeypatch):
    frame_summary = mock.Mock()
    frame_summary.filename = "/some/other/file.py"
    monkeypatch.setattr('flutils.setuputils.cfg.extract_stack', lambda: [frame_summary])
    with pytest.raises(FileNotFoundError):
        _prep_setup_dir()
