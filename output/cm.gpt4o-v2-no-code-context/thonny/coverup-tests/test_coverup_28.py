# file: thonny/roughparse.py:758-799
# asked: {"lines": [770, 771, 772, 773, 774, 775, 777, 778, 779, 780, 781, 782, 783, 785, 786, 788, 789, 790, 791, 795, 796, 799], "branches": [[772, 777], [772, 781], [778, 779], [778, 780], [782, 783], [782, 785], [788, 789], [788, 795], [789, 790], [789, 791]]}
# gained: {"lines": [770, 771, 772, 773, 774, 775, 777, 778, 779, 780, 781, 782, 783, 785, 786, 788, 789, 790, 791, 799], "branches": [[772, 777], [772, 781], [778, 779], [778, 780], [782, 783], [782, 785], [788, 789], [789, 790], [789, 791]]}

import pytest
from thonny.roughparse import HyperParser

@pytest.fixture
def hyperparser():
    class MockText:
        def index(self, index_str):
            return int(index_str.split('-')[1][:-1])

    class MockHyperParser(HyperParser):
        def __init__(self):
            self.bracketing = [(0, 0), (1, 1), (2, 0), (3, 1), (4, 0)]
            self.indexbracket = 2
            self.isopener = [True, False, True, False, True]
            self.rawtext = "({[)]}"
            self.text = MockText()
            self.stopatindex = 5

    return MockHyperParser()

def test_get_surrounding_brackets_no_openers(hyperparser):
    result = hyperparser.get_surrounding_brackets(openers="<>")
    assert result is None

def test_get_surrounding_brackets_mustclose_true(hyperparser):
    hyperparser.bracketing = [(0, 0), (1, 1), (2, 0), (3, 1)]
    result = hyperparser.get_surrounding_brackets(mustclose=True)
    assert result is None

def test_get_surrounding_brackets_mustclose_false(hyperparser):
    hyperparser.bracketing = [(0, 0), (1, 1), (2, 0), (3, 1)]
    result = hyperparser.get_surrounding_brackets(mustclose=False)
    assert result == (4, 5)

def test_get_surrounding_brackets_with_closing_bracket(hyperparser):
    hyperparser.bracketing = [(0, 0), (1, 1), (2, 0), (3, 1), (4, 0)]
    result = hyperparser.get_surrounding_brackets()
    assert result == (4, 5)
