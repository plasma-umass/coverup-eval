# file thonny/jedi_utils.py:46-49
# lines [47, 49]
# branches []

import pytest
from unittest.mock import patch

def test_parse_source_executes_import_and_parse(mocker):
    source_code = "def foo(): pass"
    
    # Mocking the import of parso within the parse_source function
    mock_parso = mocker.MagicMock()
    mock_parse = mock_parso.parse
    mock_parse.return_value = "parsed_result"
    
    with patch.dict('sys.modules', {'parso': mock_parso}):
        from thonny.jedi_utils import parse_source
        result = parse_source(source_code)
    
    # Assertions to verify the correct behavior
    mock_parso.parse.assert_called_once_with(source_code)
    assert result == "parsed_result"
