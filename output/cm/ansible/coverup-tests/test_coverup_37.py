# file lib/ansible/module_utils/common/validation.py:173-210
# lines [173, 187, 188, 189, 191, 192, 193, 194, 196, 197, 198, 199, 200, 202, 203, 204, 205, 206, 207, 208, 210]
# branches ['188->189', '188->191', '191->192', '191->202', '192->193', '192->194', '196->197', '196->198', '198->191', '198->199', '199->198', '199->200', '202->203', '202->210', '203->204', '203->210', '204->203', '204->205', '206->207', '206->208']

import pytest
from ansible.module_utils.common.validation import check_required_by
from ansible.module_utils._text import to_native

@pytest.fixture
def cleanup():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_check_required_by_missing_parameters(cleanup, mocker):
    requirements = {'param1': ['req1', 'req2'], 'param2': 'req3'}
    parameters = {'param1': 'value1', 'req3': 'value3'}
    options_context = ['context1', 'context2']

    with pytest.raises(TypeError) as excinfo:
        check_required_by(requirements, parameters, options_context)

    assert "missing parameter(s) required by 'param1': req1, req2 found in context1 -> context2" in str(excinfo.value)
