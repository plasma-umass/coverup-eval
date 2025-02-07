# file: isort/exceptions.py:140-160
# asked: {"lines": [140, 141, 145, 146, 147, 149, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [140, 141, 145, 146, 147, 149, 150, 151, 154, 155, 156, 160], "branches": []}

import pytest
from isort.exceptions import UnsupportedSettings

def test_unsupported_settings_format_option():
    result = UnsupportedSettings._format_option("setting_name", "value", "source")
    assert result == "\t- setting_name = value  (source: 'source')"

def test_unsupported_settings_initialization():
    unsupported_settings = {
        "setting1": {"value": "value1", "source": "source1"},
        "setting2": {"value": "value2", "source": "source2"},
    }
    exception = UnsupportedSettings(unsupported_settings)
    
    expected_message = (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- setting1 = value1  (source: 'source1')\n"
        "\t- setting2 = value2  (source: 'source2')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )
    
    assert str(exception) == expected_message
    assert exception.unsupported_settings == unsupported_settings
