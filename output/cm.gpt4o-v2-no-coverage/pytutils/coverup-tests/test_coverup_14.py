# file: pytutils/lazy/lazy_import.py:115-118
# asked: {"lines": [115, 116, 117, 118], "branches": [[116, 117], [116, 118]]}
# gained: {"lines": [115, 116, 117, 118], "branches": [[116, 117], [116, 118]]}

import pytest
from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer

def test_illegal_use_of_scope_replacer_eq():
    exc1 = IllegalUseOfScopeReplacer(name="test", msg="message", extra="extra")
    exc2 = IllegalUseOfScopeReplacer(name="test", msg="message", extra="extra")
    exc3 = IllegalUseOfScopeReplacer(name="test", msg="different message", extra="extra")
    exc4 = IllegalUseOfScopeReplacer(name="test", msg="message")

    assert exc1 == exc2
    assert exc1 != exc3
    assert exc1 != exc4
    assert exc1 != "not an exception"

def test_illegal_use_of_scope_replacer_init():
    exc = IllegalUseOfScopeReplacer(name="test", msg="message", extra="extra")
    assert exc.name == "test"
    assert exc.msg == "message"
    assert exc.extra == ": extra"

    exc_no_extra = IllegalUseOfScopeReplacer(name="test", msg="message")
    assert exc_no_extra.name == "test"
    assert exc_no_extra.msg == "message"
    assert exc_no_extra.extra == ""
