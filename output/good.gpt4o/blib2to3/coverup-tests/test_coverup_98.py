# file src/blib2to3/pgen2/grammar.py:98-113
# lines [107]
# branches ['104->107']

import os
import pickle
import tempfile
from pathlib import Path
import pytest
from unittest import mock
from blib2to3.pgen2.grammar import Grammar

class TestGrammar:
    def test_dump_with_getstate(self, mocker):
        class MockGrammar(Grammar):
            def __getstate__(self):
                return {'mock_key': 'mock_value'}

        mock_grammar = MockGrammar()
        mock_filename = Path(tempfile.mktemp())

        try:
            # Use mock to patch the hasattr function to simulate the absence of __dict__
            mocker.patch('blib2to3.pgen2.grammar.hasattr', side_effect=lambda obj, name: False if name == "__dict__" else hasattr(obj, name))
            mock_grammar.dump(mock_filename)

            with open(mock_filename, 'rb') as f:
                data = pickle.load(f)
                assert data == {'mock_key': 'mock_value'}
        finally:
            if mock_filename.exists():
                os.remove(mock_filename)
