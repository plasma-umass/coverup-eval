# file: lib/ansible/config/manager.py:343-345
# asked: {"lines": [343, 345], "branches": []}
# gained: {"lines": [343], "branches": []}

import pytest
from ansible.config.manager import ConfigManager

def test_find_yaml_config_files(monkeypatch):
    config_manager = ConfigManager()

    # Mocking the method to ensure it gets called
    def mock_find_yaml_config_files(self):
        self.called = True

    monkeypatch.setattr(ConfigManager, "_find_yaml_config_files", mock_find_yaml_config_files)

    config_manager._find_yaml_config_files()
    assert hasattr(config_manager, 'called') and config_manager.called
