# file dataclasses_json/cfg.py:44-97
# lines [75, 76]
# branches ['55->58', '70->75', '82->94']

import pytest
from dataclasses_json.cfg import config, UndefinedParameterError
from dataclasses_json.undefined import Undefined

def test_config_full_coverage():
    # Test the branch where `letter_case` is None and `field_name` is not None
    metadata = {}
    field_name = "test_field"
    result = config(metadata, field_name=field_name)
    assert result['dataclasses_json']['letter_case']('anything') == field_name

    # Test the branch where `undefined` is a string that is not an attribute of `Undefined`
    with pytest.raises(UndefinedParameterError):
        config(undefined="invalid_action")

    # Test the branch where `undefined` is a valid string attribute of `Undefined`
    metadata = {}
    result = config(metadata, undefined="INCLUDE")
    assert result['dataclasses_json']['undefined'] == Undefined.INCLUDE

    # Test the branch where `undefined` is already an `Undefined` enum
    metadata = {}
    result = config(metadata, undefined=Undefined.EXCLUDE)
    assert result['dataclasses_json']['undefined'] == Undefined.EXCLUDE
