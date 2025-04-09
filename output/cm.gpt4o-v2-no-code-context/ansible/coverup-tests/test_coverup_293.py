# file: lib/ansible/modules/apt_repository.py:196-209
# asked: {"lines": [196, 197, 198, 200, 201, 204, 205, 208, 209], "branches": [[204, 205], [204, 208], [208, 0], [208, 209]]}
# gained: {"lines": [196, 197, 198, 200, 201, 204, 205, 208, 209], "branches": [[204, 205], [208, 0], [208, 209]]}

import os
import glob
import pytest
from unittest import mock

# Assuming the SourcesList class is imported from the module
from ansible.modules.apt_repository import SourcesList

@pytest.fixture
def mock_module():
    return mock.Mock()

@pytest.fixture
def mock_apt_cfg_file(monkeypatch):
    def mock_apt_cfg_file(self, key):
        if key == 'Dir::Etc::sourcelist':
            return '/etc/apt/sources.list'
        return ''
    monkeypatch.setattr(SourcesList, '_apt_cfg_file', mock_apt_cfg_file)

@pytest.fixture
def mock_apt_cfg_dir(monkeypatch):
    def mock_apt_cfg_dir(self, key):
        if key == 'Dir::Etc::sourceparts':
            return '/etc/apt/sources.list.d'
        return ''
    monkeypatch.setattr(SourcesList, '_apt_cfg_dir', mock_apt_cfg_dir)

@pytest.fixture
def mock_isfile(monkeypatch):
    def mock_isfile(path):
        return path == '/etc/apt/sources.list'
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)

@pytest.fixture
def mock_glob(monkeypatch):
    def mock_iglob(pattern):
        return ['/etc/apt/sources.list.d/example.list']
    monkeypatch.setattr(glob, 'iglob', mock_iglob)

@pytest.fixture
def mock_load(monkeypatch):
    def mock_load(self, file):
        self.files[file] = 'content'
    monkeypatch.setattr(SourcesList, 'load', mock_load)

def test_sources_list_init(mock_module, mock_apt_cfg_file, mock_apt_cfg_dir, mock_isfile, mock_glob, mock_load):
    sources_list = SourcesList(mock_module)
    
    # Assertions to verify the postconditions
    assert sources_list.module == mock_module
    assert sources_list.files == {
        '/etc/apt/sources.list': 'content',
        '/etc/apt/sources.list.d/example.list': 'content'
    }
    assert sources_list.new_repos == set()
    assert sources_list.default_file == '/etc/apt/sources.list'
