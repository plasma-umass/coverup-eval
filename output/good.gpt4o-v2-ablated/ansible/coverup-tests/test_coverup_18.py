# file: lib/ansible/utils/version.py:42-82
# asked: {"lines": [42, 43, 48, 49, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 65, 66, 67, 68, 69, 70, 71, 73, 75, 76, 78, 79, 81, 82], "branches": [[55, 56], [55, 57], [57, 58], [57, 60], [66, 67], [66, 68], [68, 69], [68, 70], [70, 71], [70, 73]]}
# gained: {"lines": [42, 43, 48, 49, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 65, 66, 67, 68, 69, 70, 73, 75, 76, 78, 79, 81, 82], "branches": [[55, 56], [55, 57], [57, 58], [57, 60], [66, 67], [66, 68], [68, 69], [68, 70], [70, 73]]}

import pytest

from ansible.utils.version import _Alpha

def test_alpha_repr():
    alpha = _Alpha("test")
    assert repr(alpha) == "'test'"

def test_alpha_eq():
    alpha1 = _Alpha("test")
    alpha2 = _Alpha("test")
    alpha3 = _Alpha("different")
    assert alpha1 == alpha2
    assert alpha1 != alpha3
    assert alpha1 == "test"
    assert alpha1 != "different"
    assert alpha1 != 123  # Different type

def test_alpha_ne():
    alpha1 = _Alpha("test")
    alpha2 = _Alpha("different")
    assert alpha1 != alpha2
    assert alpha1 != "different"
    assert alpha1 != 123  # Different type

def test_alpha_lt():
    alpha1 = _Alpha("a")
    alpha2 = _Alpha("b")
    assert alpha1 < alpha2
    assert alpha1 < "b"
    with pytest.raises(ValueError):
        alpha1 < 123  # Different type

def test_alpha_le():
    alpha1 = _Alpha("a")
    alpha2 = _Alpha("a")
    alpha3 = _Alpha("b")
    assert alpha1 <= alpha2
    assert alpha1 <= alpha3
    assert alpha1 <= "a"
    assert alpha1 <= "b"

def test_alpha_gt():
    alpha1 = _Alpha("b")
    alpha2 = _Alpha("a")
    assert alpha1 > alpha2
    assert alpha1 > "a"

def test_alpha_ge():
    alpha1 = _Alpha("b")
    alpha2 = _Alpha("b")
    alpha3 = _Alpha("a")
    assert alpha1 >= alpha2
    assert alpha1 >= alpha3
    assert alpha1 >= "a"
    assert alpha1 >= "b"
