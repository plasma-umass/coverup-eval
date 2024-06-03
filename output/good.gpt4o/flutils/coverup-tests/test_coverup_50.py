# file flutils/pathutils.py:387-414
# lines [387, 412, 413, 414]
# branches []

import pytest
from flutils.pathutils import find_paths
from pathlib import Path
import os

@pytest.fixture
def setup_test_environment(tmp_path):
    # Create a temporary directory and files for testing
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    (test_dir / "file1.txt").write_text("content1")
    (test_dir / "file2.txt").write_text("content2")
    (test_dir / "subdir").mkdir()
    (test_dir / "subdir" / "file3.txt").write_text("content3")
    
    yield test_dir
    
    # Cleanup is handled by tmp_path fixture

def test_find_paths(setup_test_environment):
    test_dir = setup_test_environment
    
    # Test finding all .txt files in the test directory
    pattern = test_dir / "*.txt"
    found_paths = list(find_paths(pattern))
    expected_paths = [test_dir / "file1.txt", test_dir / "file2.txt"]
    
    assert sorted(found_paths) == sorted(expected_paths)
    
    # Test finding all files in the subdirectory
    pattern = test_dir / "subdir" / "*"
    found_paths = list(find_paths(pattern))
    expected_paths = [test_dir / "subdir" / "file3.txt"]
    
    assert sorted(found_paths) == sorted(expected_paths)
    
    # Test finding all files recursively
    pattern = test_dir / "**" / "*"
    found_paths = [p for p in find_paths(pattern) if p.is_file()]
    expected_paths = [
        test_dir / "file1.txt",
        test_dir / "file2.txt",
        test_dir / "subdir" / "file3.txt"
    ]
    
    assert sorted(found_paths) == sorted(expected_paths)
