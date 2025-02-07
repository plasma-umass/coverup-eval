# file: typesystem/composites.py:8-20
# asked: {"lines": [20], "branches": []}
# gained: {"lines": [20], "branches": []}

import pytest
from typesystem.composites import NeverMatch

def test_nevermatch_init():
    with pytest.raises(AssertionError):
        NeverMatch(allow_null=True)

def test_nevermatch_validate():
    field = NeverMatch()
    with pytest.raises(Exception) as exc_info:
        field.validate("any_value")
    assert str(exc_info.value) == "This never validates."
