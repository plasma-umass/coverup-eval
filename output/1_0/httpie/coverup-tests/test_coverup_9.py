# file httpie/cli/dicts.py:17-42
# lines [17, 18, 20, 29, 30, 31, 33, 34, 35, 37, 38, 39, 40, 41, 42]
# branches ['30->31', '30->33', '33->34', '33->35', '38->exit', '38->39', '39->40', '39->41', '41->38', '41->42']

import pytest
from httpie.cli.dicts import MultiValueOrderedDict

def test_multivalue_ordered_dict_setitem_and_items():
    mvod = MultiValueOrderedDict()
    mvod['key1'] = 'value1'
    mvod['key2'] = 'value2'
    mvod['key1'] = 'value1-2'
    mvod['key2'] = 'value2-2'
    mvod['key3'] = 'value3'

    # Check that the key with multiple values now has a list of values
    assert isinstance(mvod['key1'], list)
    assert mvod['key1'] == ['value1', 'value1-2']

    # Check that the key with a single value is not a list
    assert not isinstance(mvod['key3'], list)
    assert mvod['key3'] == 'value3'

    # Check that the items method returns an iterator of tuples
    items = list(mvod.items())
    expected_items = [
        ('key1', 'value1'),
        ('key1', 'value1-2'),
        ('key2', 'value2'),
        ('key2', 'value2-2'),
        ('key3', 'value3')
    ]
    assert items == expected_items

    # Clean up
    del mvod
