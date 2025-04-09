# file lib/ansible/module_utils/common/parameters.py:299-344
# lines [310, 312, 314, 315, 316, 317, 318, 321, 322, 323, 324, 326, 327, 329, 330, 332, 335, 336, 338, 339, 340, 342]
# branches ['309->310', '310->312', '310->321', '314->315', '314->321', '322->309', '322->323', '326->309', '326->327', '327->309', '327->329', '329->330', '329->332', '332->309', '332->335', '335->336', '335->338', '338->339', '338->342']

import pytest
from ansible.module_utils.common.parameters import _list_no_log_values
from ansible.module_utils._text import to_native
from collections.abc import Mapping
from ansible.module_utils.common.validation import check_type_dict

def _return_datastructure_name(value):
    if isinstance(value, dict):
        return value.keys()
    elif isinstance(value, list):
        return [str(v) for v in value]
    else:
        return [str(value)]

@pytest.fixture
def mock_check_type_dict(mocker):
    return mocker.patch('ansible.module_utils.common.validation.check_type_dict', side_effect=lambda x: {'key': 'value'})

def test_list_no_log_values(mock_check_type_dict):
    argument_spec = {
        'param1': {'no_log': True},
        'param2': {
            'type': 'dict',
            'options': {
                'subparam1': {'no_log': True}
            }
        },
        'param3': {
            'type': 'list',
            'elements': 'dict',
            'options': {
                'subparam2': {'no_log': True}
            }
        }
    }
    params = {
        'param1': 'secret_value',
        'param2': {'subparam1': 'sub_secret_value'},
        'param3': [{'subparam2': 'sub_secret_value_list'}]
    }

    no_log_values = _list_no_log_values(argument_spec, params)

    assert 'secret_value' in no_log_values
    assert 'sub_secret_value' in no_log_values
    assert 'sub_secret_value_list' in no_log_values

    # Test TypeError branch
    with pytest.raises(TypeError, match=r"Failed to convert \"param1\""):
        _list_no_log_values({'param1': {'no_log': True}}, {'param1': object()})

    # Test sub parameter type error
    with pytest.raises(TypeError, match=r"dictionary requested, could not parse JSON or key=value"):
        _list_no_log_values({'param2': {'type': 'dict', 'options': {}}}, {'param2': 'invalid'})

    with pytest.raises(TypeError, match=r"dictionary requested, could not parse JSON or key=value"):
        _list_no_log_values({'param3': {'type': 'list', 'elements': 'dict', 'options': {}}}, {'param3': ['invalid']})
