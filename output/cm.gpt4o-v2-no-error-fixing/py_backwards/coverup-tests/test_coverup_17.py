# file: py_backwards/conf.py:12-14
# asked: {"lines": [12, 13, 14], "branches": [[13, 0], [13, 14]]}
# gained: {"lines": [12, 13, 14], "branches": [[13, 0], [13, 14]]}

import pytest
from argparse import Namespace
from py_backwards.conf import init_settings, settings

@pytest.fixture
def reset_settings():
    original_debug = settings.debug
    yield
    settings.debug = original_debug

def test_init_settings_debug_true(reset_settings):
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

def test_init_settings_debug_false(reset_settings):
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug is False
