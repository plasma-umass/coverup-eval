# file: semantic_release/dist.py:31-34
# asked: {"lines": [31, 32, 33, 34], "branches": []}
# gained: {"lines": [31, 32, 33, 34], "branches": []}

import pytest
from unittest.mock import patch, call
import logging
from semantic_release.dist import remove_dists

@pytest.fixture
def mock_run(mocker):
    return mocker.patch('semantic_release.dist.run')

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('semantic_release.dist.logger')

def test_remove_dists(mock_run, mock_logger):
    test_path = "test_path"
    
    remove_dists(test_path)
    
    mock_run.assert_called_once_with(f"rm -rf {test_path}")
    mock_logger.debug.assert_called_once_with(f"Running rm -rf {test_path}")
