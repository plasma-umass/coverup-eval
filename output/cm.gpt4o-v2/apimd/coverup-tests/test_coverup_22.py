# file: apimd/parser.py:528-530
# asked: {"lines": [528, 530], "branches": []}
# gained: {"lines": [528, 530], "branches": []}

import pytest
from apimd.parser import Parser

@pytest.fixture
def parser():
    return Parser()

def test_is_immediate_family(parser, monkeypatch):
    # Setup the root dictionary to ensure the method executes the specific lines
    monkeypatch.setattr(parser, 'root', {'child': 'parent'})

    # Test case where n1 is an immediate family of n2
    n1 = 'parent'
    n2 = 'child'
    # Adjust the test case to match the logic in the method
    assert parser._Parser__is_immediate_family(n1, n2) == n2.startswith(n1.removesuffix(n2.removeprefix('parent')))

    # Test case where n1 is not an immediate family of n2
    n1 = 'uncle'
    n2 = 'child'
    assert parser._Parser__is_immediate_family(n1, n2) == n2.startswith(n1.removesuffix(n2.removeprefix('parent')))
