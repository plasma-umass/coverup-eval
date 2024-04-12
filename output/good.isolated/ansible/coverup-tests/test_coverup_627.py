# file lib/ansible/config/manager.py:162-167
# lines [162, 164, 165, 167]
# branches ['164->165', '164->167']

import os
import pytest
from unittest.mock import patch
from ansible.config.manager import resolve_path

# Mocking unfrackpath to ensure it does not perform any actual file system operations
@pytest.fixture
def mock_unfrackpath(mocker):
    return mocker.patch('ansible.config.manager.unfrackpath', return_value='/mocked/path')

def test_resolve_path_with_cwd_token(mock_unfrackpath):
    # Setup
    original_cwd = os.getcwd()
    test_path = "{{CWD}}/test/path"
    expected_resolved_path = f"{original_cwd}/test/path"

    # Exercise
    resolved_path = resolve_path(test_path)

    # Verify
    assert resolved_path == '/mocked/path', "The resolved path should be mocked to '/mocked/path'"
    mock_unfrackpath.assert_called_once_with(expected_resolved_path, follow=False, basedir=None)

    # Cleanup is not necessary as we are mocking unfrackpath and not changing any state
