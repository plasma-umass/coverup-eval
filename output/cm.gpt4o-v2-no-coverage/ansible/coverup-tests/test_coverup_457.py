# file: lib/ansible/module_utils/compat/version.py:310-322
# asked: {"lines": [310, 314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}
# gained: {"lines": [310, 314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_looseversion_parse():
    lv = LooseVersion("1.5.2b2")
    assert lv.vstring == "1.5.2b2"
    assert lv.version == [1, 5, 2, 'b', 2]

    lv = LooseVersion("3.10a")
    assert lv.vstring == "3.10a"
    assert lv.version == [3, 10, 'a']

    lv = LooseVersion("1996.07.12")
    assert lv.vstring == "1996.07.12"
    assert lv.version == [1996, 7, 12]

    lv = LooseVersion("2.2beta29")
    assert lv.vstring == "2.2beta29"
    assert lv.version == [2, 2, 'beta', 29]

    lv = LooseVersion("1.13++")
    assert lv.vstring == "1.13++"
    assert lv.version == [1, 13, '++']

    lv = LooseVersion("5.5.kw")
    assert lv.vstring == "5.5.kw"
    assert lv.version == [5, 5, 'kw']

    lv = LooseVersion("2.0b1pl0")
    assert lv.vstring == "2.0b1pl0"
    assert lv.version == [2, 0, 'b', 1, 'pl', 0]
