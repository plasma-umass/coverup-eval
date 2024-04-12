# file lib/ansible/playbook/included_file.py:47-51
# lines [47, 48, 49, 50, 51]
# branches ['48->49', '48->51']

import pytest
from ansible.playbook.included_file import IncludedFile

class MockIncludedFile(IncludedFile):
    def __init__(self):
        self._hosts = []

@pytest.fixture
def mock_included_file():
    return MockIncludedFile()

def test_add_host_success(mock_included_file):
    host = 'test_host'
    mock_included_file.add_host(host)
    assert host in mock_included_file._hosts

def test_add_host_failure(mock_included_file):
    host = 'test_host'
    mock_included_file._hosts.append(host)
    with pytest.raises(ValueError):
        mock_included_file.add_host(host)
