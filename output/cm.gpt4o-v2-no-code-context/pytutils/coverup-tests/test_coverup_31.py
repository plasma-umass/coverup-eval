# file: pytutils/lazy/lazy_import.py:85-94
# asked: {"lines": [85, 86, 87, 89, 90, 93, 94], "branches": [[87, 89], [87, 90], [90, 93], [90, 94]]}
# gained: {"lines": [85, 86, 87, 89, 90, 93, 94], "branches": [[87, 89], [87, 90], [90, 93]]}

import pytest

from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer

def test_illegal_use_of_scope_replacer_unicode_str(monkeypatch):
    class MockIllegalUseOfScopeReplacer(IllegalUseOfScopeReplacer):
        def __init__(self):
            pass

        def _format(self):
            return "test string"

    obj = MockIllegalUseOfScopeReplacer()
    with monkeypatch.context() as m:
        m.setattr('builtins.unicode', str, raising=False)
        result = obj.__unicode__()
        assert isinstance(result, str)
        assert result == "test string"

def test_illegal_use_of_scope_replacer_unicode_non_str(monkeypatch):
    class MockIllegalUseOfScopeReplacer(IllegalUseOfScopeReplacer):
        def __init__(self):
            pass

        def _format(self):
            return 12345

    obj = MockIllegalUseOfScopeReplacer()
    with monkeypatch.context() as m:
        m.setattr('builtins.unicode', str, raising=False)
        result = obj.__unicode__()
        assert isinstance(result, str)
        assert result == "12345"

def test_illegal_use_of_scope_replacer_unicode_unicode(monkeypatch):
    class MockIllegalUseOfScopeReplacer(IllegalUseOfScopeReplacer):
        def __init__(self):
            pass

        def _format(self):
            return u"test unicode"

    obj = MockIllegalUseOfScopeReplacer()
    with monkeypatch.context() as m:
        m.setattr('builtins.unicode', str, raising=False)
        result = obj.__unicode__()
        assert isinstance(result, str)
        assert result == "test unicode"
