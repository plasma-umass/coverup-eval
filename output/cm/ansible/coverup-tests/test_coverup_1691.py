# file lib/ansible/module_utils/common/validation.py:103-134
# lines []
# branches ['128->134', '130->132']

import pytest
from ansible.module_utils.common.validation import check_required_one_of
from ansible.module_utils._text import to_native

def test_check_required_one_of_missing_branches(mocker):
    mocker.patch('ansible.module_utils.common.validation.to_native', side_effect=lambda x: x)

    with pytest.raises(TypeError) as excinfo:
        check_required_one_of([['opt1', 'opt2']], {}, ['parent', 'child'])
    assert "one of the following is required: opt1, opt2 found in parent -> child" in str(excinfo.value)

    with pytest.raises(TypeError) as excinfo:
        check_required_one_of([['opt1', 'opt2']], {})
    assert "one of the following is required: opt1, opt2" in str(excinfo.value)
