# file: lib/ansible/module_utils/facts/system/distribution.py:99-100
# asked: {"lines": [100], "branches": []}
# gained: {"lines": [100], "branches": []}

import pytest
from unittest.mock import patch

# Assuming the get_file_content function is imported from the appropriate module
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files():
    class MockModule:
        pass

    mock_module = MockModule()
    return DistributionFiles(mock_module)

def test_get_file_content(monkeypatch, distribution_files):
    test_path = "/etc/test_file"
    expected_content = "test content"

    def mock_get_file_content(path):
        assert path == test_path
        return expected_content

    monkeypatch.setattr('ansible.module_utils.facts.system.distribution.get_file_content', mock_get_file_content)

    result = distribution_files._get_file_content(test_path)
    assert result == expected_content
