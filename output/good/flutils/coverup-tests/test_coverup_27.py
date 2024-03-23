# file flutils/pathutils.py:574-621
# lines [574, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 617, 618, 619, 621]
# branches ['603->exit', '603->604', '604->605', '604->606', '606->607', '606->621', '607->608', '607->618', '608->609', '608->612', '610->608', '610->611', '612->607', '612->613', '614->615', '614->617', '618->exit', '618->619']

import os
import pytest
from pathlib import Path
from flutils.pathutils import path_absent, normalize_path

@pytest.fixture
def temp_dir(tmp_path):
    # Create a temporary directory structure
    (tmp_path / 'subdir').mkdir()
    (tmp_path / 'subdir' / 'file.txt').write_text('content')
    (tmp_path / 'subdir' / 'link_to_file.txt').symlink_to('file.txt')
    (tmp_path / 'subdir' / 'subsubdir').mkdir()
    (tmp_path / 'subdir' / 'subsubdir' / 'nested_file.txt').write_text('nested content')
    return tmp_path

def test_path_absent_directory(temp_dir):
    subdir_path = temp_dir / 'subdir'
    path_absent(subdir_path)
    assert not subdir_path.exists()

def test_path_absent_file(temp_dir):
    file_path = temp_dir / 'subdir' / 'file.txt'
    path_absent(file_path)
    assert not file_path.exists()

def test_path_absent_symlink(temp_dir):
    symlink_path = temp_dir / 'subdir' / 'link_to_file.txt'
    path_absent(symlink_path)
    assert not symlink_path.exists()

def test_path_absent_nonexistent(temp_dir):
    nonexistent_path = temp_dir / 'nonexistent'
    path_absent(nonexistent_path)
    assert not nonexistent_path.exists()
