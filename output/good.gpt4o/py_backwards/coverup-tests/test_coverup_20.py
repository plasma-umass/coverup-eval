# file py_backwards/conf.py:4-6
# lines [4, 5, 6]
# branches []

import pytest
from py_backwards.conf import Settings

def test_settings_initialization():
    settings = Settings()
    assert settings.debug is False

@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
