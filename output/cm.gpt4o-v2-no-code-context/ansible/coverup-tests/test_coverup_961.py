# file: lib/ansible/module_utils/yumdnf.py:155-176
# asked: {"lines": [161, 162, 163, 164, 165, 166, 168, 169, 171, 173, 174, 176], "branches": [[163, 164], [163, 168], [164, 163], [164, 165], [168, 169], [168, 171], [173, 174], [173, 176]]}
# gained: {"lines": [161, 162, 163, 164, 165, 166, 168, 169, 171, 173, 174, 176], "branches": [[163, 164], [163, 168], [164, 163], [164, 165], [168, 169], [168, 171], [173, 174], [173, 176]]}

import pytest
from ansible.module_utils.yumdnf import YumDnf

class YumDnfTestable(YumDnf):
    def __init__(self):
        pass

    def is_lockfile_pid_valid(self):
        pass

    def run(self):
        pass

class TestYumDnf:
    def test_listify_comma_sep_strings_in_list_with_commas(self):
        yumdnf = YumDnfTestable()
        input_list = ['a,b,c', 'd', 'e,f']
        expected_output = ['d', 'a', 'b', 'c', 'e', 'f']
        result = yumdnf.listify_comma_sep_strings_in_list(input_list)
        assert sorted(result) == sorted(expected_output)

    def test_listify_comma_sep_strings_in_list_without_commas(self):
        yumdnf = YumDnfTestable()
        input_list = ['a', 'b', 'c']
        expected_output = ['a', 'b', 'c']
        result = yumdnf.listify_comma_sep_strings_in_list(input_list)
        assert result == expected_output

    def test_listify_comma_sep_strings_in_list_empty_string(self):
        yumdnf = YumDnfTestable()
        input_list = [""]
        expected_output = []
        result = yumdnf.listify_comma_sep_strings_in_list(input_list)
        assert result == expected_output

    def test_listify_comma_sep_strings_in_list_mixed(self):
        yumdnf = YumDnfTestable()
        input_list = ['a,b', 'c', 'd,e,f', 'g']
        expected_output = ['c', 'g', 'a', 'b', 'd', 'e', 'f']
        result = yumdnf.listify_comma_sep_strings_in_list(input_list)
        assert sorted(result) == sorted(expected_output)
