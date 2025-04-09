# file: cookiecutter/prompt.py:81-96
# asked: {"lines": [81, 86, 87, 88, 90, 92, 94, 96], "branches": [[92, 94], [92, 96]]}
# gained: {"lines": [81, 86, 87, 88, 90, 92, 94, 96], "branches": [[92, 94], [92, 96]]}

import pytest
import click
import json
from collections import OrderedDict
from cookiecutter.prompt import process_json

def test_process_json_valid_dict():
    user_value = '{"key": "value"}'
    result = process_json(user_value)
    assert result == {"key": "value"}
    assert isinstance(result, OrderedDict)

def test_process_json_invalid_json():
    user_value = '{"key": "value"'
    with pytest.raises(click.UsageError, match='Unable to decode to JSON.'):
        process_json(user_value)

def test_process_json_not_a_dict():
    user_value = '["value1", "value2"]'
    with pytest.raises(click.UsageError, match='Requires JSON dict.'):
        process_json(user_value)
