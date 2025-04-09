# file: py_backwards/conf.py:12-14
# asked: {"lines": [12, 13, 14], "branches": [[13, 0], [13, 14]]}
# gained: {"lines": [12, 13, 14], "branches": [[13, 0], [13, 14]]}

import pytest
from argparse import Namespace
from py_backwards import conf

@pytest.fixture
def mock_settings(monkeypatch):
    class MockSettings:
        debug = False

    mock_settings = MockSettings()
    monkeypatch.setattr(conf, 'settings', mock_settings)
    return mock_settings

def test_init_settings_debug_true(mock_settings):
    args = Namespace(debug=True)
    conf.init_settings(args)
    assert mock_settings.debug is True

def test_init_settings_debug_false(mock_settings):
    args = Namespace(debug=False)
    conf.init_settings(args)
    assert mock_settings.debug is False
