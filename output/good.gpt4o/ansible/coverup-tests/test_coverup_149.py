# file lib/ansible/plugins/filter/core.py:468-486
# lines [468, 470, 471, 472, 474, 475, 476, 477, 478, 480, 482, 484, 486]
# branches ['471->472', '471->486', '472->474', '472->475', '475->476', '475->484', '476->477', '476->478', '478->480', '478->482']

import pytest
from ansible.plugins.filter.core import flatten

def test_flatten():
    # Test with a nested list and levels=None
    assert flatten([1, [2, [3, 4], 5], 6]) == [1, 2, 3, 4, 5, 6]
    
    # Test with a nested list and levels=1
    assert flatten([1, [2, [3, 4], 5], 6], levels=1) == [1, 2, [3, 4], 5, 6]
    
    # Test with a nested list and levels=2
    assert flatten([1, [2, [3, 4], 5], 6], levels=2) == [1, 2, 3, 4, 5, 6]
    
    # Test with skip_nulls=False
    assert flatten([1, None, [2, 'None', [3, 'null'], 4], 5], skip_nulls=False) == [1, None, 2, 'None', 3, 'null', 4, 5]
    
    # Test with skip_nulls=True
    assert flatten([1, None, [2, 'None', [3, 'null'], 4], 5], skip_nulls=True) == [1, 2, 3, 4, 5]
    
    # Test with an empty list
    assert flatten([]) == []
    
    # Test with a list of non-sequence elements
    assert flatten([1, 2, 3]) == [1, 2, 3]
    
    # Test with a list containing only null elements
    assert flatten([None, 'None', 'null']) == []
    
    # Test with a list containing only null elements and skip_nulls=False
    assert flatten([None, 'None', 'null'], skip_nulls=False) == [None, 'None', 'null']
