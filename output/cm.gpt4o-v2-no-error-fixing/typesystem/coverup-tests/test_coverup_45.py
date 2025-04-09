# file: typesystem/fields.py:106-141
# asked: {"lines": [136, 137, 138, 140, 141], "branches": [[133, 136], [136, 137], [136, 140]]}
# gained: {"lines": [136, 137, 138, 140, 141], "branches": [[133, 136], [136, 137], [136, 140]]}

import pytest
import re
from typesystem.fields import String

def test_string_pattern_none():
    field = String(pattern=None)
    assert field.pattern is None
    assert field.pattern_regex is None

def test_string_pattern_str():
    pattern = r'^[a-z]+$'
    field = String(pattern=pattern)
    assert field.pattern == pattern
    assert field.pattern_regex.pattern == pattern

def test_string_pattern_regex():
    pattern = re.compile(r'^[a-z]+$')
    field = String(pattern=pattern)
    assert field.pattern == pattern.pattern
    assert field.pattern_regex == pattern
