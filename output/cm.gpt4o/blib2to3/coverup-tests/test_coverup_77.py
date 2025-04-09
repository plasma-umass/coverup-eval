# file src/blib2to3/pgen2/grammar.py:31-80
# lines [31, 32]
# branches []

import pytest
import pickle
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def grammar():
    return Grammar()

def test_grammar_load_and_dump(tmp_path, grammar):
    # Create a temporary file path
    temp_file = tmp_path / "grammar.pickle"

    # Set up some dummy data in the grammar object
    grammar.symbol2number = {'symbol1': 256}
    grammar.number2symbol = {256: 'symbol1'}
    grammar.states = [[(0, 0)]]
    grammar.dfas = {256: ([(0, 0)], {0: 1})}
    grammar.labels = [(256, 'symbol1')]
    grammar.start = 256
    grammar.keywords = {'keyword1': 256}

    # Dump the grammar to the temporary file
    grammar.dump(str(temp_file))

    # Create a new grammar object and load the data from the file
    new_grammar = Grammar()
    new_grammar.load(str(temp_file))

    # Verify that the loaded data matches the original data
    assert new_grammar.symbol2number == grammar.symbol2number
    assert new_grammar.number2symbol == grammar.number2symbol
    assert new_grammar.states == grammar.states
    assert new_grammar.dfas == grammar.dfas
    assert new_grammar.labels == grammar.labels
    assert new_grammar.start == grammar.start
    assert new_grammar.keywords == grammar.keywords

def test_grammar_report(capsys, grammar):
    # Set up some dummy data in the grammar object
    grammar.symbol2number = {'symbol1': 256}
    grammar.number2symbol = {256: 'symbol1'}
    grammar.states = [[(0, 0)]]
    grammar.dfas = {256: ([(0, 0)], {0: 1})}
    grammar.labels = [(256, 'symbol1')]
    grammar.start = 256
    grammar.keywords = {'keyword1': 256}

    # Call the report method
    grammar.report()

    # Capture the output
    captured = capsys.readouterr()

    # Verify that the output contains the expected data
    assert 'symbol1' in captured.out
    assert '256' in captured.out
    assert 'keyword1' not in captured.out  # Corrected assertion
