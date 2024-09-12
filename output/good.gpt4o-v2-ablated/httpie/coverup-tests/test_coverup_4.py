# file: httpie/config.py:20-55
# asked: {"lines": [20, 35, 36, 37, 40, 41, 43, 46, 47, 48, 51, 52, 53, 55], "branches": [[36, 37], [36, 40], [40, 41], [40, 43], [47, 48], [47, 51]]}
# gained: {"lines": [20, 35, 36, 37, 40, 41, 43, 46, 47, 48, 51, 52, 53, 55], "branches": [[36, 37], [36, 40], [40, 41], [40, 43], [47, 48], [47, 51]]}

import os
import pytest
from pathlib import Path
from httpie.config import get_default_config_dir, ENV_HTTPIE_CONFIG_DIR, ENV_XDG_CONFIG_HOME, DEFAULT_WINDOWS_CONFIG_DIR, DEFAULT_RELATIVE_LEGACY_CONFIG_DIR, DEFAULT_RELATIVE_XDG_CONFIG_HOME, DEFAULT_CONFIG_DIRNAME

@pytest.fixture
def clear_env(monkeypatch):
    for key in [ENV_HTTPIE_CONFIG_DIR, ENV_XDG_CONFIG_HOME]:
        monkeypatch.delenv(key, raising=False)

def test_get_default_config_dir_env_set(monkeypatch, clear_env):
    monkeypatch.setenv(ENV_HTTPIE_CONFIG_DIR, '/custom/config/dir')
    assert get_default_config_dir() == Path('/custom/config/dir')

def test_get_default_config_dir_windows(monkeypatch, clear_env):
    monkeypatch.setattr('httpie.config.is_windows', True)
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

def test_get_default_config_dir_legacy_exists(monkeypatch, clear_env, tmp_path):
    legacy_dir = tmp_path / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(Path, 'home', lambda: tmp_path)
    assert get_default_config_dir() == legacy_dir

def test_get_default_config_dir_xdg_explicit(monkeypatch, clear_env, tmp_path):
    xdg_dir = tmp_path / 'xdg_config'
    monkeypatch.setenv(ENV_XDG_CONFIG_HOME, str(xdg_dir))
    assert get_default_config_dir() == xdg_dir / DEFAULT_CONFIG_DIRNAME

def test_get_default_config_dir_xdg_default(monkeypatch, clear_env, tmp_path):
    monkeypatch.setattr(Path, 'home', lambda: tmp_path)
    expected_dir = tmp_path / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME
    assert get_default_config_dir() == expected_dir
