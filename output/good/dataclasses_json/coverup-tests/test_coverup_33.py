# file dataclasses_json/undefined.py:203-207
# lines [205, 206, 207]
# branches []

import pytest
from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin, CatchAll
from dataclasses_json.undefined import _CatchAllUndefinedParameters

@dataclass
class ExampleWithCatchAll(DataClassJsonMixin):
    name: str
    catch_all: CatchAll = field(default_factory=dict)

@pytest.fixture
def example_with_catch_all():
    return ExampleWithCatchAll(name="Test", catch_all={"extra": "value"})

def test_catch_all_undefined_parameters(example_with_catch_all, mocker):
    # Mock the _get_catch_all_field method to return the 'catch_all' field
    mocker.patch(
        'dataclasses_json.undefined._CatchAllUndefinedParameters._get_catch_all_field',
        return_value=ExampleWithCatchAll.__dataclass_fields__['catch_all']
    )

    # Call the handle_dump method and assert the result
    result = _CatchAllUndefinedParameters.handle_dump(example_with_catch_all)
    assert result == {"extra": "value"}
