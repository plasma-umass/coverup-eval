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

def test_schema_create_single_iteration(mocker):
    mock_callable = mocker.Mock(return_value={"key": "value"})
    schema = Schema(schema=mock_callable)
    result = schema.create(iterations=1)
    assert result == [{"key": "value"}]
    mock_callable.assert_called_once()

def test_schema_create_multiple_iterations(mocker):
    mock_callable = mocker.Mock(return_value={"key": "value"})
    schema = Schema(schema=mock_callable)
    iterations = 5
    result = schema.create(iterations=iterations)
    assert result == [{"key": "value"}] * iterations
    assert mock_callable.call_count == iterations
