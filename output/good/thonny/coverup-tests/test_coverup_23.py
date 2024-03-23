# file thonny/jedi_utils.py:46-49
# lines [47, 49]
# branches []

import pytest
from unittest.mock import patch
import parso

def test_parse_source_executes_missing_lines():
    source_code = "print('Hello, World!')"
    with patch('parso.parse') as mock_parse:
        from thonny.jedi_utils import parse_source
        parse_source(source_code)
        mock_parse.assert_called_once_with(source_code)
