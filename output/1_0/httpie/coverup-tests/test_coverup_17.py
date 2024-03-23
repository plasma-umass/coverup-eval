# file httpie/cli/dicts.py:17-42
# lines []
# branches ['33->35']

import pytest
from httpie.cli.dicts import MultiValueOrderedDict

def test_multivalue_ordered_dict_setitem_with_existing_list_value():
    # Setup: create a MultiValueOrderedDict and set a key with a non-list value
    mvod = MultiValueOrderedDict()
    mvod['key'] = 'value1'
    # Set the same key with a new value to create a list
    mvod['key'] = 'value2'

    # Exercise: set the same key with another new value
    mvod['key'] = 'value3'

    # Verify: the key should now correspond to a list containing all three values
    assert mvod['key'] == ['value1', 'value2', 'value3']

    # Cleanup: not necessary, as the MultiValueOrderedDict is a local variable
