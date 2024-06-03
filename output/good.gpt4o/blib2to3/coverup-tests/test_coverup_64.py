# file src/blib2to3/pgen2/pgen.py:29-30
# lines [29, 30]
# branches []

import pytest
from blib2to3.pgen2 import pgen, grammar

def test_pgen_grammar_class():
    # Create an instance of the PgenGrammar class
    class PgenGrammar(grammar.Grammar):
        pass

    pgen_grammar_instance = PgenGrammar()

    # Assert that the instance is indeed of type PgenGrammar
    assert isinstance(pgen_grammar_instance, PgenGrammar)

    # Assert that the instance is also of type grammar.Grammar
    assert isinstance(pgen_grammar_instance, grammar.Grammar)
