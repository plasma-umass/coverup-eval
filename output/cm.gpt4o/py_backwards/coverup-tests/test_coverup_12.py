# file py_backwards/conf.py:12-14
# lines [12, 13, 14]
# branches ['13->exit', '13->14']

import pytest
from argparse import Namespace
from py_backwards import conf
from py_backwards.conf import settings

@pytest.fixture
def mock_settings(mocker):
    original_debug = settings.debug
    mocker.patch.object(settings, 'debug', original_debug)
    yield
    settings.debug = original_debug

def test_init_settings_debug_enabled(mock_settings):
    args = Namespace(debug=True)
    conf.init_settings(args)
    assert settings.debug is True

def test_init_settings_debug_disabled(mock_settings):
    args = Namespace(debug=False)
    conf.init_settings(args)
    assert settings.debug is False
