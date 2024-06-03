# file semantic_release/dist.py:25-28
# lines [25, 26, 27, 28]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.dist import build_dists

@pytest.fixture
def mock_config(mocker):
    return mocker.patch('semantic_release.dist.config')

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('semantic_release.dist.logger')

@pytest.fixture
def mock_run(mocker):
    return mocker.patch('semantic_release.dist.run')

def test_build_dists(mock_config, mock_logger, mock_run):
    # Arrange
    mock_config.get.return_value = "echo 'Building distributions'"
    
    # Act
    build_dists()
    
    # Assert
    mock_config.get.assert_called_once_with("build_command")
    mock_logger.info.assert_called_once_with("Running echo 'Building distributions'")
    mock_run.assert_called_once_with("echo 'Building distributions'")
