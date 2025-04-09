# file: pytutils/log.py:134-139
# asked: {"lines": [134, 135, 136, 138, 139], "branches": [[135, 136], [135, 138]]}
# gained: {"lines": [134, 135, 136, 138, 139], "branches": [[135, 136], [135, 138]]}

import pytest
from unittest import mock
from pytutils.log import _ensure_configured, _CONFIGURED, configure

@pytest.fixture(autouse=True)
def reset_configured():
    _CONFIGURED.clear()
    yield
    _CONFIGURED.clear()

def test_ensure_configured_already_configured():
    _CONFIGURED.append(True)
    _ensure_configured()
    assert len(_CONFIGURED) == 1  # Should still be one item

def test_ensure_configured_not_configured():
    with mock.patch('pytutils.log.configure') as mock_configure:
        _ensure_configured()
        assert len(_CONFIGURED) == 1  # Should have one item now
        mock_configure.assert_called_once()
