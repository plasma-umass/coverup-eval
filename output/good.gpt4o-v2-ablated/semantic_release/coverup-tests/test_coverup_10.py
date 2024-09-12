# file: semantic_release/dist.py:20-22
# asked: {"lines": [20, 21, 22], "branches": []}
# gained: {"lines": [20, 21, 22], "branches": []}

import pytest
from unittest.mock import patch

# Assuming the config and should_build are imported from the module
from semantic_release.dist import should_remove_dist

@pytest.fixture
def mock_config():
    with patch('semantic_release.dist.config') as mock_config:
        yield mock_config

@pytest.fixture
def mock_should_build():
    with patch('semantic_release.dist.should_build') as mock_should_build:
        yield mock_should_build

def test_should_remove_dist_true(mock_config, mock_should_build):
    mock_config.get.return_value = True
    mock_should_build.return_value = True

    assert should_remove_dist() is True

def test_should_remove_dist_false_no_remove_dist(mock_config, mock_should_build):
    mock_config.get.return_value = False
    mock_should_build.return_value = True

    assert should_remove_dist() is False

def test_should_remove_dist_false_no_build(mock_config, mock_should_build):
    mock_config.get.return_value = True
    mock_should_build.return_value = False

    assert should_remove_dist() is False

def test_should_remove_dist_false_no_remove_dist_no_build(mock_config, mock_should_build):
    mock_config.get.return_value = False
    mock_should_build.return_value = False

    assert should_remove_dist() is False
