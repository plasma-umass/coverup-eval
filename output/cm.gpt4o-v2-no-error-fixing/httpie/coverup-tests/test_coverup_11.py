# file: httpie/config.py:20-55
# asked: {"lines": [20, 35, 36, 37, 40, 41, 43, 46, 47, 48, 51, 52, 53, 55], "branches": [[36, 37], [36, 40], [40, 41], [40, 43], [47, 48], [47, 51]]}
# gained: {"lines": [20, 35, 36, 37, 40, 41, 43, 46, 47, 48, 51, 52, 53, 55], "branches": [[36, 37], [36, 40], [40, 41], [40, 43], [47, 48], [47, 51]]}

import os
from pathlib import Path
import pytest
from httpie.config import get_default_config_dir
from httpie.compat import is_windows

ENV_HTTPIE_CONFIG_DIR = 'HTTPIE_CONFIG_DIR'
DEFAULT_WINDOWS_CONFIG_DIR = Path(os.path.expandvars('%APPDATA%')) / 'httpie'
DEFAULT_RELATIVE_LEGACY_CONFIG_DIR = Path('.httpie')
ENV_XDG_CONFIG_HOME = 'XDG_CONFIG_HOME'
DEFAULT_RELATIVE_XDG_CONFIG_HOME = Path('.config')
DEFAULT_CONFIG_DIRNAME = 'httpie'

def test_get_default_config_dir_env(monkeypatch):
    monkeypatch.setenv(ENV_HTTPIE_CONFIG_DIR, '/custom/config/dir')
    assert get_default_config_dir() == Path('/custom/config/dir')
    monkeypatch.delenv(ENV_HTTPIE_CONFIG_DIR)

def test_get_default_config_dir_windows(monkeypatch):
    monkeypatch.setattr('httpie.config.is_windows', True)
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    monkeypatch.setattr('httpie.config.is_windows', is_windows)

def test_get_default_config_dir_legacy(monkeypatch, tmp_path):
    legacy_dir = tmp_path / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir()
    monkeypatch.setattr(Path, 'home', lambda: tmp_path)
    assert get_default_config_dir() == legacy_dir

def test_get_default_config_dir_xdg(monkeypatch, tmp_path):
    xdg_dir = tmp_path / DEFAULT_RELATIVE_XDG_CONFIG_HOME
    monkeypatch.setenv(ENV_XDG_CONFIG_HOME, str(xdg_dir))
    assert get_default_config_dir() == xdg_dir / DEFAULT_CONFIG_DIRNAME
    monkeypatch.delenv(ENV_XDG_CONFIG_HOME)

def test_get_default_config_dir_default(monkeypatch, tmp_path):
    monkeypatch.setattr(Path, 'home', lambda: tmp_path)
    assert get_default_config_dir() == tmp_path / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME
