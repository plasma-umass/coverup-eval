# file: src/blib2to3/pgen2/pgen.py:428-430
# asked: {"lines": [428, 429, 430], "branches": []}
# gained: {"lines": [428, 429, 430], "branches": []}

import pytest
from blib2to3.pgen2.pgen import generate_grammar, ParserGenerator, PgenGrammar
from pathlib import Path
import os

def test_generate_grammar(monkeypatch):
    # Create a temporary grammar file
    test_grammar_content = """
# Test grammar
file: (NEWLINE | stmt)* ENDMARKER
stmt: simple_stmt
simple_stmt: NAME NEWLINE
"""
    test_grammar_path = Path("test_grammar.txt")
    with open(test_grammar_path, "w") as f:
        f.write(test_grammar_content)

    # Ensure the file is cleaned up after the test
    def cleanup():
        if test_grammar_path.exists():
            os.remove(test_grammar_path)

    try:
        grammar = generate_grammar(test_grammar_path)
        assert isinstance(grammar, PgenGrammar)
    finally:
        cleanup()
