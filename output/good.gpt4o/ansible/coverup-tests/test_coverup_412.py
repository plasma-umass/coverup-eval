# file lib/ansible/module_utils/compat/version.py:310-322
# lines [310, 314, 315, 316, 317, 318, 319, 320, 322]
# branches ['316->317', '316->322']

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_loose_version_parse():
    lv = LooseVersion("1.2.3a4")
    lv.parse("1.2.3a4")
    
    assert lv.vstring == "1.2.3a4"
    assert lv.version == [1, 2, 3, 'a', 4]

    lv.parse("2.0")
    assert lv.vstring == "2.0"
    assert lv.version == [2, 0]

    lv.parse("1.0.0")
    assert lv.vstring == "1.0.0"
    assert lv.version == [1, 0, 0]

    lv.parse("1.2.3b5")
    assert lv.vstring == "1.2.3b5"
    assert lv.version == [1, 2, 3, 'b', 5]

    lv.parse("1.2.3.4")
    assert lv.vstring == "1.2.3.4"
    assert lv.version == [1, 2, 3, 4]
