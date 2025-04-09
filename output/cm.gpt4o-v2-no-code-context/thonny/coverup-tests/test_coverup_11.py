# file: thonny/jedi_utils.py:46-49
# asked: {"lines": [46, 47, 49], "branches": []}
# gained: {"lines": [46, 47, 49], "branches": []}

import pytest
import sys
from thonny.jedi_utils import parse_source

def test_parse_source(monkeypatch):
    class MockParso:
        @staticmethod
        def parse(source):
            return f"Parsed: {source}"

    # Mock the parso module itself
    mock_parso_module = MockParso()
    sys.modules['parso'] = mock_parso_module

    source_code = "print('Hello, World!')"
    result = parse_source(source_code)
    assert result == f"Parsed: {source_code}"

    # Clean up by removing the mock
    del sys.modules['parso']
