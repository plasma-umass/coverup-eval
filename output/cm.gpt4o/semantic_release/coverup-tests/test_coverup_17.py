# file semantic_release/dist.py:31-34
# lines [31, 32, 33, 34]
# branches []

import pytest
import os
from unittest.mock import patch
from semantic_release.dist import remove_dists

@pytest.fixture
def mock_run(mocker):
    return mocker.patch('semantic_release.dist.run')

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('semantic_release.dist.logger')

def test_remove_dists(mock_run, mock_logger):
    test_path = "test_path"
    
    # Ensure the directory exists before running the test
    os.makedirs(test_path, exist_ok=True)
    
    # Call the function
    remove_dists(test_path)
    
    # Assert that the run function was called with the correct command
    mock_run.assert_called_once_with(f"rm -rf {test_path}")
    
    # Assert that the logger debug was called with the correct message
    mock_logger.debug.assert_called_once_with(f"Running rm -rf {test_path}")
    
    # Clean up by removing the test directory if it still exists
    if os.path.exists(test_path):
        os.rmdir(test_path)
