# file lib/ansible/plugins/filter/core.py:468-486
# lines [468, 470, 471, 472, 474, 475, 476, 477, 478, 480, 482, 484, 486]
# branches ['471->472', '471->486', '472->474', '472->475', '475->476', '475->484', '476->477', '476->478', '478->480', '478->482']

import pytest
from ansible.plugins.filter.core import flatten

def test_flatten_with_levels_and_skip_nulls(mocker):
    # Mock is_sequence to control the flow of the code
    mocker.patch('ansible.plugins.filter.core.is_sequence', side_effect=lambda x: isinstance(x, list))

    # Test data
    test_list = [1, [2, 3], None, 'None', 'null', [4, [5, 6], 'null'], [7, [8, [9]]]]
    
    # Expected results
    expected_flatten_all = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected_flatten_one_level = [1, 2, 3, 4, [5, 6], 7, [8, [9]]]
    expected_flatten_two_levels = [1, 2, 3, 4, 5, 6, 7, 8, [9]]

    # Test flatten with no levels specified (should flatten all levels)
    assert flatten(test_list) == expected_flatten_all, "Flatten all levels did not work as expected"

    # Test flatten with levels=1
    assert flatten(test_list, levels=1) == expected_flatten_one_level, "Flatten one level did not work as expected"

    # Test flatten with levels=2
    assert flatten(test_list, levels=2) == expected_flatten_two_levels, "Flatten two levels did not work as expected"

    # Test flatten with levels=0 (should not flatten)
    assert flatten(test_list, levels=0) == [1, [2, 3], [4, [5, 6], 'null'], [7, [8, [9]]]], "Flatten with levels=0 did not work as expected"

    # Test flatten with skip_nulls=False
    assert flatten(test_list, skip_nulls=False) == [1, 2, 3, None, 'None', 'null', 4, 5, 6, 'null', 7, 8, 9], "Flatten with skip_nulls=False did not work as expected"

    # Cleanup is not necessary as we are using mocker to patch the function
