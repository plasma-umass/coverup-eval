# file: typesystem/composites.py:8-20
# asked: {"lines": [8, 9, 13, 15, 16, 17, 19, 20], "branches": []}
# gained: {"lines": [8, 9, 13, 15, 16, 17, 19, 20], "branches": []}

import pytest
from typesystem.composites import NeverMatch
from typesystem import Field

def test_nevermatch_init():
    with pytest.raises(AssertionError):
        NeverMatch(allow_null=True)

    field = NeverMatch()
    assert isinstance(field, NeverMatch)
    assert field.errors == {"never": "This never validates."}

def test_nevermatch_validate():
    field = NeverMatch()
    with pytest.raises(Exception) as exc_info:
        field.validate("any_value")
    assert str(exc_info.value) == "This never validates."
