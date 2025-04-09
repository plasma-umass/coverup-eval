# file thefuck/shells/generic.py:52-54
# lines [52, 53, 54]
# branches []

import pytest
from thefuck.shells.generic import Generic
from thefuck.utils import memoize

# Assuming the existence of the following in thefuck/shells/generic.py
# If not present, they should be mocked or added accordingly.
# class memoize(object):
#     ...

# Mocking the _get_history_lines method
def test_get_history(mocker):
    mocker.patch('thefuck.shells.generic.Generic._get_history_lines', return_value=['ls', 'cd ..', 'git status'])

    shell = Generic()
    history = shell.get_history()

    # Assert that the history is correct
    assert history == ['ls', 'cd ..', 'git status']

    # Call get_history again to test memoization
    history_again = shell.get_history()

    # Assert that the history is still correct and memoization works
    assert history_again == history

    # Assert that _get_history_lines was called only once due to memoization
    assert Generic._get_history_lines.call_count == 1
