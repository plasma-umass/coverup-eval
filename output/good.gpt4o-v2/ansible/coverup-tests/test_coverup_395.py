# file: lib/ansible/module_utils/compat/version.py:310-322
# asked: {"lines": [310, 314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}
# gained: {"lines": [310, 314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_looseversion_parse():
    version_string = "1.5.2b2"
    lv = LooseVersion(version_string)
    assert lv.vstring == version_string
    assert lv.version == [1, 5, 2, 'b', 2]

    version_string = "3.10a"
    lv = LooseVersion(version_string)
    assert lv.vstring == version_string
    assert lv.version == [3, 10, 'a']

    version_string = "1996.07.12"
    lv = LooseVersion(version_string)
    assert lv.vstring == version_string
    assert lv.version == [1996, 7, 12]

    version_string = "2.2beta29"
    lv = LooseVersion(version_string)
    assert lv.vstring == version_string
    assert lv.version == [2, 2, 'beta', 29]

    version_string = "1.13++"
    lv = LooseVersion(version_string)
    assert lv.vstring == version_string
    assert lv.version == [1, 13, '++']
