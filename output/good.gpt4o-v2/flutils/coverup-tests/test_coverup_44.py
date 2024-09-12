# file: flutils/pathutils.py:504-560
# asked: {"lines": [504, 505, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560], "branches": [[553, 554], [553, 555]]}
# gained: {"lines": [504, 505, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560], "branches": [[553, 554], [553, 555]]}

import pytest
import os
from pathlib import Path
from flutils.pathutils import normalize_path

def test_normalize_path_str(monkeypatch):
    # Test with a string path
    test_path = '~/tmp/foo/../bar'
    expected_path = Path(os.path.expanduser('~/tmp/bar')).resolve()
    
    result = normalize_path(test_path)
    assert result == expected_path

def test_normalize_path_bytes(monkeypatch):
    # Test with a bytes path
    test_path = b'~/tmp/foo/../bar'
    expected_path = Path(os.path.expanduser('~/tmp/bar')).resolve()
    
    result = normalize_path(test_path)
    assert result == expected_path

def test_normalize_path_pathlib(monkeypatch):
    # Test with a pathlib.Path object
    test_path = Path('~/tmp/foo/../bar')
    expected_path = Path(os.path.expanduser('~/tmp/bar')).resolve()
    
    result = normalize_path(test_path)
    assert result == expected_path

def test_normalize_path_env_var(monkeypatch):
    # Test with environment variable in path
    monkeypatch.setenv('TEST_VAR', 'tmp')
    test_path = '~/$TEST_VAR/foo/../bar'
    expected_path = Path(os.path.expanduser('~/tmp/bar')).resolve()
    
    result = normalize_path(test_path)
    assert result == expected_path

def test_normalize_path_relative(monkeypatch):
    # Test with a relative path
    test_path = 'foo/../bar'
    expected_path = Path(os.path.join(os.getcwd(), 'bar')).resolve()
    
    result = normalize_path(test_path)
    assert result == expected_path

def test_normalize_path_absolute(monkeypatch):
    # Test with an absolute path
    test_path = '/foo/../bar'
    expected_path = Path('/bar').resolve()
    
    result = normalize_path(test_path)
    assert result == expected_path
