# file: isort/format.py:137-150
# asked: {"lines": [137, 138, 139, 140, 147, 148, 150], "branches": [[138, 139], [138, 150]]}
# gained: {"lines": [137, 138, 139, 140, 147, 148, 150], "branches": [[138, 139], [138, 150]]}

import pytest
import sys
from io import StringIO
from isort.format import create_terminal_printer, ColoramaPrinter, BasicPrinter

def test_create_terminal_printer_with_colorama_unavailable(monkeypatch):
    # Mock colorama_unavailable to be True
    monkeypatch.setattr('isort.format.colorama_unavailable', True)
    
    # Redirect stderr to capture the print output
    stderr = StringIO()
    monkeypatch.setattr(sys, 'stderr', stderr)
    
    with pytest.raises(SystemExit) as excinfo:
        create_terminal_printer(color=True)
    
    assert excinfo.value.code == 1
    assert "Sorry, but to use --color (color_output) the colorama python package is required." in stderr.getvalue()

def test_create_terminal_printer_with_color(monkeypatch):
    # Mock colorama_unavailable to be False
    monkeypatch.setattr('isort.format.colorama_unavailable', False)
    
    printer = create_terminal_printer(color=True)
    assert isinstance(printer, ColoramaPrinter)

def test_create_terminal_printer_without_color():
    printer = create_terminal_printer(color=False)
    assert isinstance(printer, BasicPrinter)
