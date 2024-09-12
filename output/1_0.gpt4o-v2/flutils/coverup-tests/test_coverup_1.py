# file: flutils/strutils.py:100-154
# asked: {"lines": [100, 153, 154], "branches": []}
# gained: {"lines": [100, 153, 154], "branches": []}

import pytest
from flutils.strutils import convert_escaped_unicode_literal

def test_convert_escaped_unicode_literal_basic():
    input_str = '\\x31\\x2e\\u2605\\x20\\U0001f6d1'
    expected_output = '1.★ 🛑'
    assert convert_escaped_unicode_literal(input_str) == expected_output

def test_convert_escaped_unicode_literal_env_var(monkeypatch):
    monkeypatch.setenv('TEST', '\\x31\\x2e\\u2605\\x20\\U0001f6d1')
    import os
    input_str = os.getenv('TEST')
    expected_output = '1.★ 🛑'
    assert convert_escaped_unicode_literal(input_str) == expected_output
