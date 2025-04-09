# file: dataclasses_json/cfg.py:44-97
# asked: {"lines": [], "branches": [[84, 92]]}
# gained: {"lines": [], "branches": [[84, 92]]}

import pytest
from dataclasses_json.cfg import config
from dataclasses_json.undefined import Undefined, UndefinedParameterError

def test_config_with_valid_string_undefined():
    metadata = {}
    result = config(metadata, undefined='raise')
    assert result['dataclasses_json']['undefined'] == Undefined.RAISE

def test_config_with_invalid_string_undefined():
    metadata = {}
    with pytest.raises(UndefinedParameterError) as excinfo:
        config(metadata, undefined='invalid_action')
    assert "Invalid undefined parameter action" in str(excinfo.value)

def test_config_with_undefined_enum():
    metadata = {}
    result = config(metadata, undefined=Undefined.EXCLUDE)
    assert result['dataclasses_json']['undefined'] == Undefined.EXCLUDE
