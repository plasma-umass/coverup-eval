# file semantic_release/settings.py:35-61
# lines [35, 36, 37, 39, 54, 55, 56, 57, 59, 61]
# branches ['55->56', '55->61', '56->57', '56->59']

import configparser
import os
import pytest
from semantic_release.settings import _config_from_ini

@pytest.fixture
def ini_file(tmp_path):
    ini_content = """
    [semantic_release]
    changelog_capitalize = true
    changelog_scope = true
    check_build_status = false
    commit_version_number = yes
    patch_without_tag = no
    major_on_zero = 1
    remove_dist = 0
    upload_to_pypi = True
    upload_to_release = False
    custom_option = some_value
    """
    ini_file_path = tmp_path / "test_config.ini"
    ini_file_path.write_text(ini_content)
    return str(ini_file_path)

def test_config_from_ini(ini_file):
    config = _config_from_ini([ini_file])
    
    assert config['changelog_capitalize'] is True
    assert config['changelog_scope'] is True
    assert config['check_build_status'] is False
    assert config['commit_version_number'] is True
    assert config['patch_without_tag'] is False
    assert config['major_on_zero'] is True
    assert config['remove_dist'] is False
    assert config['upload_to_pypi'] is True
    assert config['upload_to_release'] is False
    assert config['custom_option'] == 'some_value'
