# file lib/ansible/module_utils/yumdnf.py:155-176
# lines [155, 161, 162, 163, 164, 165, 166, 168, 169, 171, 173, 174, 176]
# branches ['163->164', '163->168', '164->163', '164->165', '168->169', '168->171', '173->174', '173->176']

import pytest
from ansible.module_utils.yumdnf import YumDnf

class ConcreteYumDnf(YumDnf):
    def __init__(self, module):
        pass

    def is_lockfile_pid_valid(self):
        pass

    def run(self):
        pass

@pytest.fixture
def mock_yumdnf(mocker):
    module_mock = mocker.MagicMock()
    return ConcreteYumDnf(module_mock)

def test_listify_comma_sep_strings_in_list(mock_yumdnf):
    input_list = ['pkg1,pkg2', 'pkg3', 'pkg4,pkg5,pkg6']
    expected_output = ['pkg3', 'pkg1', 'pkg2', 'pkg4', 'pkg5', 'pkg6']
    result = mock_yumdnf.listify_comma_sep_strings_in_list(input_list)
    assert sorted(result) == sorted(expected_output), "The list was not processed as expected"

def test_listify_comma_sep_strings_in_list_empty_string(mock_yumdnf):
    input_list = ['']
    expected_output = []
    result = mock_yumdnf.listify_comma_sep_strings_in_list(input_list)
    assert result == expected_output, "The list should be empty when the only element is an empty string"
