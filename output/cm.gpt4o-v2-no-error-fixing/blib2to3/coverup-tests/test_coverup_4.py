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
    # Mock the pprint function and the print function
    with patch('builtins.print') as mock_print, patch('pprint.pprint') as mock_pprint:
        # Call the report method
        grammar.report()
        
        # Check that print and pprint were called with the expected arguments
        mock_print.assert_any_call('s2n')
        mock_pprint.assert_any_call(grammar.symbol2number)
        mock_print.assert_any_call('n2s')
        mock_pprint.assert_any_call(grammar.number2symbol)
        mock_print.assert_any_call('states')
        mock_pprint.assert_any_call(grammar.states)
        mock_print.assert_any_call('dfas')
        mock_pprint.assert_any_call(grammar.dfas)
        mock_print.assert_any_call('labels')
        mock_pprint.assert_any_call(grammar.labels)
        mock_print.assert_any_call('start', grammar.start)
