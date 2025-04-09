# file: flutils/txtutils.py:223-227
# asked: {"lines": [223, 224, 225, 226, 227], "branches": [[225, 226], [225, 227]]}
# gained: {"lines": [223, 224, 225, 226, 227], "branches": [[225, 226], [225, 227]]}

import pytest
from flutils.txtutils import AnsiTextWrapper
from unittest.mock import patch

@pytest.fixture
def text_wrapper():
    return AnsiTextWrapper()

def test_initial_indent_len_no_indent(text_wrapper, monkeypatch):
    monkeypatch.setattr(text_wrapper, 'initial_indent', '')
    assert text_wrapper.initial_indent_len == 0

def test_initial_indent_len_with_indent(text_wrapper, monkeypatch):
    monkeypatch.setattr(text_wrapper, 'initial_indent', '  ')
    with patch('flutils.txtutils.len_without_ansi', return_value=2) as mock_len:
        assert text_wrapper.initial_indent_len == 2
        mock_len.assert_called_once_with('  ')
