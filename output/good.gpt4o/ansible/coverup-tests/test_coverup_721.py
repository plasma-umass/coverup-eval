# file lib/ansible/config/manager.py:277-281
# lines [277, 279, 280]
# branches []

import pytest
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    # Create a new instance of ConfigManager for each test
    return ConfigManager()

def test_deprecated_initialization(config_manager):
    assert isinstance(config_manager.DEPRECATED, list)
    assert config_manager.DEPRECATED == []

def test_warnings_initialization(config_manager):
    assert isinstance(config_manager.WARNINGS, set)
    assert config_manager.WARNINGS == set()

def test_modify_deprecated(config_manager):
    config_manager.DEPRECATED.append('deprecated_item')
    assert 'deprecated_item' in config_manager.DEPRECATED

def test_modify_warnings(config_manager):
    config_manager.WARNINGS.add('warning_item')
    assert 'warning_item' in config_manager.WARNINGS

def test_cleanup_deprecated(config_manager):
    config_manager.DEPRECATED.append('deprecated_item')
    config_manager.DEPRECATED.remove('deprecated_item')
    assert 'deprecated_item' not in config_manager.DEPRECATED

def test_cleanup_warnings(config_manager):
    config_manager.WARNINGS.add('warning_item')
    config_manager.WARNINGS.remove('warning_item')
    assert 'warning_item' not in config_manager.WARNINGS

@pytest.fixture(autouse=True)
def cleanup():
    # Ensure DEPRECATED and WARNINGS are reset after each test
    yield
    ConfigManager.DEPRECATED.clear()
    ConfigManager.WARNINGS.clear()
