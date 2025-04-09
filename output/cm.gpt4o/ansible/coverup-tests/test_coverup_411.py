# file lib/ansible/parsing/splitter.py:141-152
# lines [141, 146, 147, 148, 149, 151, 152]
# branches ['147->148', '147->152', '148->149', '148->151']

import pytest
from ansible.parsing.splitter import join_args

def test_join_args():
    # Test with an empty list
    assert join_args([]) == ''

    # Test with a single element
    assert join_args(['arg1']) == 'arg1'

    # Test with multiple elements without newlines
    assert join_args(['arg1', 'arg2', 'arg3']) == 'arg1 arg2 arg3'

    # Test with multiple elements with newlines
    assert join_args(['arg1\n', 'arg2', 'arg3\n', 'arg4']) == 'arg1\narg2 arg3\narg4'

    # Test with elements that end with newlines
    assert join_args(['arg1\n', 'arg2\n', 'arg3\n']) == 'arg1\narg2\narg3\n'

    # Test with elements that start with newlines
    assert join_args(['\narg1', '\narg2', '\narg3']) == '\narg1 \narg2 \narg3'

    # Test with mixed elements
    assert join_args(['arg1', '\narg2', 'arg3\n', 'arg4']) == 'arg1 \narg2 arg3\narg4'
