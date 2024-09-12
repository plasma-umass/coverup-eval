# file: semantic_release/dist.py:31-34
# asked: {"lines": [31, 32, 33, 34], "branches": []}
# gained: {"lines": [31, 32, 33, 34], "branches": []}

import pytest
from unittest.mock import patch
import logging

# Assuming the remove_dists function is imported from semantic_release.dist
from semantic_release.dist import remove_dists

@pytest.fixture
def mock_run(mocker):
    return mocker.patch('semantic_release.dist.run')

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('semantic_release.dist.logger')

def test_remove_dists(mock_run, mock_logger):
    path = "some/path"
    remove_dists(path)
    
    # Verify the command was constructed correctly
    expected_command = f"rm -rf {path}"
    mock_run.assert_called_once_with(expected_command)
    
    # Verify the logger was called with the correct debug message
    mock_logger.debug.assert_called_once_with(f"Running {expected_command}")
