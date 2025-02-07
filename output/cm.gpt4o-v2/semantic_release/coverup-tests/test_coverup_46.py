# file: semantic_release/dist.py:25-28
# asked: {"lines": [26, 27, 28], "branches": []}
# gained: {"lines": [26, 27, 28], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.dist import build_dists

@pytest.fixture
def mock_config():
    with patch('semantic_release.dist.config') as mock_config:
        yield mock_config

@pytest.fixture
def mock_logger():
    with patch('semantic_release.dist.logger') as mock_logger:
        yield mock_logger

@pytest.fixture
def mock_run():
    with patch('semantic_release.dist.run') as mock_run:
        yield mock_run

def test_build_dists(mock_config, mock_logger, mock_run):
    mock_config.get.return_value = 'echo "Building dists"'
    
    build_dists()
    
    mock_config.get.assert_called_once_with('build_command')
    mock_logger.info.assert_called_once_with('Running echo "Building dists"')
    mock_run.assert_called_once_with('echo "Building dists"')
