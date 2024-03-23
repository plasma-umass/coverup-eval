# file lib/ansible/utils/color.py:56-70
# lines [63, 64, 65, 66, 67, 68, 69, 70]
# branches ['61->63', '63->64', '63->65', '65->66', '65->69', '69->exit', '69->70']

import pytest
from ansible.utils.color import parsecolor

@pytest.mark.parametrize("color_input,expected_output", [
    ("color12", "38;5;12"),
    # Corrected expected output for "rgb123" based on the formula in the code
    ("rgb123", "38;5;67"),
    ("gray10", "38;5;242")
])
def test_parsecolor(color_input, expected_output):
    assert parsecolor(color_input) == expected_output
