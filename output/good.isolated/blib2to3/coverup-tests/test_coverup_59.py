# file src/blib2to3/pgen2/pgen.py:29-30
# lines [29, 30]
# branches []

import pytest
from blib2to3.pgen2 import pgen
from blib2to3.pgen2 import grammar

# Assuming the existence of a test_grammar.py file in the tests directory

def test_pgen_grammar_instantiation():
    # Test the instantiation of PgenGrammar to ensure coverage
    pgen_grammar_instance = pgen.PgenGrammar()
    assert isinstance(pgen_grammar_instance, grammar.Grammar)
    assert isinstance(pgen_grammar_instance, pgen.PgenGrammar)
