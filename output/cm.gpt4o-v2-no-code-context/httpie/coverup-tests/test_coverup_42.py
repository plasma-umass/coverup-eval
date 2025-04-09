# file: httpie/config.py:70-72
# asked: {"lines": [70, 71, 72], "branches": []}
# gained: {"lines": [70, 71, 72], "branches": []}

import pytest
from pathlib import Path
from httpie.config import BaseConfigDict

def test_base_config_dict_initialization():
    test_path = Path('/tmp/test_config.json')
    config_dict = BaseConfigDict(test_path)
    
    assert isinstance(config_dict, BaseConfigDict)
    assert config_dict.path == test_path

@pytest.fixture
def temp_path(tmp_path):
    return tmp_path / "test_config.json"

def test_base_config_dict_with_temp_path(temp_path):
    config_dict = BaseConfigDict(temp_path)
    
    assert isinstance(config_dict, BaseConfigDict)
    assert config_dict.path == temp_path
