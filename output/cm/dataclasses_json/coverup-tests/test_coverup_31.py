# file dataclasses_json/undefined.py:209-241
# lines [223]
# branches ['221->223']

import pytest
from dataclasses import dataclass, field
from typing import Any
from dataclasses_json.undefined import Undefined, _CatchAllUndefinedParameters
from dataclasses_json import dataclass_json

@pytest.fixture
def cleanup():
    yield
    # No cleanup needed for this test case

def test_catch_all_undefined_parameters(cleanup, mocker):
    @dataclass_json(undefined=Undefined.INCLUDE)
    @dataclass
    class TestClass:
        a: int
        b: int
        c: Any = field(default_factory=dict)

    mock_field = mocker.Mock()
    mock_field.name = 'c'
    mocker.patch.object(
        _CatchAllUndefinedParameters, '_get_catch_all_field',
        return_value=mock_field
    )

    TestClass.__init__ = _CatchAllUndefinedParameters.create_init(TestClass)

    # Call the modified __init__ with an extra undefined parameter
    instance = TestClass(1, 2, d=4)

    # Assert that the undefined parameter is included in the 'c' field
    assert instance.c == {'d': 4}
    assert instance.a == 1
    assert instance.b == 2
