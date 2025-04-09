# file src/blib2to3/pgen2/pgen.py:264-283
# lines [271, 272, 273, 274, 275, 276, 277, 279, 280, 281, 282, 283]
# branches ['272->exit', '272->273', '274->272', '274->275', '275->274', '275->276', '277->275', '277->279', '280->281', '280->282']

import pytest
from blib2to3.pgen2.pgen import ParserGenerator

def test_simplify_dfa(mocker):
    # Mock DFAState to control equality and unifystate behavior
    class MockDFAState:
        def __init__(self, id):
            self.id = id

        def __eq__(self, other):
            return self.id == other.id

        def unifystate(self, old, new):
            pass

    # Create a list of DFAState instances with some duplicates
    dfa = [MockDFAState(1), MockDFAState(2), MockDFAState(1), MockDFAState(3)]

    # Mock the ParserGenerator's __init__ to bypass file handling
    mocker.patch.object(ParserGenerator, '__init__', lambda self, filename, stream=None: None)
    pg = ParserGenerator(None)

    # Call simplify_dfa
    pg.simplify_dfa(dfa)

    # Assert that duplicates are removed
    assert len(dfa) == 3
    assert dfa[0].id == 1
    assert dfa[1].id == 2
    assert dfa[2].id == 3

    # Clean up any mocks if necessary (not needed in this case)

# Note: No top-level code calling pytest.main or the test itself
