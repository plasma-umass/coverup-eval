# file: lib/ansible/plugins/filter/core.py:108-110
# asked: {"lines": [108, 110], "branches": []}
# gained: {"lines": [108, 110], "branches": []}

import pytest
import glob
import os.path

from ansible.plugins.filter.core import fileglob

def test_fileglob(monkeypatch):
    # Mocking glob.glob to return a predefined list of files
    mock_glob = ['file1.txt', 'file2.txt', 'dir1', 'file3.txt']
    monkeypatch.setattr(glob, 'glob', lambda _: mock_glob)
    
    # Mocking os.path.isfile to return True for files and False for directories
    monkeypatch.setattr(os.path, 'isfile', lambda path: path in ['file1.txt', 'file2.txt', 'file3.txt'])
    
    result = fileglob('dummy_path')
    
    # Asserting that the result contains only the files
    assert result == ['file1.txt', 'file2.txt', 'file3.txt']
