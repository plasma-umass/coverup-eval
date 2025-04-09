# file: httpie/config.py:70-72
# asked: {"lines": [70, 71, 72], "branches": []}
# gained: {"lines": [70, 71, 72], "branches": []}

import pytest
from pathlib import Path
from httpie.config import BaseConfigDict

@pytest.fixture
def temp_path(tmp_path):
    return tmp_path / "config.json"

def test_base_config_dict_initialization(temp_path):
    config = BaseConfigDict(temp_path)
    assert config.path == temp_path
    assert isinstance(config, dict)

def test_base_config_dict_inherits_dict_methods(temp_path):
    config = BaseConfigDict(temp_path)
    config['key'] = 'value'
    assert config['key'] == 'value'
    assert 'key' in config
    del config['key']
    assert 'key' not in config
