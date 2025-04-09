# file: src/blib2to3/pgen2/grammar.py:149-163
# asked: {"lines": [149, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163], "branches": []}
# gained: {"lines": [149, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163], "branches": []}

import pytest
from blib2to3.pgen2.grammar import Grammar

def test_grammar_report(monkeypatch, capsys):
    # Arrange
    grammar = Grammar()
    
    # Act
    grammar.report()
    
    # Assert
    captured = capsys.readouterr()
    assert "s2n" in captured.out
    assert "{}" in captured.out  # symbol2number is empty
    assert "n2s" in captured.out
    assert "{}" in captured.out  # number2symbol is empty
    assert "states" in captured.out
    assert "[]" in captured.out  # states is empty
    assert "dfas" in captured.out
    assert "{}" in captured.out  # dfas is empty
    assert "labels" in captured.out
    assert "[(0, 'EMPTY')]" in captured.out  # labels has one item
    assert "start 256" in captured.out  # start is 256
