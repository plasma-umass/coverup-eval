# file src/blib2to3/pgen2/pgen.py:80-88
# lines [81, 82, 83, 84, 85, 87, 88]
# branches ['84->85', '84->88']

import pytest
from blib2to3.pgen2.pgen import ParserGenerator, PgenGrammar

@pytest.fixture
def mock_pgen_grammar(mocker):
    return mocker.Mock(spec=PgenGrammar)

def test_make_first_executes_all_branches(mocker, mock_pgen_grammar):
    # Create a mock instance of ParserGenerator with the required 'first' attribute
    pg = mocker.Mock(spec=ParserGenerator)
    pg.first = {'test_name': ['label1', 'label2']}
    
    # Mock the make_label method to return unique labels
    mocker.patch.object(pg, 'make_label', side_effect=lambda c, label: hash(label))
    
    # Call the method and capture the result
    result = ParserGenerator.make_first(pg, mock_pgen_grammar, 'test_name')
    
    # Assertions to verify the postconditions
    assert result is not None
    assert len(result) == 2
    assert all(isinstance(key, int) for key in result.keys())
    assert all(value == 1 for value in result.values())
