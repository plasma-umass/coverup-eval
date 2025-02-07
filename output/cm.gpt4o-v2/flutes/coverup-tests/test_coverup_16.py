# file: flutes/iterator.py:316-328
# asked: {"lines": [316, 317, 318, 319, 320, 321, 322, 324, 325, 326, 327, 328], "branches": [[317, 318], [317, 319], [319, 320], [319, 324]]}
# gained: {"lines": [316, 317, 318, 319, 320, 321, 322, 324, 325, 326, 327, 328], "branches": [[317, 318], [317, 319], [319, 320], [319, 324]]}

import pytest
from flutes.iterator import Range

def test_range_no_args():
    with pytest.raises(ValueError, match="Range should be called the same way as the builtin `range`"):
        Range()

def test_range_too_many_args():
    with pytest.raises(ValueError, match="Range should be called the same way as the builtin `range`"):
        Range(1, 2, 3, 4)

def test_range_single_arg():
    r = Range(10)
    assert r.l == 0
    assert r.r == 10
    assert r.step == 1
    assert r.val == 0
    assert r.length == 10

def test_range_two_args():
    r = Range(1, 10)
    assert r.l == 1
    assert r.r == 10
    assert r.step == 1
    assert r.val == 1
    assert r.length == 9

def test_range_three_args():
    r = Range(1, 10, 2)
    assert r.l == 1
    assert r.r == 10
    assert r.step == 2
    assert r.val == 1
    assert r.length == 4
