# file: f153/__init__.py:1-12
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}

import pytest
from f153 import Strongest_Extension

def test_Strongest_Extension():
    # Test case 1: Single extension
    result = Strongest_Extension("ClassA", ["EXT"])
    assert result == "ClassA.EXT"

    # Test case 2: Multiple extensions with different strengths
    result = Strongest_Extension("ClassB", ["ext", "EXT", "ExT"])
    assert result == "ClassB.EXT"

    # Test case 3: Multiple extensions with same strengths
    result = Strongest_Extension("ClassC", ["ExT", "eXt", "EXt"])
    assert result == "ClassC.ExT"

    # Test case 4: All lowercase extensions
    result = Strongest_Extension("ClassD", ["ext", "ext", "ext"])
    assert result == "ClassD.ext"

    # Test case 5: All uppercase extensions
    result = Strongest_Extension("ClassE", ["EXT", "EXT", "EXT"])
    assert result == "ClassE.EXT"

    # Test case 6: Mixed case extensions
    result = Strongest_Extension("ClassF", ["eXt", "ExT", "EXt"])
    assert result == "ClassF.ExT"
