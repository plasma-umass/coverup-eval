# file: src/blib2to3/pgen2/pgen.py:285-300
# asked: {"lines": [285, 287, 288, 289, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300], "branches": [[288, 289], [288, 291], [295, 296], [295, 300]]}
# gained: {"lines": [285, 287, 288, 289, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300], "branches": [[288, 289], [288, 291], [295, 296], [295, 300]]}

import pytest
from unittest.mock import MagicMock
from blib2to3.pgen2.pgen import ParserGenerator, NFAState
from pathlib import Path
from io import StringIO

@pytest.fixture
def parser_generator(mocker):
    mocker.patch('blib2to3.pgen2.pgen.ParserGenerator.parse', return_value=({}, 'start'))
    dummy_file = StringIO("dummy content")
    pg = ParserGenerator(filename=Path("dummy"), stream=dummy_file)
    pg.parse_alt = MagicMock()
    pg.gettoken = MagicMock()
    pg.value = None
    return pg

def test_parse_rhs_single_alt(parser_generator):
    a, z = NFAState(), NFAState()
    parser_generator.parse_alt.return_value = (a, z)
    parser_generator.value = "not|"
    
    result_a, result_z = parser_generator.parse_rhs()
    
    parser_generator.parse_alt.assert_called_once()
    assert result_a == a
    assert result_z == z

def test_parse_rhs_multiple_alts(parser_generator):
    a1, z1 = NFAState(), NFAState()
    a2, z2 = NFAState(), NFAState()
    parser_generator.parse_alt.side_effect = [(a1, z1), (a2, z2)]
    parser_generator.value = "|"
    
    def side_effect():
        parser_generator.value = "not|"
    parser_generator.gettoken.side_effect = side_effect
    
    result_aa, result_zz = parser_generator.parse_rhs()
    
    assert result_aa.arcs[0][1] == a1
    assert z1.arcs[0][1] == result_zz
    assert result_aa.arcs[1][1] == a2
    assert z2.arcs[0][1] == result_zz
    assert parser_generator.parse_alt.call_count == 2
    assert parser_generator.gettoken.call_count == 1
