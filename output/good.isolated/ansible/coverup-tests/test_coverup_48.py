# file lib/ansible/module_utils/common/parameters.py:299-344
# lines [299, 308, 309, 310, 312, 314, 315, 316, 317, 318, 321, 322, 323, 324, 326, 327, 329, 330, 332, 335, 336, 338, 339, 340, 342, 344]
# branches ['309->310', '309->344', '310->312', '310->321', '314->315', '314->321', '322->309', '322->323', '326->309', '326->327', '327->309', '327->329', '329->330', '329->332', '332->309', '332->335', '335->336', '335->338', '338->339', '338->342']

import pytest
from ansible.module_utils.common.parameters import _list_no_log_values
from ansible.module_utils._text import to_native
from ansible.module_utils.six import string_types
from collections.abc import Mapping

def test_list_no_log_values_with_suboptions(mocker):
    # Mock the _return_datastructure_name function to return a set with the input value
    mocker.patch('ansible.module_utils.common.parameters._return_datastructure_name', side_effect=lambda x: {x})

    argument_spec = {
        'password': {'no_log': True},
        'user': {
            'options': {
                'secret': {'no_log': True}
            },
            'type': 'dict'
        },
        'users': {
            'options': {
                'secret': {'no_log': True}
            },
            'type': 'list',
            'elements': 'dict'
        }
    }

    params = {
        'password': 'supersecret',
        'user': {
            'name': 'testuser',
            'secret': 'shouldnotlog'
        },
        'users': [
            {
                'name': 'user1',
                'secret': 'hidethis'
            },
            {
                'name': 'user2',
                'secret': 'andthis'
            }
        ]
    }

    expected_no_log_values = {'supersecret', 'shouldnotlog', 'hidethis', 'andthis'}

    no_log_values = _list_no_log_values(argument_spec, params)

    assert no_log_values == expected_no_log_values

    # Test with a string that should be converted to a dict
    params['user'] = '{"name": "testuser", "secret": "shouldnotlog"}'
    mocker.patch('ansible.module_utils.common.parameters.check_type_dict', side_effect=lambda x: eval(x))

    no_log_values = _list_no_log_values(argument_spec, params)

    assert no_log_values == expected_no_log_values

    # Test with invalid type for sub_parameter
    params['user'] = 'notadict'
    mocker.patch('ansible.module_utils.common.parameters.check_type_dict', side_effect=lambda x: x if isinstance(x, Mapping) else None)

    with pytest.raises(TypeError):
        _list_no_log_values(argument_spec, params)
