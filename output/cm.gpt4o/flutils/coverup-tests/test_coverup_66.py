# file flutils/pathutils.py:219-333
# lines []
# branches ['306->321', '321->324']

import pytest
from flutils.pathutils import directory_present
from pathlib import Path
import os
import shutil

def test_directory_present_creates_directories_with_mode(mocker):
    # Setup
    base_path = Path('/tmp/test_directory_present')
    test_path = base_path / 'subdir1' / 'subdir2'
    
    # Ensure the base path is clean before the test
    if base_path.exists():
        shutil.rmtree(base_path)
    
    # Mocking chown to avoid changing actual file ownership
    mocker.patch('flutils.pathutils.chown')
    
    # Test
    result_path = directory_present(test_path, mode=0o755)
    
    # Assertions
    assert result_path == test_path
    assert test_path.exists()
    assert test_path.is_dir()
    assert oct(test_path.stat().st_mode & 0o777) == '0o755'
    
    # Cleanup
    shutil.rmtree(base_path)

def test_directory_present_existing_directory_with_mode(mocker):
    # Setup
    base_path = Path('/tmp/test_directory_present')
    test_path = base_path / 'subdir1' / 'subdir2'
    
    # Ensure the base path is clean before the test
    if base_path.exists():
        shutil.rmtree(base_path)
    
    # Create the directory structure beforehand
    test_path.mkdir(parents=True, exist_ok=True)
    
    # Mocking chown to avoid changing actual file ownership
    mocker.patch('flutils.pathutils.chown')
    
    # Test
    result_path = directory_present(test_path, mode=0o755)
    
    # Assertions
    assert result_path == test_path
    assert test_path.exists()
    assert test_path.is_dir()
    assert oct(test_path.stat().st_mode & 0o777) == '0o755'
    
    # Cleanup
    shutil.rmtree(base_path)
