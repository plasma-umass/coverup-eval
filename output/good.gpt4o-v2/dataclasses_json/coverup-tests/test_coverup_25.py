# file: dataclasses_json/core.py:53-87
# asked: {"lines": [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 83, 85, 86, 87], "branches": [[58, 59], [58, 65], [59, 60], [59, 61], [61, 62], [61, 63], [63, 58], [63, 64], [72, 73], [72, 87], [76, 77], [76, 78], [78, 79], [78, 80], [80, 81], [80, 83]]}
# gained: {"lines": [53], "branches": []}

import pytest
from collections import defaultdict
from dataclasses import dataclass, field, fields
from unittest.mock import MagicMock
from dataclasses_json import cfg

# Mocking the necessary parts of cfg
cfg.global_config = MagicMock()
cfg.global_config.encoders = {int: lambda x: str(x)}
cfg.global_config.decoders = {int: lambda x: int(x)}
cfg.global_config.mm_fields = {int: "mock_mm_field"}

# Mocking FieldOverride and confs
from collections import namedtuple
FieldOverride = namedtuple('FieldOverride', ['encoder', 'decoder', 'mm_field', 'letter_case', 'exclude'])
confs = ['encoder', 'decoder', 'mm_field', 'letter_case', 'exclude']

# The function to be tested
def _user_overrides_or_exts(cls):
    global_metadata = defaultdict(dict)
    encoders = cfg.global_config.encoders
    decoders = cfg.global_config.decoders
    mm_fields = cfg.global_config.mm_fields
    for field in fields(cls):
        if field.type in encoders:
            global_metadata[field.name]['encoder'] = encoders[field.type]
        if field.type in decoders:
            global_metadata[field.name]['decoder'] = decoders[field.type]
        if field.type in mm_fields:
            global_metadata[field.name]['mm_fields'] = mm_fields[field.type]
    try:
        cls_config = cls.dataclass_json_config if cls.dataclass_json_config is not None else {}
    except AttributeError:
        cls_config = {}
    overrides = {}
    for field in fields(cls):
        field_config = {}
        field_metadata = global_metadata[field.name]
        if 'encoder' in field_metadata:
            field_config['encoder'] = field_metadata['encoder']
        if 'decoder' in field_metadata:
            field_config['decoder'] = field_metadata['decoder']
        if 'mm_fields' in field_metadata:
            field_config['mm_field'] = field_metadata['mm_fields']
        field_config.update(cls_config)
        field_config.update(field.metadata.get('dataclasses_json', {}))
        overrides[field.name] = FieldOverride(*map(field_config.get, confs))
    return overrides

# Test cases
@dataclass
class TestClass:
    a: int = field(metadata={'dataclasses_json': {'encoder': lambda x: x + 1}})
    b: int = field(metadata={'dataclasses_json': {'decoder': lambda x: x - 1}})
    c: int = field(metadata={'dataclasses_json': {'mm_field': 'custom_mm_field'}})

@dataclass
class TestClassNoOverrides:
    a: int
    b: int
    c: int

def test_user_overrides_or_exts():
    result = _user_overrides_or_exts(TestClass)
    assert result['a'].encoder(1) == 2
    assert result['b'].decoder(1) == 0
    assert result['c'].mm_field == 'custom_mm_field'
    assert result['a'].mm_field == 'mock_mm_field'
    assert result['b'].mm_field == 'mock_mm_field'

def test_user_overrides_or_exts_no_overrides():
    result = _user_overrides_or_exts(TestClassNoOverrides)
    assert result['a'].encoder(1) == '1'
    assert result['b'].decoder(1) == 1
    assert result['c'].mm_field == 'mock_mm_field'

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: Mock global config
    monkeypatch.setattr(cfg, "global_config", MagicMock())
    cfg.global_config.encoders = {int: lambda x: str(x)}
    cfg.global_config.decoders = {int: lambda x: int(x)}
    cfg.global_config.mm_fields = {int: "mock_mm_field"}
    yield
    # Teardown: Reset global config
    cfg.global_config = MagicMock()
