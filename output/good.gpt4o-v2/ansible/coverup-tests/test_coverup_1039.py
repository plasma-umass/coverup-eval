# file: lib/ansible/module_utils/facts/system/distribution.py:99-100
# asked: {"lines": [99, 100], "branches": []}
# gained: {"lines": [99, 100], "branches": []}

import pytest
from unittest import mock
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files():
    module = mock.MagicMock()
    return DistributionFiles(module)

def test_get_file_content_exists_readable(distribution_files, monkeypatch):
    path = "/tmp/testfile"
    content = "test content"

    def mock_exists(path):
        return True

    def mock_access(path, mode):
        return True

    def mock_open(*args, **kwargs):
        file_obj = mock.MagicMock()
        file_obj.read.return_value = content
        return file_obj

    monkeypatch.setattr("os.path.exists", mock_exists)
    monkeypatch.setattr("os.access", mock_access)
    monkeypatch.setattr("builtins.open", mock_open)

    result = distribution_files._get_file_content(path)
    assert result == content

def test_get_file_content_not_exists(distribution_files, monkeypatch):
    path = "/tmp/nonexistentfile"

    def mock_exists(path):
        return False

    monkeypatch.setattr("os.path.exists", mock_exists)

    result = distribution_files._get_file_content(path)
    assert result is None

def test_get_file_content_not_readable(distribution_files, monkeypatch):
    path = "/tmp/unreadablefile"

    def mock_exists(path):
        return True

    def mock_access(path, mode):
        return False

    monkeypatch.setattr("os.path.exists", mock_exists)
    monkeypatch.setattr("os.access", mock_access)

    result = distribution_files._get_file_content(path)
    assert result is None
