# file: semantic_release/settings.py:35-61
# asked: {"lines": [35, 36, 37, 39, 54, 55, 56, 57, 59, 61], "branches": [[55, 56], [55, 61], [56, 57], [56, 59]]}
# gained: {"lines": [35, 36, 37, 39, 54, 55, 56, 57, 59, 61], "branches": [[55, 56], [55, 61], [56, 57], [56, 59]]}

import pytest
import configparser
from semantic_release.settings import _config_from_ini

@pytest.fixture
def ini_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test.ini"
    p.write_text(
        "[semantic_release]\n"
        "changelog_capitalize = true\n"
        "changelog_scope = false\n"
        "check_build_status = true\n"
        "commit_version_number = false\n"
        "patch_without_tag = true\n"
        "major_on_zero = false\n"
        "remove_dist = true\n"
        "upload_to_pypi = false\n"
        "upload_to_release = true\n"
        "some_other_key = some_value\n"
    )
    return p

def test_config_from_ini(ini_file):
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
    assert config["some_other_key"] == "some_value"
