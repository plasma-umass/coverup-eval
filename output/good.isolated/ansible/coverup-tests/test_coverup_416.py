# file lib/ansible/parsing/splitter.py:141-152
# lines [141, 146, 147, 148, 149, 151, 152]
# branches ['147->148', '147->152', '148->149', '148->151']

import pytest
from ansible.parsing.splitter import join_args

def test_join_args_empty():
    assert join_args([]) == ''

def test_join_args_single_element():
    assert join_args(['single']) == 'single'

def test_join_args_multiple_elements():
    assert join_args(['multiple', 'elements']) == 'multiple elements'

def test_join_args_with_newline():
    assert join_args(['line1\n', 'line2']) == 'line1\nline2'

def test_join_args_with_consecutive_newlines():
    assert join_args(['line1\n', '\n', 'line2']) == 'line1\n\nline2'

def test_join_args_with_space_at_end():
    assert join_args(['endswithspace ', 'nextword']) == 'endswithspace  nextword'

def test_join_args_with_newline_at_end():
    assert join_args(['endswithnewline\n', 'nextline']) == 'endswithnewline\nnextline'

# Run the tests
if __name__ == "__main__":
    pytest.main()
