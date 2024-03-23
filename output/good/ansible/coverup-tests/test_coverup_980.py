# file lib/ansible/plugins/filter/core.py:71-73
# lines [71, 73]
# branches []

import pytest
import json
from ansible.plugins.filter.core import to_nice_json

def test_to_nice_json():
    data = {"key3": "value3", "key2": "value2", "key1": "value1"}
    expected_output = '{\n    "key1": "value1",\n    "key2": "value2",\n    "key3": "value3"\n}'
    
    # Test with default parameters
    nice_json_output = to_nice_json(data)
    assert nice_json_output == expected_output

    # Test with non-default indent
    nice_json_output_indent = to_nice_json(data, indent=2)
    expected_output_indent = '{\n  "key1": "value1",\n  "key2": "value2",\n  "key3": "value3"\n}'
    assert nice_json_output_indent == expected_output_indent

    # Test with sort_keys as False
    # When sort_keys is False, the order of keys in the JSON string is not guaranteed,
    # so we should not compare the string directly. Instead, we can parse the JSON
    # and compare the resulting objects.
    nice_json_output_unsorted = to_nice_json(data, sort_keys=False)
    assert json.loads(nice_json_output_unsorted) == data

    # Test with additional args and kwargs
    # The ensure_ascii=False parameter should not affect the output string format,
    # so the expected output should be the same as when ensure_ascii is not specified.
    nice_json_output_extra = to_nice_json(data, indent=2, sort_keys=False, ensure_ascii=False)
    assert json.loads(nice_json_output_extra) == data
