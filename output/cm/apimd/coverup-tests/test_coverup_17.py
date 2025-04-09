# file apimd/parser.py:528-530
# lines [528, 530]
# branches []

import pytest
from apimd.parser import Parser

@pytest.fixture
def parser():
    p = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={'Smith': 'John Smith', 'Doe': 'Jane Doe'}, alias={}, const={})
    yield p

def test_is_immediate_family(parser):
    # Accessing the private method using its mangled name
    assert parser._Parser__is_immediate_family('Smith', 'Smith') == True
    assert parser._Parser__is_immediate_family('Doe', 'Doe') == True
    assert parser._Parser__is_immediate_family('Smith', 'Doe') == False
    assert parser._Parser__is_immediate_family('Doe', 'Smith') == False
