# file mimesis/schema.py:118-140
# lines [118, 119, 121, 126, 127, 129, 131, 140]
# branches ['126->127', '126->129']

import pytest
from mimesis.schema import Schema
from mimesis.exceptions import UndefinedSchema

def test_schema_initialization_with_non_callable():
    with pytest.raises(UndefinedSchema):
        Schema(schema="not_callable")

def test_schema_initialization_with_callable(mocker):
    mock_callable = mocker.Mock()
    schema = Schema(schema=mock_callable)
    assert schema.schema == mock_callable

def test_schema_create_with_iterations(mocker):
    mock_callable = mocker.Mock(return_value={'key': 'value'})
    schema = Schema(schema=mock_callable)
    iterations = 5
    result = schema.create(iterations=iterations)
    assert len(result) == iterations
    assert all(item == {'key': 'value'} for item in result)
    assert mock_callable.call_count == iterations
