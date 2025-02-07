# file: py_backwards/conf.py:12-14
# asked: {"lines": [12, 13, 14], "branches": [[13, 0], [13, 14]]}
# gained: {"lines": [12, 13, 14], "branches": [[13, 0], [13, 14]]}

import pytest
from argparse import Namespace
from py_backwards.conf import init_settings, settings

def test_init_settings_debug_true(monkeypatch):
    # Arrange
    args = Namespace(debug=True)
    
    # Act
    init_settings(args)
    
    # Assert
    assert settings.debug is True
    
    # Cleanup
    monkeypatch.setattr(settings, 'debug', False)

def test_init_settings_debug_false(monkeypatch):
    # Arrange
    args = Namespace(debug=False)
    
    # Act
    init_settings(args)
    
    # Assert
    assert settings.debug is False
    
    # Cleanup
    monkeypatch.setattr(settings, 'debug', False)
