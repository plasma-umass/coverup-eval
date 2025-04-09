# file: src/blib2to3/pgen2/grammar.py:149-163
# asked: {"lines": [151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163], "branches": []}
# gained: {"lines": [151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163], "branches": []}

import pytest
from blib2to3.pgen2.grammar import Grammar
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_pprint():
    with patch('pprint.pprint') as mock_pprint:
        yield mock_pprint

def test_grammar_report(mock_pprint):
    grammar = Grammar()
    grammar.symbol2number = {'a': 1, 'b': 2}
    grammar.number2symbol = {1: 'a', 2: 'b'}
    grammar.states = {'state1': 'value1'}
    grammar.dfas = {'dfa1': 'value1'}
    grammar.labels = ['label1', 'label2']
    grammar.start = 'start_value'

    with patch('builtins.print') as mock_print:
        grammar.report()

        mock_print.assert_any_call("s2n")
        mock_pprint.assert_any_call(grammar.symbol2number)
        mock_print.assert_any_call("n2s")
        mock_pprint.assert_any_call(grammar.number2symbol)
        mock_print.assert_any_call("states")
        mock_pprint.assert_any_call(grammar.states)
        mock_print.assert_any_call("dfas")
        mock_pprint.assert_any_call(grammar.dfas)
        mock_print.assert_any_call("labels")
        mock_pprint.assert_any_call(grammar.labels)
        mock_print.assert_any_call("start", grammar.start)
