# file thonny/roughparse.py:524-550
# lines [526, 527, 528, 529, 530, 531, 532, 534, 535, 536, 537, 538, 539, 542, 546, 547, 548, 549, 550]
# branches ['534->535', '534->546', '536->537', '536->542', '547->548', '547->549']

import pytest
from thonny.roughparse import RoughParser, C_BRACKET

@pytest.fixture
def rough_parser():
    rp = RoughParser(indent_width=4, tabwidth=8)
    yield rp

def test_compute_bracket_indent(rough_parser, mocker):
    # Mocking the _study2 method and setting continuation to C_BRACKET
    mocker.patch.object(rough_parser, '_study2')
    rough_parser.continuation = C_BRACKET
    
    # Setting up a string that will trigger the missing lines
    test_str = "def foo():\n    [\n    item1,\n    item2,\n    ]"
    rough_parser.str = test_str
    rough_parser.lastopenbracketpos = test_str.rfind("[")
    
    # Call the method under test
    indent = rough_parser.compute_bracket_indent()
    
    # Assert postconditions
    expected_indent = 4  # Indentation should be 4 spaces (one level)
    assert indent == expected_indent

    # Cleanup is handled by pytest's fixture scope
