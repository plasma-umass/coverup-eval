# file: pytutils/log.py:134-139
# asked: {"lines": [134, 135, 136, 138, 139], "branches": [[135, 136], [135, 138]]}
# gained: {"lines": [134, 135, 136, 138, 139], "branches": [[135, 136], [135, 138]]}

import pytest
from unittest import mock
from pytutils.log import _ensure_configured, _CONFIGURED, configure

def test_ensure_configured_already_configured():
    _CONFIGURED.clear()
    _CONFIGURED.append(True)
    with mock.patch('pytutils.log.configure') as mock_configure:
        _ensure_configured()
        mock_configure.assert_not_called()
    _CONFIGURED.clear()

def test_ensure_configured_not_configured():
    _CONFIGURED.clear()
    with mock.patch('pytutils.log.configure') as mock_configure:
        _ensure_configured()
        mock_configure.assert_called_once()
        assert _CONFIGURED == [True]
    _CONFIGURED.clear()
