# file: semantic_release/dist.py:25-28
# asked: {"lines": [25, 26, 27, 28], "branches": []}
# gained: {"lines": [25, 26, 27, 28], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
import logging

# Assuming the build_dists function is part of a module named semantic_release.dist
from semantic_release.dist import build_dists

@pytest.fixture
def mock_config(monkeypatch):
    mock_config = MagicMock()
    monkeypatch.setattr('semantic_release.dist.config', mock_config)
    return mock_config

@pytest.fixture
def mock_run(monkeypatch):
    mock_run = MagicMock()
    monkeypatch.setattr('semantic_release.dist.run', mock_run)
    return mock_run

@pytest.fixture
def mock_logger(monkeypatch):
    mock_logger = MagicMock()
    monkeypatch.setattr('semantic_release.dist.logger', mock_logger)
    return mock_logger

def test_build_dists(mock_config, mock_run, mock_logger):
    # Setup
    mock_config.get.return_value = "echo 'Building distributions'"
    
    # Execute
    build_dists()
    
    # Verify
    mock_config.get.assert_called_once_with("build_command")
    mock_logger.info.assert_called_once_with("Running echo 'Building distributions'")
    mock_run.assert_called_once_with("echo 'Building distributions'")
