# file src/blib2to3/pgen2/grammar.py:31-80
# lines [31, 32]
# branches []

import pytest
from blib2to3.pgen2.grammar import Grammar
import pickle
import os

class TestGrammar:
    @pytest.fixture
    def grammar(self):
        g = Grammar()
        g.symbol2number = {'sym1': 256}
        g.number2symbol = {256: 'sym1'}
        g.states = [[(1, 2)], [(0, 1)]]
        g.dfas = {256: (0, {1: 1})}
        g.labels = [(0, None), (1, 'keyword')]
        g.start = 256
        g.keywords = {'keyword': 1}
        return g

    def test_grammar_dump_load(self, grammar, tmp_path):
        # Dump the grammar to a file
        dump_file = tmp_path / "grammar_dump.pkl"
        dump_file_path = str(dump_file)  # Convert to string for compatibility
        grammar.dump(dump_file_path)

        # Load the grammar from the file
        new_grammar = Grammar()
        new_grammar.load(dump_file_path)

        # Check if the loaded grammar is the same as the dumped one
        assert new_grammar.symbol2number == grammar.symbol2number
        assert new_grammar.number2symbol == grammar.number2symbol
        assert new_grammar.states == grammar.states
        assert new_grammar.dfas == grammar.dfas
        assert new_grammar.labels == grammar.labels
        assert new_grammar.start == grammar.start
        assert new_grammar.keywords == grammar.keywords

        # Clean up the dump file
        os.remove(dump_file_path)
