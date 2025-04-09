# file dataclasses_json/cfg.py:21-26
# lines [21, 23, 24, 25, 26]
# branches []

import pytest
from dataclasses_json.cfg import _GlobalConfig

def test_global_config_initialization():
    config = _GlobalConfig()
    
    assert isinstance(config.encoders, dict)
    assert isinstance(config.decoders, dict)
    assert isinstance(config.mm_fields, dict)
    
    assert len(config.encoders) == 0
    assert len(config.decoders) == 0
    assert len(config.mm_fields) == 0
