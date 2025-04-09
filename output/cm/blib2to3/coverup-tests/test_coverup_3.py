# file src/blib2to3/pgen2/grammar.py:149-163
# lines [149, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163]
# branches []

import pytest
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def mock_print(mocker):
    return mocker.patch('builtins.print')

@pytest.fixture
def mock_pprint(mocker):
    return mocker.patch('pprint.pprint')

@pytest.fixture
def example_grammar():
    grammar = Grammar()
    grammar.symbol2number = {'symbol': 1}
    grammar.number2symbol = {1: 'symbol'}
    grammar.states = {'state': 'value'}
    grammar.dfas = {'dfa': 'value'}
    grammar.labels = [(0, 'label')]
    grammar.start = 0
    return grammar

def test_grammar_report(mock_print, mock_pprint, example_grammar):
    example_grammar.report()
    mock_print.assert_any_call("s2n")
    mock_print.assert_any_call("n2s")
    mock_print.assert_any_call("states")
    mock_print.assert_any_call("dfas")
    mock_print.assert_any_call("labels")
    mock_print.assert_any_call("start", example_grammar.start)
    mock_pprint.assert_any_call(example_grammar.symbol2number)
    mock_pprint.assert_any_call(example_grammar.number2symbol)
    mock_pprint.assert_any_call(example_grammar.states)
    mock_pprint.assert_any_call(example_grammar.dfas)
    mock_pprint.assert_any_call(example_grammar.labels)
