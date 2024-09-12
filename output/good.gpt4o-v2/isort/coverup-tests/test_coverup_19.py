# file: isort/format.py:137-150
# asked: {"lines": [137, 138, 139, 140, 147, 148, 150], "branches": [[138, 139], [138, 150]]}
# gained: {"lines": [137, 138, 139, 140, 147, 148, 150], "branches": [[138, 139], [138, 150]]}

import pytest
import sys
from io import StringIO
from unittest.mock import patch

# Assuming the following imports based on the provided code
from isort.format import create_terminal_printer, ColoramaPrinter, BasicPrinter

@pytest.fixture
def mock_colorama_unavailable(monkeypatch):
    monkeypatch.setattr('isort.format.colorama_unavailable', True)

def test_create_terminal_printer_colorama_unavailable(mock_colorama_unavailable):
    with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
        with pytest.raises(SystemExit) as excinfo:
            create_terminal_printer(color=True)
        assert excinfo.value.code == 1
        assert "Sorry, but to use --color (color_output) the colorama python package is required." in mock_stderr.getvalue()

def test_create_terminal_printer_colorama_available(monkeypatch):
    monkeypatch.setattr('isort.format.colorama_unavailable', False)
    printer = create_terminal_printer(color=True)
    assert isinstance(printer, ColoramaPrinter)

def test_create_terminal_printer_no_color(monkeypatch):
    monkeypatch.setattr('isort.format.colorama_unavailable', False)
    printer = create_terminal_printer(color=False)
    assert isinstance(printer, BasicPrinter)
