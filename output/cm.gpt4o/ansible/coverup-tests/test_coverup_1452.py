# file lib/ansible/module_utils/common/dict_transformations.py:86-109
# lines [89, 92, 101, 103]
# branches ['91->92', '100->101', '102->103']

import pytest
from ansible.module_utils.common.dict_transformations import _camel_to_snake

def test_camel_to_snake_reversible():
    # Test case to cover line 89, 92, 101, 103
    result = _camel_to_snake("CamelCaseTest", reversible=True)
    assert result == "camel_case_test"

    result = _camel_to_snake("CamelCaseTest", reversible=False)
    assert result == "camel_case_test"

    result = _camel_to_snake("TargetGroupARNs", reversible=True)
    assert result == "target_group_a_r_ns"

    result = _camel_to_snake("TargetGroupARNs", reversible=False)
    assert result == "target_group_arns"

    result = _camel_to_snake("CamelCase", reversible=True)
    assert result == "camel_case"

    result = _camel_to_snake("CamelCase", reversible=False)
    assert result == "camel_case"
