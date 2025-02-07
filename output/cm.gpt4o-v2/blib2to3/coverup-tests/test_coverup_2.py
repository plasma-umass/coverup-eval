# file: src/blib2to3/pgen2/grammar.py:149-163
# asked: {"lines": [149, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163], "branches": []}
# gained: {"lines": [149, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163], "branches": []}

import pytest
from blib2to3.pgen2.grammar import Grammar
from unittest.mock import patch
from io import StringIO
import sys

@pytest.fixture
def grammar():
    return Grammar()

def test_report(grammar):
    # Capture the output of the report method
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        grammar.report()
        output = mock_stdout.getvalue()

    # Check that all sections are printed
    assert "s2n" in output
    assert "n2s" in output
    assert "states" in output
    assert "dfas" in output
    assert "labels" in output
    assert "start" in output

    # Check that the printed values match the grammar's attributes
    assert str(grammar.symbol2number) in output
    assert str(grammar.number2symbol) in output
    assert str(grammar.states) in output
    assert str(grammar.dfas) in output
    assert str(grammar.labels) in output
    assert str(grammar.start) in output
