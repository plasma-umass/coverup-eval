# file: semantic_release/dist.py:31-34
# asked: {"lines": [31, 32, 33, 34], "branches": []}
# gained: {"lines": [31, 32, 33, 34], "branches": []}

import pytest
from unittest.mock import patch
from semantic_release.dist import remove_dists

@patch('semantic_release.dist.run')
@patch('semantic_release.dist.logger')
def test_remove_dists(mock_logger, mock_run):
    path = 'dummy_path'
    remove_dists(path)
    
    mock_logger.debug.assert_called_once_with(f'Running rm -rf {path}')
    mock_run.assert_called_once_with(f'rm -rf {path}')
