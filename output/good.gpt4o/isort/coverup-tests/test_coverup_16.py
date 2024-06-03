# file isort/exceptions.py:140-160
# lines [140, 141, 145, 146, 147, 149, 150, 151, 154, 155, 156, 160]
# branches []

import pytest
from isort.exceptions import UnsupportedSettings

def test_unsupported_settings():
    unsupported_settings = {
        "setting1": {"value": "value1", "source": "config"},
        "setting2": {"value": "value2", "source": "CLI"},
    }
    
    exception = UnsupportedSettings(unsupported_settings)
    
    expected_message = (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- setting1 = value1  (source: 'config')\n"
        "\t- setting2 = value2  (source: 'CLI')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )
    
    assert str(exception) == expected_message
    assert exception.unsupported_settings == unsupported_settings
