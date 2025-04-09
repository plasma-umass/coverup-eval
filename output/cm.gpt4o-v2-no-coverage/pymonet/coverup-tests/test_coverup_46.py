# file: pymonet/maybe.py:19-22
# asked: {"lines": [19, 20, 21, 22], "branches": []}
# gained: {"lines": [19, 20, 21, 22], "branches": []}

import pytest
from pymonet.maybe import Maybe

def test_maybe_eq():
    just_1 = Maybe(1, False)
    just_1_again = Maybe(1, False)
    just_2 = Maybe(2, False)
    nothing = Maybe(None, True)
    nothing_again = Maybe(None, True)

    # Test equality of two Maybe instances with the same value
    assert just_1 == just_1_again

    # Test inequality of two Maybe instances with different values
    assert just_1 != just_2

    # Test equality of two Maybe instances representing nothing
    assert nothing == nothing_again

    # Test inequality of a Maybe instance with a value and one representing nothing
    assert just_1 != nothing

    # Test inequality with an instance of a different type
    assert just_1 != 1
