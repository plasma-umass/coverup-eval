# file: src/blib2to3/pgen2/pgen.py:29-30
# asked: {"lines": [29, 30], "branches": []}
# gained: {"lines": [29, 30], "branches": []}

import pytest
from blib2to3.pgen2 import pgen, grammar

def test_pgen_grammar_inheritance():
    # Ensure PgenGrammar is a subclass of grammar.Grammar
    assert issubclass(pgen.PgenGrammar, grammar.Grammar)

def test_pgen_grammar_instance():
    # Ensure an instance of PgenGrammar can be created
    instance = pgen.PgenGrammar()
    assert isinstance(instance, pgen.PgenGrammar)
    assert isinstance(instance, grammar.Grammar)
