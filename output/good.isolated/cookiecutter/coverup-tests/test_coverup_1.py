# file cookiecutter/prompt.py:81-96
# lines [81, 86, 87, 88, 90, 92, 94, 96]
# branches ['92->94', '92->96']

import json
import pytest
from click.testing import CliRunner
from cookiecutter.prompt import process_json
from click.exceptions import UsageError

def test_process_json_valid_dict(mocker):
    user_value = '{"name": "John", "age": 30}'
    expected_dict = {"name": "John", "age": 30}
    result = process_json(user_value)
    assert result == expected_dict

def test_process_json_invalid_json(mocker):
    user_value = 'not a json'
    with pytest.raises(UsageError) as excinfo:
        process_json(user_value)
    assert 'Unable to decode to JSON.' in str(excinfo.value)

def test_process_json_non_dict_json(mocker):
    user_value = '["not", "a", "dict"]'
    with pytest.raises(UsageError) as excinfo:
        process_json(user_value)
    assert 'Requires JSON dict.' in str(excinfo.value)
