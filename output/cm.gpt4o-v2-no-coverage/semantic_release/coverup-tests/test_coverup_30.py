# file: semantic_release/dist.py:12-17
# asked: {"lines": [12, 13, 14, 15, 16, 17], "branches": []}
# gained: {"lines": [12, 13, 14, 15, 16, 17], "branches": []}

import pytest
from unittest.mock import patch

# Mocking the config object from semantic_release.settings
@pytest.fixture
def mock_config():
    with patch('semantic_release.settings.config') as mock_config:
        yield mock_config

def test_should_build_with_build_command_false(mock_config):
    from semantic_release.dist import should_build

    mock_config.get.side_effect = lambda key: {
        "upload_to_pypi": True,
        "upload_to_release": False,
        "build_command": "false"
    }.get(key)

    assert not should_build()

def test_should_build_with_upload_to_pypi(mock_config):
    from semantic_release.dist import should_build

    mock_config.get.side_effect = lambda key: {
        "upload_to_pypi": True,
        "upload_to_release": False,
        "build_command": "build"
    }.get(key)

    assert should_build()

def test_should_build_with_upload_to_release(mock_config):
    from semantic_release.dist import should_build

    mock_config.get.side_effect = lambda key: {
        "upload_to_pypi": False,
        "upload_to_release": True,
        "build_command": "build"
    }.get(key)

    assert should_build()

def test_should_build_with_no_upload(mock_config):
    from semantic_release.dist import should_build

    mock_config.get.side_effect = lambda key: {
        "upload_to_pypi": False,
        "upload_to_release": False,
        "build_command": "build"
    }.get(key)

    assert not should_build()

def test_should_build_with_no_build_command(mock_config):
    from semantic_release.dist import should_build

    mock_config.get.side_effect = lambda key: {
        "upload_to_pypi": True,
        "upload_to_release": True,
        "build_command": None
    }.get(key)

    assert not should_build()
