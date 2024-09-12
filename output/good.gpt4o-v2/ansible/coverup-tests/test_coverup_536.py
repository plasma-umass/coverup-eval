# file: lib/ansible/constants.py:33-40
# asked: {"lines": [33, 35, 36, 37, 38, 39, 40], "branches": []}
# gained: {"lines": [33, 35, 36, 37, 38, 39, 40], "branches": []}

import pytest
from unittest import mock
import sys

def test_deprecated_with_display(monkeypatch):
    from ansible.constants import _deprecated

    mock_display = mock.Mock()
    monkeypatch.setattr('ansible.utils.display.Display', mock_display)

    _deprecated("Test message", "2.0")

    mock_display().deprecated.assert_called_once_with("Test message", version="2.0")

def test_deprecated_without_display(monkeypatch):
    from ansible.constants import _deprecated

    monkeypatch.setattr('ansible.utils.display.Display', None)
    mock_stderr = mock.Mock()
    monkeypatch.setattr(sys, 'stderr', mock_stderr)

    _deprecated("Test message", "2.0")

    mock_stderr.write.assert_called_once_with(' [DEPRECATED] Test message, to be removed in 2.0\n')
