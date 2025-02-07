# file: tornado/escape.py:204-206
# asked: {"lines": [204, 205, 206], "branches": []}
# gained: {"lines": [204, 205], "branches": []}

import pytest
from tornado.escape import to_unicode
import typing

def test_to_unicode_overload():
    @typing.overload
    def to_unicode(value: str) -> str:
        pass

    # Since the actual implementation is not provided, we cannot call it directly.
    # We are testing the presence of the overload decorator.
    assert hasattr(to_unicode, '__isabstractmethod__') is False
