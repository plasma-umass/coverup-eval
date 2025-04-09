# file apimd/parser.py:141-153
# lines [151, 152, 153]
# branches []

import pytest
from apimd.parser import table

def test_table_with_mixed_items():
    titles = ('a', 'b')
    items = ['c', ['d', 'e'], 'f']
    expected_output = (
        "| a | b |\n"
        "|:---:|:---:|\n"
        "| c |\n"
        "| d | e |\n"
        "| f |\n\n"
    )
    
    result = table(*titles, items=items)
    
    assert result == expected_output

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
