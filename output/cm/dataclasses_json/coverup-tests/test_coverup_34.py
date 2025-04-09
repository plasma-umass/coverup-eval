# file dataclasses_json/undefined.py:59-73
# lines [73]
# branches ['70->73']

import pytest
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined, UndefinedParameterError

@dataclass_json(undefined=Undefined.RAISE)
@dataclass
class MyDataClass:
    a: int
    b: str

def test_raise_undefined_parameters_handle_from_dict():
    valid_data = {'a': 1, 'b': 'test'}
    invalid_data = {'a': 1, 'b': 'test', 'c': 'unexpected'}

    # Test that valid data does not raise an error and returns the correct dictionary
    assert MyDataClass.from_dict(valid_data)

    # Test that invalid data raises UndefinedParameterError
    with pytest.raises(UndefinedParameterError) as exc_info:
        MyDataClass.from_dict(invalid_data)
    assert "Received undefined initialization arguments" in str(exc_info.value)
