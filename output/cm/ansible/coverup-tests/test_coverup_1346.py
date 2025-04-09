# file lib/ansible/plugins/filter/core.py:101-105
# lines [103, 104, 105]
# branches ['103->104', '103->105']

import pytest
from ansible.plugins.filter.core import quote
from ansible.module_utils._text import to_text

def test_quote_with_none_input():
    # Call the quote function with None, which should trigger lines 103-105
    result = quote(None)
    
    # Assert that the result is an empty string quoted
    assert result == "''"
