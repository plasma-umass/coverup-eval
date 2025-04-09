# file: semantic_release/settings.py:35-61
# asked: {"lines": [35, 36, 37, 39, 54, 55, 56, 57, 59, 61], "branches": [[55, 56], [55, 61], [56, 57], [56, 59]]}
# gained: {"lines": [35, 36, 37, 39, 54, 55, 56, 57, 59, 61], "branches": [[55, 56], [55, 61], [56, 57], [56, 59]]}

import pytest
import configparser
from semantic_release.settings import _config_from_ini

def test_config_from_ini_all_flags(monkeypatch, tmp_path):
    ini_content = """
    [semantic_release]
    changelog_capitalize = true
    changelog_scope = false
    check_build_status = true
    commit_version_number = false
    patch_without_tag = true
    major_on_zero = false
    remove_dist = true
    upload_to_pypi = false
    upload_to_release = true
    """

    ini_file = tmp_path / "test.ini"
    ini_file.write_text(ini_content)

    config = _config_from_ini([str(ini_file)])

    assert config["changelog_capitalize"] is True
    assert config["changelog_scope"] is False
    assert config["check_build_status"] is True
    assert config["commit_version_number"] is False
    assert config["patch_without_tag"] is True
    assert config["major_on_zero"] is False
    assert config["remove_dist"] is True
    assert config["upload_to_pypi"] is False
    assert config["upload_to_release"] is True

def test_config_from_ini_mixed_flags_and_values(monkeypatch, tmp_path):
    ini_content = """
    [semantic_release]
    changelog_capitalize = true
    some_other_key = some_value
    """

    ini_file = tmp_path / "test.ini"
    ini_file.write_text(ini_content)

    config = _config_from_ini([str(ini_file)])

    assert config["changelog_capitalize"] is True
    assert config["some_other_key"] == "some_value"

def test_config_from_ini_no_flags(monkeypatch, tmp_path):
    ini_content = """
    [semantic_release]
    some_other_key = some_value
    another_key = another_value
    """

    ini_file = tmp_path / "test.ini"
    ini_file.write_text(ini_content)

    config = _config_from_ini([str(ini_file)])

    assert config["some_other_key"] == "some_value"
    assert config["another_key"] == "another_value"
