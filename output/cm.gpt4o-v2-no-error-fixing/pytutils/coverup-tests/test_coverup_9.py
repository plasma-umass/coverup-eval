# file: pytutils/lazy/lazy_import.py:52-60
# asked: {"lines": [52, 53, 54, 55, 56, 58, 60], "branches": [[55, 56], [55, 58]]}
# gained: {"lines": [52, 53, 54, 55, 56, 58, 60], "branches": [[55, 56], [55, 58]]}

import pytest
from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer

def test_illegal_use_of_scope_replacer_with_extra():
    exception = IllegalUseOfScopeReplacer(name="test_name", msg="test_msg", extra="extra_info")
    assert exception.name == "test_name"
    assert exception.msg == "test_msg"
    assert exception.extra == ": extra_info"

def test_illegal_use_of_scope_replacer_without_extra():
    exception = IllegalUseOfScopeReplacer(name="test_name", msg="test_msg")
    assert exception.name == "test_name"
    assert exception.msg == "test_msg"
    assert exception.extra == ""
