# file: flutils/pathutils.py:504-560
# asked: {"lines": [504, 505, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560], "branches": [[553, 554], [553, 555]]}
# gained: {"lines": [504, 505, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560], "branches": [[553, 554], [553, 555]]}

import pytest
from pathlib import Path
import os
from flutils.pathutils import normalize_path

def test_normalize_path_str(monkeypatch):
    home = str(Path.home())
    cwd = os.getcwd()
    
    # Test expanding user directory
    assert normalize_path('~/tmp/foo/../bar') == Path(home) / 'tmp/bar'
    
    # Test expanding environment variables
    monkeypatch.setenv('TEST_ENV', 'test_value')
    expected_path = Path(cwd) / 'test_value/tmp/bar'
    assert normalize_path('$TEST_ENV/tmp/foo/../bar') == expected_path
    
    # Test non-absolute path
    assert normalize_path('tmp/foo/../bar') == Path(cwd) / 'tmp/bar'
    
    # Test absolute path
    assert normalize_path('/tmp/foo/../bar') == Path('/tmp/bar')
    
    # Test redundant separators and up-level references
    assert normalize_path('A//B') == Path(cwd) / 'A/B'
    assert normalize_path('A/B/') == Path(cwd) / 'A/B'
    assert normalize_path('A/./B') == Path(cwd) / 'A/B'
    assert normalize_path('A/foo/../B') == Path(cwd) / 'A/B'

def test_normalize_path_bytes(monkeypatch):
    home = str(Path.home())
    cwd = os.getcwd()
    
    # Test expanding user directory
    assert normalize_path(b'~/tmp/foo/../bar') == Path(home) / 'tmp/bar'
    
    # Test expanding environment variables
    monkeypatch.setenv('TEST_ENV', 'test_value')
    expected_path = Path(cwd) / 'test_value/tmp/bar'
    assert normalize_path(b'$TEST_ENV/tmp/foo/../bar') == expected_path
    
    # Test non-absolute path
    assert normalize_path(b'tmp/foo/../bar') == Path(cwd) / 'tmp/bar'
    
    # Test absolute path
    assert normalize_path(b'/tmp/foo/../bar') == Path('/tmp/bar')
    
    # Test redundant separators and up-level references
    assert normalize_path(b'A//B') == Path(cwd) / 'A/B'
    assert normalize_path(b'A/B/') == Path(cwd) / 'A/B'
    assert normalize_path(b'A/./B') == Path(cwd) / 'A/B'
    assert normalize_path(b'A/foo/../B') == Path(cwd) / 'A/B'

def test_normalize_path_pathlib(monkeypatch):
    home = str(Path.home())
    cwd = os.getcwd()
    
    # Test expanding user directory
    assert normalize_path(Path('~/tmp/foo/../bar')) == Path(home) / 'tmp/bar'
    
    # Test expanding environment variables
    monkeypatch.setenv('TEST_ENV', 'test_value')
    expected_path = Path(cwd) / 'test_value/tmp/bar'
    assert normalize_path(Path('$TEST_ENV/tmp/foo/../bar')) == expected_path
    
    # Test non-absolute path
    assert normalize_path(Path('tmp/foo/../bar')) == Path(cwd) / 'tmp/bar'
    
    # Test absolute path
    assert normalize_path(Path('/tmp/foo/../bar')) == Path('/tmp/bar')
    
    # Test redundant separators and up-level references
    assert normalize_path(Path('A//B')) == Path(cwd) / 'A/B'
    assert normalize_path(Path('A/B/')) == Path(cwd) / 'A/B'
    assert normalize_path(Path('A/./B')) == Path(cwd) / 'A/B'
    assert normalize_path(Path('A/foo/../B')) == Path(cwd) / 'A/B'
