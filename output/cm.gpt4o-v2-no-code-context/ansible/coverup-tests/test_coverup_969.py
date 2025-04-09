# file: lib/ansible/utils/version.py:42-82
# asked: {"lines": [52, 60, 63, 68, 69, 70, 71, 73, 82], "branches": [[57, 60], [66, 68], [68, 69], [68, 70], [70, 71], [70, 73]]}
# gained: {"lines": [52, 60, 63, 68, 69, 70, 73, 82], "branches": [[57, 60], [66, 68], [68, 69], [68, 70], [70, 73]]}

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
    assert alpha1 != 123

def test_alpha_ne():
    alpha1 = _Alpha("test")
    alpha2 = _Alpha("test")
    alpha3 = _Alpha("different")
    assert not (alpha1 != alpha2)
    assert alpha1 != alpha3

def test_alpha_lt():
    alpha1 = _Alpha("a")
    alpha2 = _Alpha("b")
    assert alpha1 < alpha2
    assert not (alpha2 < alpha1)
    assert alpha1 < "b"
    assert not (alpha2 < "a")
    with pytest.raises(ValueError):
        alpha1 < 123

def test_alpha_le():
    alpha1 = _Alpha("a")
    alpha2 = _Alpha("a")
    alpha3 = _Alpha("b")
    assert alpha1 <= alpha2
    assert alpha1 <= alpha3
    assert not (alpha3 <= alpha1)

def test_alpha_gt():
    alpha1 = _Alpha("b")
    alpha2 = _Alpha("a")
    assert alpha1 > alpha2
    assert not (alpha2 > alpha1)

def test_alpha_ge():
    alpha1 = _Alpha("a")
    alpha2 = _Alpha("a")
    alpha3 = _Alpha("b")
    assert alpha1 >= alpha2
    assert alpha3 >= alpha1
    assert not (alpha1 >= alpha3)
