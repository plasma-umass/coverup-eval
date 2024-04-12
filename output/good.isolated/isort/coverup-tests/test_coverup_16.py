# file isort/exceptions.py:140-160
# lines [140, 141, 145, 146, 147, 149, 150, 151, 154, 155, 156, 160]
# branches []

import pytest
from isort.exceptions import UnsupportedSettings

def test_unsupported_settings_exception():
    unsupported_settings = {
        "unknown_option": {"value": True, "source": "config file"},
        "another_bad_option": {"value": 123, "source": "CLI"}
    }
    with pytest.raises(UnsupportedSettings) as exc_info:
        raise UnsupportedSettings(unsupported_settings)

    exception_message = str(exc_info.value)
    assert "isort was provided settings that it doesn't support:" in exception_message
    for setting, details in unsupported_settings.items():
        assert f"\t- {setting} = {details['value']}  (source: '{details['source']}')" in exception_message
    assert "https://pycqa.github.io/isort/docs/configuration/options/." in exception_message
    assert exc_info.value.unsupported_settings == unsupported_settings
