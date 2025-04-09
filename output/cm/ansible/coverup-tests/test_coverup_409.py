# file lib/ansible/module_utils/compat/version.py:310-322
# lines [310, 314, 315, 316, 317, 318, 319, 320, 322]
# branches ['316->317', '316->322']

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_loose_version_parse():
    # Test with a version string that includes non-integer components
    version_string = "1.2.3b"
    lv = LooseVersion()
    lv.parse(version_string)
    
    # Check that the version string is stored correctly
    assert lv.vstring == version_string
    
    # Check that the version components are parsed correctly
    assert lv.version == [1, 2, 3, 'b']
    
    # Test with a version string that includes only integer components
    version_string_integers = "1.2.3"
    lv_integers = LooseVersion()
    lv_integers.parse(version_string_integers)
    
    # Check that the version string is stored correctly
    assert lv_integers.vstring == version_string_integers
    
    # Check that the version components are parsed correctly
    assert lv_integers.version == [1, 2, 3]
