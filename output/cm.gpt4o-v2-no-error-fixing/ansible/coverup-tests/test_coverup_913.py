# file: lib/ansible/utils/version.py:42-82
# asked: {"lines": [71], "branches": [[70, 71]]}
# gained: {"lines": [71], "branches": [[70, 71]]}

import pytest
from ansible.utils.version import _Alpha, _Numeric

def test_alpha_lt_numeric():
    alpha = _Alpha("a")
    numeric = _Numeric("1")
    assert not (alpha < numeric)

def test_alpha_le_numeric():
    alpha = _Alpha("a")
    numeric = _Numeric("1")
    assert not (alpha <= numeric)

def test_alpha_gt_numeric():
    alpha = _Alpha("a")
    numeric = _Numeric("1")
    assert alpha > numeric

def test_alpha_ge_numeric():
    alpha = _Alpha("a")
    numeric = _Numeric("1")
    assert alpha >= numeric
