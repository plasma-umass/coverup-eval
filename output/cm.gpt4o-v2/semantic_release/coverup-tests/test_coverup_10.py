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
    p.write_text("""
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
some_other_key = some_value
""")
    return str(p)

def test_config_from_ini(ini_file):
    config = _config_from_ini([ini_file])
    assert config == {
        "changelog_capitalize": True,
        "changelog_scope": False,
        "check_build_status": True,
        "commit_version_number": False,
        "patch_without_tag": True,
        "major_on_zero": False,
        "remove_dist": True,
        "upload_to_pypi": False,
        "upload_to_release": True,
        "some_other_key": "some_value"
    }
