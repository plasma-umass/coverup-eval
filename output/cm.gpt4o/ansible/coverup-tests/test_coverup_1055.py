# file lib/ansible/module_utils/common/validation.py:173-210
# lines [191, 192, 193, 194, 196, 197, 198, 199, 200, 202, 203, 204, 205, 206, 207, 208, 210]
# branches ['188->191', '191->192', '191->202', '192->193', '192->194', '196->197', '196->198', '198->191', '198->199', '199->198', '199->200', '202->203', '202->210', '203->204', '203->210', '204->203', '204->205', '206->207', '206->208']

import pytest
from ansible.module_utils.common.validation import check_required_by
from ansible.module_utils._text import to_native
from ansible.module_utils.six import string_types

def test_check_required_by():
    # Test case where requirements is None
    assert check_required_by(None, {}) == {}

    # Test case where key is not in parameters or parameters[key] is None
    requirements = {'key1': 'required1'}
    parameters = {}
    assert check_required_by(requirements, parameters) == {}

    parameters = {'key1': None}
    assert check_required_by(requirements, parameters) == {}

    # Test case where required parameter is missing
    requirements = {'key1': 'required1'}
    parameters = {'key1': 'value1'}
    with pytest.raises(TypeError, match="missing parameter\(s\) required by 'key1': required1"):
        check_required_by(requirements, parameters)

    # Test case where required parameter is present
    requirements = {'key1': 'required1'}
    parameters = {'key1': 'value1', 'required1': 'value2'}
    assert check_required_by(requirements, parameters) == {'key1': []}

    # Test case with multiple required parameters
    requirements = {'key1': ['required1', 'required2']}
    parameters = {'key1': 'value1', 'required1': 'value2'}
    with pytest.raises(TypeError, match="missing parameter\(s\) required by 'key1': required2"):
        check_required_by(requirements, parameters)

    # Test case with options_context
    requirements = {'key1': 'required1'}
    parameters = {'key1': 'value1'}
    options_context = ['parent']
    with pytest.raises(TypeError, match="missing parameter\(s\) required by 'key1': required1 found in parent"):
        check_required_by(requirements, parameters, options_context)

    # Test case where required parameter is present but empty list is returned
    requirements = {'key1': 'required1'}
    parameters = {'key1': 'value1', 'required1': 'value2'}
    result = check_required_by(requirements, parameters)
    assert result == {'key1': []}
