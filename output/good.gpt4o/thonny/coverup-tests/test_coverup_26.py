# file thonny/roughparse.py:183-231
# lines [186, 188, 190, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 215, 216, 217, 218, 222, 223, 224, 225, 226, 227, 228, 230, 231]
# branches ['188->190', '188->195', '196->197', '196->206', '198->199', '198->200', '202->203', '202->205', '206->215', '206->222', '216->217', '216->218', '223->224', '225->226', '225->230', '227->223', '227->228']

import pytest
from thonny.roughparse import RoughParser

def test_find_good_parse_start(mocker):
    # Initialize RoughParser with required arguments
    parser = RoughParser(indent_width=4, tabwidth=4)
    
    # Mocking _synchre to simulate the behavior
    mock_synchre = mocker.Mock()
    mock_synchre.side_effect = [
        None,  # First call returns None
        mocker.Mock(start=lambda: 5, span=lambda: (5, 10)),  # Second call returns a match
        mocker.Mock(start=lambda: 15, span=lambda: (15, 20)),  # Third call returns a match
        None  # Fourth call returns None
    ]
    
    # Mocking is_char_in_string to simulate the behavior
    mock_is_char_in_string = mocker.Mock()
    mock_is_char_in_string.side_effect = lambda x: x == 5  # Returns True only for position 5
    
    # Injecting the mocks into the parser method
    parser._synchre = mock_synchre
    parser.str = "some random string:\nwith multiple lines:\nand some more text"
    
    result = parser.find_good_parse_start(is_char_in_string=mock_is_char_in_string, _synchre=mock_synchre)
    
    # Assertions to verify the expected behavior
    assert result == 15  # The expected position after parsing
    
    # Verify the calls to the mocks
    assert mock_synchre.call_count == 3
    mock_is_char_in_string.assert_called_with(15)
    
    # Clean up
    del parser._synchre
    del parser.str
