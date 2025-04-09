# file: pytutils/log.py:134-139
# asked: {"lines": [134, 135, 136, 138, 139], "branches": [[135, 136], [135, 138]]}
# gained: {"lines": [134, 135, 136, 138, 139], "branches": [[135, 136], [135, 138]]}

import pytest
from unittest import mock
from pytutils.log import _ensure_configured, _CONFIGURED, configure

def test_ensure_configured_already_configured():
    _CONFIGURED.append(True)
    _ensure_configured()
    assert len(_CONFIGURED) == 1
    _CONFIGURED.clear()

def test_ensure_configured_not_configured(monkeypatch):
    _CONFIGURED.clear()
    
    mock_configure = mock.Mock()
    monkeypatch.setattr('pytutils.log.configure', mock_configure)
    
    _ensure_configured()
    
    assert len(_CONFIGURED) == 1
    assert _CONFIGURED[0] is True
    mock_configure.assert_called_once()
    _CONFIGURED.clear()
