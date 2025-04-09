# file: lib/ansible/config/manager.py:343-345
# asked: {"lines": [345], "branches": []}
# gained: {"lines": [345], "branches": []}

import pytest
from ansible.config.manager import ConfigManager

def test_find_yaml_config_files():
    config_manager = ConfigManager()
    assert config_manager._find_yaml_config_files() is None
