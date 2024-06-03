# file semantic_release/settings.py:35-61
# lines [35, 36, 37, 39, 54, 55, 56, 57, 59, 61]
# branches ['55->56', '55->61', '56->57', '56->59']

import pytest
import configparser
from unittest import mock

# Assuming the function _config_from_ini is imported from semantic_release.settings
from semantic_release.settings import _config_from_ini

def test_config_from_ini(mocker):
    # Create a mock for the configparser.ConfigParser
    mock_parser = mocker.patch('configparser.ConfigParser', autospec=True)
    mock_instance = mock_parser.return_value

    # Mock the read method to simulate reading from a file
    mock_instance.read.return_value = None

    # Mock the getboolean method to return the correct boolean values
    mock_instance.getboolean.side_effect = lambda section, key: {
        "changelog_capitalize": True,
        "changelog_scope": False,
        "check_build_status": True,
        "commit_version_number": False,
        "patch_without_tag": True,
        "major_on_zero": False,
        "remove_dist": True,
        "upload_to_pypi": False,
        "upload_to_release": True
    }[key]

    # Mock the get method to return the correct string values
    mock_instance.get.side_effect = lambda section, key: {
        "some_other_key": "some_value"
    }[key]

    # Mock the items method to return a list of tuples
    mock_instance.items.return_value = [
        ("changelog_capitalize", "true"),
        ("changelog_scope", "false"),
        ("check_build_status", "true"),
        ("commit_version_number", "false"),
        ("patch_without_tag", "true"),
        ("major_on_zero", "false"),
        ("remove_dist", "true"),
        ("upload_to_pypi", "false"),
        ("upload_to_release", "true"),
        ("some_other_key", "some_value")
    ]

    # Call the function with a dummy path
    config = _config_from_ini(["dummy_path.ini"])

    # Assertions to verify the correct behavior
    assert config["changelog_capitalize"] is True
    assert config["changelog_scope"] is False
    assert config["check_build_status"] is True
    assert config["commit_version_number"] is False
    assert config["patch_without_tag"] is True
    assert config["major_on_zero"] is False
    assert config["remove_dist"] is True
    assert config["upload_to_pypi"] is False
    assert config["upload_to_release"] is True
    assert config["some_other_key"] == "some_value"

    # Ensure the read method was called with the correct path
    mock_instance.read.assert_called_once_with(["dummy_path.ini"])

    # Ensure the items method was called with the correct section
    mock_instance.items.assert_called_once_with("semantic_release")
