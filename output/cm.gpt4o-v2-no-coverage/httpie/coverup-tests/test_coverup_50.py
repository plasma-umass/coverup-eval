# file: httpie/config.py:70-72
# asked: {"lines": [70, 71, 72], "branches": []}
# gained: {"lines": [70, 71, 72], "branches": []}

import pytest
from pathlib import Path
from httpie.config import BaseConfigDict

@pytest.fixture
def temp_path(tmp_path):
    return tmp_path / "config.json"

def test_base_config_dict_init(temp_path):
    config = BaseConfigDict(temp_path)
    assert config.path == temp_path

