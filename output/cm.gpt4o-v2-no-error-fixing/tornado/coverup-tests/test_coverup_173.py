# file: tornado/locale.py:75-86
# asked: {"lines": [85, 86], "branches": []}
# gained: {"lines": [85, 86], "branches": []}

import pytest
from tornado.locale import set_default_locale

def test_set_default_locale(monkeypatch):
    # Setup initial state
    monkeypatch.setattr('tornado.locale._default_locale', 'en_US')
    monkeypatch.setattr('tornado.locale._supported_locales', frozenset(['en_US']))
    monkeypatch.setattr('tornado.locale._translations', {'es_ES': 'Spanish'})

    # Call the function with a new locale code
    set_default_locale('fr_FR')

    # Assertions to verify the postconditions
    from tornado.locale import _default_locale, _supported_locales
    assert _default_locale == 'fr_FR'
    assert _supported_locales == frozenset(['es_ES', 'fr_FR'])

    # Cleanup
    monkeypatch.undo()
