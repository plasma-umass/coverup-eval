# file: dataclasses_json/cfg.py:21-26
# asked: {"lines": [21, 23, 24, 25, 26], "branches": []}
# gained: {"lines": [21, 23, 24, 25, 26], "branches": []}

import pytest
from dataclasses_json.cfg import _GlobalConfig

@pytest.fixture
def global_config():
    return _GlobalConfig()

def test_global_config_initialization(global_config):
    assert isinstance(global_config.encoders, dict)
    assert isinstance(global_config.decoders, dict)
    assert isinstance(global_config.mm_fields, dict)
    assert len(global_config.encoders) == 0
    assert len(global_config.decoders) == 0
    assert len(global_config.mm_fields) == 0
