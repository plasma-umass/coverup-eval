# file: lib/ansible/module_utils/facts/system/distribution.py:30-44
# asked: {"lines": [30, 32, 33, 36, 37, 40, 41, 44], "branches": [[32, 33], [32, 36], [36, 37], [36, 40], [40, 41], [40, 44]]}
# gained: {"lines": [30, 32, 33, 36, 37, 40, 41, 44], "branches": [[32, 33], [32, 36], [36, 37], [36, 40], [40, 41], [40, 44]]}

import pytest
import os
from ansible.module_utils.facts.system.distribution import _file_exists

def test_file_exists(monkeypatch):
    # Test when file does not exist
    def mock_exists(path):
        return False

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    assert not _file_exists('/non/existent/path')

    # Test when file exists and allow_empty is True
    def mock_exists(path):
        return True

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    assert _file_exists('/existent/path', allow_empty=True)

    # Test when file exists, is empty, and allow_empty is False
    def mock_getsize(path):
        return 0

    monkeypatch.setattr(os.path, 'getsize', mock_getsize)
    assert not _file_exists('/existent/empty/path', allow_empty=False)

    # Test when file exists and is not empty
    def mock_getsize(path):
        return 10

    monkeypatch.setattr(os.path, 'getsize', mock_getsize)
    assert _file_exists('/existent/nonempty/path', allow_empty=False)
