# file: isort/exceptions.py:140-160
# asked: {"lines": [140, 141, 145, 146, 147, 149, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [140, 141, 145, 146, 147, 149, 150, 151, 154, 155, 156, 160], "branches": []}

import pytest
from isort.exceptions import UnsupportedSettings

def test_unsupported_settings_empty():
    unsupported_settings = {}
    exception = UnsupportedSettings(unsupported_settings)
    assert exception.unsupported_settings == unsupported_settings
    assert "isort was provided settings that it doesn't support" in str(exception)

def test_unsupported_settings_with_values():
    unsupported_settings = {
        "setting1": {"value": "value1", "source": "source1"},
        "setting2": {"value": "value2", "source": "source2"},
    }
    exception = UnsupportedSettings(unsupported_settings)
    assert exception.unsupported_settings == unsupported_settings
    assert "isort was provided settings that it doesn't support" in str(exception)
    assert "\t- setting1 = value1  (source: 'source1')" in str(exception)
    assert "\t- setting2 = value2  (source: 'source2')" in str(exception)

def test_format_option():
    formatted_option = UnsupportedSettings._format_option("name", "value", "source")
    assert formatted_option == "\t- name = value  (source: 'source')"
