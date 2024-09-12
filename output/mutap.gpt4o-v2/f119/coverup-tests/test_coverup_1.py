# file: f119/__init__.py:1-29
# asked: {"lines": [1, 16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}
# gained: {"lines": [1, 16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}

import pytest
from f119 import match_parens

def test_match_parens_yes_case():
    assert match_parens(['()(', ')']) == 'Yes'
    assert match_parens(['', '()']) == 'Yes'
    assert match_parens(['()', '']) == 'Yes'

def test_match_parens_no_case():
    assert match_parens([')', ')']) == 'No'
    assert match_parens(['(', '(']) == 'No'
    assert match_parens([')(', ')']) == 'No'
    assert match_parens(['(', '']) == 'No'
    assert match_parens(['(', '()']) == 'No'
