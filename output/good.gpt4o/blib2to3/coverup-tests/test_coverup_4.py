# file src/blib2to3/pgen2/grammar.py:149-163
# lines [149, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def mock_grammar():
    grammar = Grammar()
    grammar.symbol2number = {'symbol1': 1, 'symbol2': 2}
    grammar.number2symbol = {1: 'symbol1', 2: 'symbol2'}
    grammar.states = {'state1': 'some_state'}
    grammar.dfas = {'dfa1': 'some_dfa'}
    grammar.labels = ['label1', 'label2']
    grammar.start = 'start_symbol'
    return grammar

def test_report(mock_grammar):
    with patch('builtins.print') as mock_print, patch('pprint.pprint') as mock_pprint:
        mock_grammar.report()
        
        mock_print.assert_any_call("s2n")
        mock_pprint.assert_any_call(mock_grammar.symbol2number)
        mock_print.assert_any_call("n2s")
        mock_pprint.assert_any_call(mock_grammar.number2symbol)
        mock_print.assert_any_call("states")
        mock_pprint.assert_any_call(mock_grammar.states)
        mock_print.assert_any_call("dfas")
        mock_pprint.assert_any_call(mock_grammar.dfas)
        mock_print.assert_any_call("labels")
        mock_pprint.assert_any_call(mock_grammar.labels)
        mock_print.assert_any_call("start", mock_grammar.start)
