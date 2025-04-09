# file lib/ansible/module_utils/common/network.py:32-36
# lines [32, 33, 34, 35, 36]
# branches []

import pytest
from ansible.module_utils.common.network import is_masklen

def test_is_masklen():
    # Test valid mask lengths
    assert is_masklen('0') == True
    assert is_masklen('32') == True
    assert is_masklen('16') == True

    # Test invalid mask lengths
    assert is_masklen('-1') == False
    assert is_masklen('33') == False
    assert is_masklen('100') == False

    # Test non-integer values
    assert is_masklen('abc') == False
    assert is_masklen('3.14') == False
    assert is_masklen('') == False

    # Test None value
    with pytest.raises(TypeError):
        is_masklen(None)

    # Test boolean values
    assert is_masklen(str(True)) == False
    assert is_masklen(str(False)) == False
