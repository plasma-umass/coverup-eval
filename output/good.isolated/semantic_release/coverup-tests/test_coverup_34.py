# file semantic_release/dist.py:12-17
# lines [12, 13, 14, 15, 16, 17]
# branches []

import pytest
from semantic_release import dist
from semantic_release.settings import config

@pytest.fixture
def mock_config(mocker):
    return mocker.patch('semantic_release.dist.config')

def test_should_build_with_build_command_and_upload_to_pypi(mock_config):
    mock_config.get.side_effect = lambda key: {
        "upload_to_pypi": True,
        "upload_to_release": False,
        "build_command": "python setup.py sdist"
    }.get(key, None)

    assert dist.should_build() is True
    mock_config.get.assert_any_call("upload_to_pypi")
    mock_config.get.assert_any_call("upload_to_release")
    mock_config.get.assert_any_call("build_command")

def test_should_build_with_build_command_and_upload_to_release(mock_config):
    mock_config.get.side_effect = lambda key: {
        "upload_to_pypi": False,
        "upload_to_release": True,
        "build_command": "python setup.py sdist"
    }.get(key, None)

    assert dist.should_build() is True
    mock_config.get.assert_any_call("upload_to_pypi")
    mock_config.get.assert_any_call("upload_to_release")
    mock_config.get.assert_any_call("build_command")

def test_should_not_build_with_false_build_command(mock_config):
    mock_config.get.side_effect = lambda key: {
        "upload_to_pypi": True,
        "upload_to_release": True,
        "build_command": "false"
    }.get(key, None)

    assert dist.should_build() is False
    mock_config.get.assert_any_call("upload_to_pypi")
    mock_config.get.assert_any_call("upload_to_release")
    mock_config.get.assert_any_call("build_command")

def test_should_not_build_with_no_build_command(mock_config):
    mock_config.get.side_effect = lambda key: {
        "upload_to_pypi": True,
        "upload_to_release": True,
        "build_command": None
    }.get(key, None)

    assert dist.should_build() is False
    mock_config.get.assert_any_call("upload_to_pypi")
    mock_config.get.assert_any_call("upload_to_release")
    mock_config.get.assert_any_call("build_command")
