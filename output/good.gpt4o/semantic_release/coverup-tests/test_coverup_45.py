# file semantic_release/dist.py:12-17
# lines [13, 14, 15, 16, 17]
# branches []

import pytest
from unittest.mock import patch

# Assuming the function should_build is imported from semantic_release.dist
from semantic_release.dist import should_build

@pytest.fixture
def mock_config(mocker):
    config = {
        "upload_to_pypi": None,
        "upload_to_release": None,
        "build_command": None
    }
    mocker.patch('semantic_release.dist.config', config)
    return config

def test_should_build_with_build_command_false(mock_config):
    mock_config["build_command"] = "false"
    mock_config["upload_to_pypi"] = True
    assert not should_build()

def test_should_build_with_no_uploads(mock_config):
    mock_config["build_command"] = "build"
    mock_config["upload_to_pypi"] = False
    mock_config["upload_to_release"] = False
    assert not should_build()

def test_should_build_with_upload_pypi(mock_config):
    mock_config["build_command"] = "build"
    mock_config["upload_to_pypi"] = True
    assert should_build()

def test_should_build_with_upload_release(mock_config):
    mock_config["build_command"] = "build"
    mock_config["upload_to_release"] = True
    assert should_build()
