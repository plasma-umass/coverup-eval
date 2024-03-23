# file lib/ansible/module_utils/common/dict_transformations.py:79-83
# lines [79, 80, 81, 83]
# branches ['80->81', '80->83']

import pytest
from ansible.module_utils.common.dict_transformations import _snake_to_camel

def test_snake_to_camel():
    # Test with capitalize_first=False
    assert _snake_to_camel("this_is_a_test") == "thisIsATest"
    assert _snake_to_camel("this") == "this"
    assert _snake_to_camel("this_is") == "thisIs"
    assert _snake_to_camel("this__is") == "this_Is"
    assert _snake_to_camel("_this_is") == "ThisIs"

    # Test with capitalize_first=True
    assert _snake_to_camel("this_is_a_test", capitalize_first=True) == "ThisIsATest"
    assert _snake_to_camel("this", capitalize_first=True) == "This"
    assert _snake_to_camel("this_is", capitalize_first=True) == "ThisIs"
    assert _snake_to_camel("this__is", capitalize_first=True) == "This_Is"
    assert _snake_to_camel("_this_is", capitalize_first=True) == "_ThisIs"
