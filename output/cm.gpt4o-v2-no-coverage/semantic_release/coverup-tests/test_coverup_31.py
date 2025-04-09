# file: semantic_release/settings.py:20-32
# asked: {"lines": [20, 21, 22, 23, 24, 26, 28, 29, 32], "branches": []}
# gained: {"lines": [20, 21, 22, 23, 24, 26, 28, 29, 32], "branches": []}

import os
import pytest
from unittest.mock import patch, mock_open
from collections import UserDict
from semantic_release.settings import _config, _config_from_ini, _config_from_pyproject

@pytest.fixture
def mock_getcwd(monkeypatch):
    monkeypatch.setattr(os, 'getcwd', lambda: '/mocked/path')

@pytest.fixture
def mock_isfile(monkeypatch):
    monkeypatch.setattr(os.path, 'isfile', lambda path: True)

@pytest.fixture
def mock_open_file(monkeypatch):
    mocked_open = mock_open(read_data='''
    [tool.semantic_release]
    changelog_capitalize = true
    changelog_scope = "scope"
    check_build_status = false
    commit_version_number = true
    patch_without_tag = false
    major_on_zero = true
    remove_dist = false
    upload_to_pypi = true
    upload_to_release = false
    ''')
    monkeypatch.setattr('builtins.open', mocked_open)

@pytest.fixture
def mock_configparser(monkeypatch):
    def mock_read(paths):
        return None

    def mock_items(section):
        return [
            ('changelog_capitalize', 'true'),
            ('changelog_scope', 'scope'),
            ('check_build_status', 'false'),
            ('commit_version_number', 'true'),
            ('patch_without_tag', 'false'),
            ('major_on_zero', 'true'),
            ('remove_dist', 'false'),
            ('upload_to_pypi', 'true'),
            ('upload_to_release', 'false')
        ]

    monkeypatch.setattr('configparser.ConfigParser.read', mock_read)
    monkeypatch.setattr('configparser.ConfigParser.items', mock_items)

def test_config(mock_getcwd, mock_isfile, mock_open_file, mock_configparser):
    with patch('semantic_release.settings._config_from_ini') as mock_ini, \
         patch('semantic_release.settings._config_from_pyproject') as mock_toml:
        
        mock_ini.return_value = {
            'changelog_capitalize': True,
            'changelog_scope': 'scope',
            'check_build_status': False,
            'commit_version_number': True,
            'patch_without_tag': False,
            'major_on_zero': True,
            'remove_dist': False,
            'upload_to_pypi': True,
            'upload_to_release': False
        }
        
        mock_toml.return_value = {
            'changelog_capitalize': True,
            'changelog_scope': 'scope',
            'check_build_status': False,
            'commit_version_number': True,
            'patch_without_tag': False,
            'major_on_zero': True,
            'remove_dist': False,
            'upload_to_pypi': True,
            'upload_to_release': False
        }
        
        config = _config()
        
        assert isinstance(config, UserDict)
        assert config['changelog_capitalize'] == True
        assert config['changelog_scope'] == 'scope'
        assert config['check_build_status'] == False
        assert config['commit_version_number'] == True
        assert config['patch_without_tag'] == False
        assert config['major_on_zero'] == True
        assert config['remove_dist'] == False
        assert config['upload_to_pypi'] == True
        assert config['upload_to_release'] == False
